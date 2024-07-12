import os
import subprocess

# Define the output file names
latex_file = 'output.tex'
pdf_file = 'output.pdf'

# Convert the generated Markdown file to a LaTeX file using Pandoc with the custom template
subprocess.run(['pandoc', '_site/combined.md', '-o', latex_file, '--template=template.tex'])

# Compile the LaTeX file to PDF using pdflatex
subprocess.run(['pdflatex', latex_file])

# Clean up temporary files
aux_files = [latex_file, 'output.aux', 'output.log']
for aux_file in aux_files:
    if os.path.exists(aux_file):
        os.remove(aux_file)

print(f'PDF generated: {pdf_file}')
