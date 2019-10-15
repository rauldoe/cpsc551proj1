
import re
import xmlrpc.client

import ConverterModule

class DistributedOperation:

    xmlrpcUrl = "http://localhost:8088/"

    def __init__(self):
        self.readList = []
        self.writeList = []
        with xmlrpc.client.ServerProxy(DistributedOperation.xmlrpcUrl, allow_none=True) as proxy:
            self.srv = proxy.LindaDistributed

    def _in(self, t):
        converted = ConverterModule.Converter.tupleToXMLRPCTuple(t)
        return self.srv._in(converted)

    def _rd(self, t):
        converted = ConverterModule.Converter.tupleToXMLRPCTuple(t)
        return self.srv._rd(converted)

    def _out(self, t):
        converted = ConverterModule.Converter.tupleToXMLRPCTuple(t)
        return self.srv._out(converted)
    
    def _out_next(self, t):
        topic = t[1]
        index = self.findTopic(self.writeList, topic)
        # print('i: ' + str(index))
        if (index == -1):
            self.writeList.append({'topic' : topic, 'count' : 0})
            index = len(self.writeList)-1

        topicInfo = self.writeList[index]
        # print('t: ' + str(topicInfo))

        t1 = t + (topicInfo['count'],)
        print(str(t1))
        m = self._out(t1)
        topicInfo['count'] += 1
        self.writeList[index] = topicInfo
        # print('l: ' + str(self.writeList))

        return m
    
    def _rd_next(self, t):
        topic = t[1]
        index = self.findTopic(self.readList, topic)
        if (index == -1):
            self.readList.append({'topic' : topic, 'count' : 0})
            index = len(self.readList)-1

        topicInfo = self.readList[index]

        t1 = t + (topicInfo['count'],)
        m = self._rd(t1)
        topicInfo['count'] += 1
        self.readList[index] = topicInfo
        
        return m

    def findTopic(self, lookup, topic):
        index = -1

        for i in range(len(lookup)):
            if (lookup[i]['topic'] == topic):
                index = i
                break
        return index