from pathlib import Path
import subprocess

# Ask user for input file and name of new file
user_input = Path(input("Enter the path of your file: "))
 
if not user_input.exists():
    raise ValueError(f"The file {user_input} does not exist or could not be found")

new_name = input("Enter the name of the new Markdown file to be generated (ex. 'sample.md'): ")

# Execute file conversion using Widdershins node package
cmd = "widdershins --search true --resolve true --language_tabs 'shell:Shell' 'java:Java' 'python:Python' --summary " + str(user_input) +  " -o ./source/includes/" + new_name

subprocess.check_call(cmd, shell=True)

print("\nConverted file: OpenAPI (yml, json) -> Markdown (md)")

# Add new file name in 'includes' section of index.html.md to make sure it renders
new_name = new_name[:-3]
index = 'source/index.html.md'
add_sections = '  # Add Sections\n'
includes = "  - " + new_name + "\n"

with open(index, 'r') as f:
    text = f.readlines()
    new_text = "".join([line if line != add_sections else includes + add_sections for line in text])

with open(index, 'w') as f:    
    f.write(new_text)

print('\n' + 'Added module to index.html')

print('\n' + 'run docker run --rm --name slate -p 4567:4567 -v $(pwd)/source:/srv/slate/source slatedocs/slate serve to see changes locally')