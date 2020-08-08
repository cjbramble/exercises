puts "What is your first number?"
first_input = gets.chomp

puts "What is your second number?"
second_input = gets.chomp

first_number = first_input.to_i
second_number = second_input.to_i

puts "#{first_number} + #{second_number} = #{first_number + second_number}", "\n",
     "#{first_number} - #{second_number} = #{first_number - second_number}", "\n",
     "#{first_number} * #{second_number} = #{first_number * second_number}", "\n",
     "#{first_number} / #{second_number} = #{first_number / second_number}", "\n"
