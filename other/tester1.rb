
require "./ConverterModule"

# test
# [ Regexp.new("^[-+/*]$"), 1, "tester", Range.new(5, 49), Module.const_get('String'), Module.const_get('Numeric'), :ewe, nil ]

# output: [ { "regexp" => "^[-+/*]$" }, 1, "tester", { "from" => 10, "to" => 6 }, { "class" => "String" }, { "class" => "Numeric" }, { "symbol" => "chopstick" }, nil ]

loop do
    print "Expression: "
    $stdout.flush

    input = (gets).strip

    if (input == 'exit')
        break
    else
        expr = eval(input)
        converted = ConverterModule::Converter.tupleToXMLRPCTuple(expr)
        
        for i in converted
            puts 'class: ' + i.class.name
            puts i   
        end
    end
end