import os
import nbformat

# ✏️ Your credit text (Markdown format)
CREDIT_MARKDOWN = """
> **Note**: This notebook is based on materials from the [Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) by [Andrew Ng](https://www.andrewng.org/), offered through Coursera and DeepLearning.AI.

> Original notebook credit goes to [greyhatguy007](https://github.com/greyhatguy007/Machine-Learning-Specialization-Coursera).

> This version is shared for educational and personal use only.
"""

# 📁 Root folder where your .ipynb files are located
ROOT_DIR = "D:\RazonCoding\machine learning\ML_Andrew_NG_Practical"  # <-- CHANGE THIS!

def add_credit_to_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Check if credit is already in the first cell
    if nb.cells and CREDIT_MARKDOWN.strip() in nb.cells[0].get('source', ''):
        print(f"[✓] Credit already exists in: {notebook_path}")
        return

    # Create a new markdown cell
    credit_cell = nbformat.v4.new_markdown_cell(CREDIT_MARKDOWN.strip())

    # Insert at the top
    nb.cells.insert(0, credit_cell)

    # Save notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print(f"[+] Added credit to: {notebook_path}")

# 🔍 Walk through all files and apply
for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith(".ipynb"):
            add_credit_to_notebook(os.path.join(root, file))
