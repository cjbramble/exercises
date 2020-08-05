# [2 of 57] Counting the Number of Characters

### Problem Statement:

Create a program that prompts for an input string and displays output that shows the input string and the number of characters the string contains.

        Nouns:
        - input string
        - number of characters

        Verbs:
        - prompts
        - displays

---
### Example Output:

        What is the input string? Homer
        Homer is 5 characters.

---
### Constraints:

* Be sure the output contains the original string.
* Use a single output statement to construct the output.
* Use a built-in function of the programming language to determine the length of the string.

---
### Inputs, Processes, Outputs:
        
        Inputs:
        - input string

        Processes:
        - prompts and displays

        Outputs:
        - string and number of characters it counted

---
### Test Plan:

        Inputs:
        - string: Homer

        Expected Results:
          Homer has 5 characters.

        Actual Results:

---
### Pseudocode

        CountCharacters
          - Prompts for input string with "What is your input string?"
          
          - Count = length of string
          
          - Displays input string and character Count
          
          - If input string isn't given, prompt user to enter input string
        end

---
### TODO:

* If the user enters nothing, state that the user must enter something into the program.
* Implement this program using a graphical user interface and update the character counter every time a key is pressed. If your language doesn't have a particularly friendly GUI library, try doing this exercise with HTML and JavaScript instead.

---
