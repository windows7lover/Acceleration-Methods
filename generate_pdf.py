import os
import pypandoc

# Define the directory containing the markdown files
md_dir = 'Acceleration-Methods/_monographtypos'

# Define the output filenames
combined_md_file = 'combined.md'
output_pdf_file = 'output.pdf'
'''
def strip_yaml_header(content):
    """Strip YAML header from the content."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) == 3:
            return parts[2].strip()
    return content

# Combine content from all markdown files
combined_content = ""

for filename in os.listdir(md_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(md_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            content_without_header = strip_yaml_header(content)
            combined_content += content_without_header + "\n\n"

# Write the combined content to a markdown file
with open(combined_md_file, 'w', encoding='utf-8') as file:
    file.write(combined_content)
'''
# Convert the combined markdown file to PDF using pypandoc
pypandoc.convert_file(combined_md_file, 'pdf', outputfile=output_pdf_file)

print(f'PDF generated: {output_pdf_file}')
