class SayingHello
    def initialize
        get_name
        print_name
    end
  
    def get_name
      print "What is your name? "
      @name = gets.chomp
    end
  
    def print_name
        print "Hello #{@name}, nice to meet you!\n"
    end
  end
  
  SayingHello.new
