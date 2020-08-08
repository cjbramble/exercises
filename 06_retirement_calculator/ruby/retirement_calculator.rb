require 'Date'

puts "What is your current age?"

current_age_input = gets.chomp

puts "At what age would you like to retire?"

age_to_retire_input = gets.chomp

current_age = current_age_input.to_i
age_to_retire = age_to_retire_input.to_i

years_to_retire = age_to_retire - current_age

puts "You have #{years_to_retire} years to retire."

current_year = Date.today.year

puts "It's #{current_year}, so you can retire in #{current_year + years_to_retire}"
