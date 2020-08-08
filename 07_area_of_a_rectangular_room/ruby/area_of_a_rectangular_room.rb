FEET_TO_METERS = 0.09290304

puts "What is the length of the room in feet?"
length_in_feet = gets.chomp

puts "What is the width of the room in feet?"
width_in_feet = gets.chomp

area_in_feet = length_in_feet.to_i * width_in_feet.to_i
area_in_meters = area_in_feet.to_i * FEET_TO_METERS

puts "You entered dimensions of #{length_in_feet} in feet by #{width_in_feet} feet."
puts "The area is\n#{area_in_feet} square feet\n#{area_in_meters} square meters"
