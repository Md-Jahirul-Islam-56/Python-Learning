# A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.

import pandas as pd
print(pd.__version__)


# # Create a virtual environment
# python -m venv myenv

# # Activate the virtual environment (Linux/macOS)
# source myenv/bin/activate

# # Activate the virtual environment (Windows)
# myenv\Scripts\activate.bat


# # Deactivate the virtual environment
# deactivate

# # Output the list of installed packages and their versions to a file
# pip freeze > requirements.txt

# # Install the packages listed in the requirements.txt file
# pip install -r requirements.txt