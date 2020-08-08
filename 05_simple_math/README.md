# [5 of 57] Simple Math

### Problem Statement:

Write a program that prompts for two numbers. Print the sum, difference, product, and quotient of the numbers as shown in the example output.

        Nouns:
        - numbers
        - sum
        - difference
        - product
        - quotient
        
        Verbs:
        - prompts
        - adds
        - subtracts
        - multiplies
        - divides
        - outputs

---
### Example Output:

        What is the first number? 10
        What is the second number? 5
        10 + 5 = 15
        10 - 5 = 5
        10 * 5 = 50
        10 / 5 = 2
 
---
### Constraints:

* Values coming from users will be strings. Ensure that you convert these values to numbers before doing the math.
* Keep the inputs and outputs separate from the numerical conversions and other processing.
* Generate a single output statement with line breaks in the appropriate spots.

---
### Inputs, Processes, Outputs

        Inputs:
        - first number
        - second number
        
        Processes:
        - add
        - subtract
        - multiply
        - divide
        
        Outputs:
        - sum
        - difference
        - product
        - quotient

---
### Test Plan:

        Inputs:
        - numbers: 10, 5
        
        Expected Results:
          What is the first number? 10
          What is the second number? 5
          10 + 5 = 15
          10 - 5 = 5
          10 * 5 = 50
          10 / 5 = 2
        
        Actual Results:
        
---
### Pseudocode

        SimpleMath
          - Prompt for first number
          - Prompt for second number
          
          - Add second number to first number
          - Subtract second number from first number
          - Multiply first number by second number
          - Divide first number by second number
          
          - Output sum
          - Output difference
          - Output product
          - Output quotient
        end

---
### TODO:

* Revise the program to ensure that inputs are entered as numeric values. Don't allow the user to proceed if the value entered is not numeric.
* Don't allow the user to enter a negative number.
* Break the program into functions that do the computations. You'll explore functions in Chapter 5, _Functions_.
* Implement this program as a GUI program that automatically updates the values when any value changes.

---
