import os

file_path = r'd:\Sebastian\Documents\turismo-ebejico\agroturismo.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract lines starting from 267 (index 266)
# view_file is 1-indexed, so 267 is the 267th line. Index 266.
start_index = 266
content_lines = lines[start_index:]

# Dedent
if content_lines:
    first_line = content_lines[0]
    indent = len(first_line) - len(first_line.lstrip())
    print(f"Detected indentation: {indent} spaces")
    
    dedented_lines = []
    for line in content_lines:
        if len(line) >= indent:
            dedented_lines.append(line[indent:])
        else:
            dedented_lines.append(line.lstrip())
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(dedented_lines)
    print("File fixed successfully.")
else:
    print("Error: No content found at specified lines.")
