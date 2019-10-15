# clear;ruby tuplespace.rb

require "./LindaDistributed"

include LindaDistributed

server = Server.new
server.start(Common.Url)

# initialize the topic list
ts = DRbObject.new(nil, "druby://localhost:4000")
ts.send(:write, ["__topic_list__", []])
puts "setting topic list"