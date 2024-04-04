import nbformat
import os

def extract_code_cells(notebook_path, output_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
        code_cells = [cell for cell in nb.cells if cell.cell_type == 'code']
        
        # Safely check for 'output' tag in cell metadata
        output_cells = [cell for cell in code_cells if "tags" in cell.metadata 
                            and "output" in cell.metadata["tags"]]
        
        with open(output_path, 'w') as output_file:
            for cell in output_cells:
                output_file.write(cell.source + '\n\n')

# Example usage
notebooks_dir = './notebooks'
output_dir = './src'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for notebook_file in os.listdir(notebooks_dir):
    if notebook_file.endswith('.ipynb'):
        notebook_path = os.path.join(notebooks_dir, notebook_file)
        output_path = os.path.join(output_dir, notebook_file.replace('.ipynb', '.py'))
        extract_code_cells(notebook_path, output_path)

