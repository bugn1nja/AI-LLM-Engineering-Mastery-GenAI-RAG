from pathlib import Path

# Get the current working directory
current_directory = Path.cwd()
print(f"Current working directory: {current_directory}")   

# Read the contents of a file

path = Path("Intro.txt")  # Replace with your file path
content = path.read_text()
print(f"Contents of the file:\n{content}")