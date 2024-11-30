import papermill as pm
from datetime import datetime

notebooks = ["Notebook\fetch_periodically.py", "Notebook\data-explorer.ipynb"]

for notebook in notebooks:
    try:
        output = f"output_{notebook.split('.')[0]}_{datetime.now().strftime('%Y%m%d%H%M%S')}.ipynb"
        pm.execute_notebook(notebook, output)
        print(f"Executed {notebook}, saved as {output}")
    except Exception as e:
        print(f"Failed to execute {notebook}: {e}")
