class PizzaParty
    def initialize
      get_stats
      print_stats
    end
  
    def get_stats
      puts "How many people?"
      @people = gets.chomp.to_i
  
      puts "How many pizzas?"
      @pizzas = gets.chomp.to_i
  
      puts "How many slices do the pizzas have?"
      @slices_per_pizza = gets.chomp.to_i
    end
  
    def total_slices
      @pizzas * @slices_per_pizza
    end
  
    def slices_per_person
      total_slices / @people
    end
  
    def remaining_slices
      total_slices % @people
    end
  
    def print_stats
      puts "#{@people} people with #{@pizzas} pizzas."
      puts "Each person gets #{slices_per_person} pieces of pizza."
      puts "There are #{remaining_slices} leftover."
    end
  end
  
PizzaParty.new
