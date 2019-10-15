
require "rinda/tuplespace"
require "rinda/rinda"

module LindaDistributed
    class Common

        @@Port = 4000
        @@Url = "druby://localhost:#{@@Port}"

        @@TopicPort = 3000
        @@TopicUrl = "druby://localhost:#{@@TopicPort}"

        @OList = [:read, :write, :take]
        @@OperationLookup = { 
            @OList[0] => {:key => @OList[0], :tag => "_rd"},
            @OList[1] => {:key => @OList[1], :tag => "_out"},
            @OList[2] => {:key => @OList[2], :tag => "_in"} 
        }

        def self.Port
            @@Port
        end
        def self.Url
            @@Url
        end
        def self.OList
            @@OList
        end
        def self.OperationLookup
            @@OperationLookup
        end

    end

    class Server

        def start(url)
            ts = Rinda::TupleSpace.new
            DRb.start_service(url, ts)
            puts "Rinda listening on #{DRb.uri}..."
            DRb.thread.join
        end
    end

    class Client
        
        @url = nil
        @ts = nil

        def initialize(url)
            @url = url
            @ts = DRbObject.new(nil, url)
        end

        def send(method, t)
            puts "method: #{method} tuple: #{t}"
            @ts.send(method, t)
        end
    end
end