import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",
    "src/Folder_name/__init__.py",
    "src/prompt_template.py",
    ".env",
    ".gitignore", 
    "README.md",
    "setup.py",
    "experiments/trail.ipynb",
    "app.py",
    "static/style.css",
    "requirements.txt", 
    "templates/chat.html",
    "store_index.py"
]

for filepath in list_of_files:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   if filedir !="":
      os.makedirs(filedir, exist_ok=True)
      logging.info(f"Creating directory; {filedir} for the file {filename}")

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass
         logging.info(f"Creating empty file: {filepath}")

   else:
      logging.info(f"{filename} is already exists")
        
        