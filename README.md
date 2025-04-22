Here's a professional and detailed **`README.md`** file for your Streamlit-based Truth Table Generator project, including instructions, usage, and logical expression examples:

* * *

🧠 Truth Table Generator for Discrete Mathematics
=================================================

A simple and interactive **Streamlit web app** that allows students, educators, and logic enthusiasts to generate truth tables for logical expressions used in **Discrete Mathematics**.

📌 Features
-----------

*   Easy-to-use UI for entering logical expressions
    
*   Supports all standard propositional logic operators
    
*   Dynamic generation of truth tables based on user input
    
*   Highlights **Tautology**, **Contradiction**, or **Contingency**
    
*   Option to **download** the truth table as a CSV file
    
*   LaTeX rendering of expressions for readability
    

* * *

🧩 Logical Operators Supported
------------------------------

Operator

Symbol

Example

Meaning

AND

`&`

`A & B`

True if A and B are true

OR

\`

\`

\`A

NOT

`~`

`~A`

Negation of A

IMPLIES

`>>`

`A >> B`

A implies B

BI-COND

`==`

`A == B`

A if and only if B

XOR

`^`

`A ^ B`

A or B, but not both

> ⚠️ **Important Notes:**
> 
> *   Use `~` **only** with one variable, e.g., `~A`.
>     
> *   Group expressions with parentheses if needed.
>     
> *   XOR (`^`) and Bi-Conditional (`==`) must be used with proper syntax due to parsing limitations.
>     

* * *

🚀 Getting Started
------------------

### 🔧 Installation

1.  Clone this repository:
    

`git clone https://github.com/your-username/truth-table-generator.git cd truth-table-generator` 

2.  Install the required Python dependencies:
    

`pip install -r requirements.txt` 

### 🧪 Run the App

`streamlit run app.py` 

* * *

📝 Example Inputs and Expected Outputs
--------------------------------------

Here are logical expressions you can use as inputs to demonstrate all the possible outputs in your truth table generator app. These cover the different logical operators mentioned in your app's instructions:

### 1\. **AND (Conjunction)**

*   **Expression:** `A & B`
    
*   **Expected Output:** `True` only when both `A` and `B` are `True`.
    

### 2\. **OR (Disjunction)**

*   **Expression:** `A | B`
    
*   **Expected Output:** `True` when at least one of `A` or `B` is `True`.
    

### 3\. **NOT (Negation)**

*   **Expression:** `~A`
    
*   **Expected Output:** Inverts the value of `A`.
    

### 4\. **IMPLICATION (→)**

*   **Expression:** `A >> B`
    
*   **Expected Output:** `False` only when `A` is `True` and `B` is `False`.
    

### 5\. **BI-CONDITIONAL (↔)**

*   **Expression:** `A == B`
    
*   **Expected Output:** `True` when both `A` and `B` are either both `True` or both `False`.
    

### 6\. **XOR (Exclusive OR)**

*   **Expression:** `A ^ B`
    
*   **Expected Output:** `True` if exactly one of `A` or `B` is `True`.
    

### 7\. **Combination of AND, OR, and NOT**

*   **Expression:** `A & B | ~C`
    
*   **Expected Output:** `(A AND B) OR (NOT C)` for each variable combination.
    

### 8\. **Complex Expression (Multiple Operators)**

*   **Expression:** `A >> (B | C) & ~(A & B)`
    
*   **Expected Output:** Evaluates the expression `A → (B OR C) AND NOT (A AND B)`.
    

### 9\. **Contradiction (Always False)**

*   **Expression:** `A & ~A`
    
*   **Expected Output:** Always `False`.
    

### 10\. **Tautology (Always True)**

*   **Expression:** `A | ~A`
    
*   **Expected Output:** Always `True`.
    

* * *

📦 `requirements.txt`
---------------------

`streamlit
sympy
pandas` 

* * *

📄 License
----------

This project is licensed under the MIT License. Feel free to fork, use, and contribute!

* * *

