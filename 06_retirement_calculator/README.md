# [6 of 57] Retirement Calculator

### Problem Statement:

Create a program that determines how many years you have left until retirement and the year you can retire. It should prompt for your current age and the age you want to retire and display the output as shown in the example that follows.

        Nouns:
        - current age
        - age to retire
        
        Verbs:
        - prompt
        - display
        
---
### Example Output:

        What is your current age? 25
        At what age would you like to retire? 65
        You have 40 years left until you can retire.
        It's 2015, so you can retire in 2055.

---
### Constraints:

* Again, be sure to convert the input to numerical data before doing any math.
* Don’t hard-code the current year into your program. Get it from the system time via your programming language.

---
### Inputs, Processes, Outputs:

        Inputs:
        - current age
        - age to retire
        
        Processes:
        - compute
        
        Outputs:
        - years till retirement
        - year of retirement
        
---
### Test Plan:

        Inputs:
        - age: 25
        - age to retire: 65
        
        Expected Results:
          What is your current age? 25
          At what age would you like to retire? 65
          You have 40 years left until you can retire?
          It's 2015, so you can retire in 2055.
          
        Actual Results:
        
---
###  Pseudocode:

        RetirementCalculator
          - Prompt for current age
          - Prompt for age to retire
        
          - Subtract current age from age to retire
          - Add the difference to the current year
        
          - Display difference
          - Display sum
        end

---
### TODO:

* Handle situations where the program returns a negative number by stating that the user can already retire.
