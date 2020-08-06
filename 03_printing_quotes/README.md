# [3 of 57] Printing Quotes

### Problem Statement:

Create a program that prompts for a quote and an author. Display the quotation and author as shown in the example output.

        nouns:
        - quote
        - author
        
        verbs:
        - prompts
        - display

---
### Example Output:
        
        What is the quote? These aren't the droids you're looking for.
        Who said it? Obi-Wan Kenobi
        Obi-Wan Kenobi says, "These aren't the droids you're looking for."

---
### Constraints:

* Use a single output statement to produce this output, using appropriate string-escaping techniques for quotes.
* If your language supports string interpolation or string substitution, don't use it for this exercise. Use string concatenation instead.

---
### Inputs, Processes, Outputs:
        
        Inputs:
        - quote and author
        
        Processes:
        - prompts and displays
        
        Outputs:
        - author and quotation

---
### Test Plan:
        
        Inputs:
        - quote: These aren't the droids you're looking for.
        - author: Obi-Wan Kenobi
        
        Expected Result:
          Obi-Wan Kenobi says, "These aren't the droids you're looking for."
        
        Actual Results:

---
### Pseudocode:
        
        QuotePrinter
          - Prompts for a quote "What is the quote?"
          - Prompts for author "Who said it?"
          
          - Combine quote and author, using _escape characters_ to handle quotations.
          
          - Display author and quote.
        end

---
### TODO:

* In Chapter 7, _Data Structures_, you'll practice working with lists of data. Modify this program so that instead of prompting for quotes from the user, you create a structure that holds quotes and their associated attributions and then display all of the quotes using the format in the example. An array of maps would be a good choice.
