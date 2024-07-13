import subprocess

# Define the output file names
latex_file = 'output.tex'
pdf_file = 'output.pdf'

# Convert the generated Markdown file to a LaTeX file using Pandoc
try:
    subprocess.run(['pandoc', '_site/combined.md', '-o', latex_file], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error converting Markdown to LaTeX: {e}")
    exit(1)

# Compile the LaTeX file to PDF using pdflatex
try:
    subprocess.run(['pdflatex', latex_file], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error compiling LaTeX to PDF: {e}")
    exit(1)

# Move or copy the generated PDF to the expected location
try:
    subprocess.run(['mv', 'output.pdf', '../output.pdf'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error moving PDF file: {e}")
    exit(1)

print(f'PDF generated: {pdf_file}')
