begin
  puts "What is your input string?"

  input_string = gets.chomp
end while input_string.empty?
  
puts "#{input_string} has #{input_string.length} characters."
