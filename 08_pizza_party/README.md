# [8 of 57] Pizza Party

### Problem Statement:

Write a program to evenly divide pizzas. Prompt for the number of people, the number of pizzas, and the number of slices per pizza. Ensure that the number of pieces comes out even. Display the number of pieces of pizza each person should get. If there are leftovers, show the number of leftover pieces.

    Nouns:
      pizzas
      people
      slices
      leftovers

    Verbs:
      divide
      prompt
      display

---
### Example Output:

    How many people? 8
    How many pizzas do you have? 2
    How many slices do the pizzas have? 8

    8 people with 2 pizzas
    Each person gets 2 pieces of pizza.
    There are 0 leftover pieces.

---
### Inputs, Processes, Outputs

    Inputs:
      pizzas
      people
      slices

    Processes:
      calculate

    Output:
      slices
      leftovers

---
### Test Plan:

    Inputs:
      people: 8
      pizzas: 2
      slices: 8

    Expected Results:
      How many people? 8
      How many pizzas do you have? 2
      How many slices do the pizzas have? 8

      8 people with 2 pizzas.
      Each person gets 2 pieces of pizza.
      There are 0 leftover pieces.

    Actual Results:

---
### Pseudocode:

    PizzaParty
      - Prompt for how many people
      - Prompt for how many pizzas
      - Prompt for how many slices the pizzas have

      - Multiply how many pizzas by how many slices per pizza
      - Divide the product by how many people 

      - Display how many people and how many pizzas
      - Display how many slices each person gets
      - Display how many slices are leftover
    End
---
### TODO:

* Revise the program to ensure that inputs are entered as numeric values. Don't allow the user to proceed if the value entered is not numeric.
* Alter the output so it handles pluralization properly, for example: Each person gets 2 pieces, or each person gets 1 piece of pizza. Handle the output for leftover pieces appropriately as well.
* Create a variant of the program that prompts for the number of people and the number of pieces each person wants, and calculate how many full pizzas you need to purchase

---
