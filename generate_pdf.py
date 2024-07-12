import os
import subprocess

# Define the directory containing the markdown files
markdown_dir = 'pages/monograph'

# Define the output file names
latex_file = 'output.tex'
pdf_file = 'output.pdf'

# Combine content of all markdown files into a single markdown file
combined_markdown = ''
for root, _, files in os.walk(markdown_dir):
    for file in sorted(files):
        if file.endswith('.md'):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                combined_markdown += f.read() + '\n\n'

# Write the combined markdown content to a temporary file
with open('combined.md', 'w', encoding='utf-8') as f:
    f.write(combined_markdown)

# Convert the combined markdown file to a LaTeX file using Pandoc with the custom template
subprocess.run(['pandoc', 'combined.md', '-o', latex_file, '--template=template.tex'])

# Compile the LaTeX file to PDF using pdflatex
subprocess.run(['pdflatex', latex_file])

# Clean up temporary files
aux_files = ['combined.md', latex_file, 'output.aux', 'output.log']
for aux_file in aux_files:
    if os.path.exists(aux_file):
        os.remove(aux_file)

print(f'PDF generated: {pdf_file}')
