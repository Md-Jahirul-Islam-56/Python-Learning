import requests
import os

# Repository details
REPO_OWNER = "greyhatguy007"
REPO_NAME = "Machine-Learning-Specialization-Coursera"
BRANCH = "main"  # Adjust if the default branch is different

# GitHub API URL to fetch repository tree
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/git/trees/{BRANCH}?recursive=1"

# Base URL for raw content
RAW_URL_BASE = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/"

# Directory to save downloaded notebooks
SAVE_DIR ="D:\RazonCoding\machine learning\ML_Andrew_NG_Practical"

os.makedirs(SAVE_DIR, exist_ok=True)

# Fetch the repository tree from GitHub

response = requests.get(API_URL)
if response.status_code != 200:
    raise Exception(f"GitHub API request failed with status code {response.status_code}")

# Parse the JSON response
repo_tree = response.json()

# Filter for .ipynb files
notebook_paths = [item['path'] for item in repo_tree.get('tree', []) if item['path'].endswith('.ipynb')]

# Download each notebook
for notebook_path in notebook_paths:
    raw_url = RAW_URL_BASE + notebook_path
    response = requests.get(raw_url)
    if response.status_code == 200:
        # Save notebook to the specified directory, preserving folder structure
        save_path = os.path.join(SAVE_DIR, notebook_path)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {notebook_path}")
    else:
        print(f"Failed to download: {notebook_path}")

print(f"All notebooks have been downloaded to the '{SAVE_DIR}' directory.")
