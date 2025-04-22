import streamlit as st
import sympy as sp
import pandas as pd
import itertools
import re

# Streamlit App Title
st.title("Truth Table Generator for Discrete Mathematics")

# Introduction
st.write("""
#### **Operators Supported**
- **AND**: `&`  (e.g., `A & B`)
- **OR**: `|`  (e.g., `A | B`)
- **NOT**: `~`  (e.g., `~A`)
- **IMPLICATION (→)**: `>>`  (e.g., `A >> B`)
- **BI-CONDITIONAL (↔)**: `==` (Handled as `Eq(A, B)`)
- **XOR (⊕)**: `^`  (Handled as `Xor(A, B)`)

⚠ **Important:**  
- The NOT (`~`) operator should be applied **only to a single variable** (`~A` is valid, `A ~ B` is NOT).
- Avoid incorrect combinations like `A |& B` (Use `A & B` or `A | B` instead).

💡 **Examples:**  
- `A & B` (AND)
- `A | B` (OR)
- `~A` (NOT)
- `A >> B` (IMPLICATION)
- `A == B` (BI-CONDITIONAL)
- `A ^ B` (XOR)
""")

# User input for logical expression
expr_str = st.text_input("Enter a logical expression:", "A ^ B")

# Function to validate and process logical expression
def process_expression(expression):
    try:
        # Replace XOR (^) with `Xor(A, B)`
        expression = re.sub(r'(\w+)\s*\^\s*(\w+)', r'Xor(\1, \2)', expression)

        # Replace Bi-Conditional (==) with `Eq(A, B)`
        expression = re.sub(r'(\w+)\s*==\s*(\w+)', r'Eq(\1, \2)', expression)

        # Parse the expression with SymPy
        expr = sp.sympify(expression, evaluate=False, locals={"Eq": sp.Eq, "Xor": sp.Xor})

        # Ensure the expression is symbolic
        if isinstance(expr, bool):
            return None, "❌ The expression evaluates to a boolean value. Please provide a symbolic expression."

        return expr, None  # Valid expression
    except Exception:
        return None, "❌ Invalid logical expression. Check for missing variables or incorrect syntax."

# Process the user input
expr, error_message = process_expression(expr_str)

if error_message:
    st.error(error_message)
else:
    try:
        # Extract unique variables from the expression
        variables = sorted(expr.free_symbols, key=lambda x: x.name)

        # Check if variables exist
        if not variables:
            raise ValueError("No valid variables found in the expression. Use symbols like A, B, C.")

        # Generate all possible binary combinations for the variables
        num_vars = len(variables)
        truth_values = list(itertools.product([0, 1], repeat=num_vars))

        # Compute the truth table results
        table_data = []
        for values in truth_values:
            val_dict = dict(zip(variables, values))  # Map variables to their binary values
            result = expr.subs(val_dict)  # Compute the expression result

            # Convert sympy Boolean values to Python integers (1 or 0)
            result = int(bool(result))

            table_data.append(list(values) + [result])

        # Convert to DataFrame
        headers = [str(var) for var in variables] + [str(expr)]
        df = pd.DataFrame(table_data, columns=headers)

        # Display the truth table
        st.write("### Truth Table:")
        st.dataframe(df)

        # Display LaTeX formatted expression
        st.latex(sp.latex(expr))

        # Additional Explanation (as per syllabus)
        if df.iloc[:, -1].nunique() == 1:  # Check if all results are the same
            if df.iloc[:, -1].iloc[0] == 1:
                st.success("This expression is a **Tautology** (Always True).")
            else:
                st.error("This expression is a **Contradiction** (Always False).")
        else:
            st.info("This expression is a **Contingency** (Not always True or False).")

        # CSV download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(label="📥 Download Truth Table", data=csv, file_name="truth_table.csv", mime="text/csv")

    except Exception as e:
        st.error(f"❌ Invalid Expression: {e}")
