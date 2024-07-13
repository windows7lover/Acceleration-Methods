import os

# Define the order of the files
file_order = [
    'Introduction.md',
    'ChebyshevAcceleration.md',
    'NonlinearAcceleration.md',
    'NesterovAcceleration.md',
    'ProximalAccelerationandCatalyst.md',
    'UsefulInequalities.md',
    'VariationsonNesterovAcceleration.md',
    'OnWorst-caseAnalysesforFirst-orderMethods.md',
    'Acknowledgements.md',
    'References.md'
]

# Directory containing the Markdown files
directory = '_site'

# Path for the combined Markdown file
combined_file_path = os.path.join(directory, 'combined.md')

# Combine the contents of the files in the specified order
combined_content = ""

for filename in file_order:
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            combined_content += file.read() + "\n\n"
    else:
        print(f"Warning: {filename} not found in {directory}")

# Write the combined content to combined.md
with open(combined_file_path, 'w', encoding='utf-8') as combined_file:
    combined_file.write(combined_content)

print(f"Combined Markdown file generated at {combined_file_path}")
