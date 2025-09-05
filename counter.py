import os

base_path = "."
count = sum(
    1 for name in os.listdir(base_path)
    if os.path.isdir(os.path.join(base_path, name)) and name[0].isdigit()
)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = content.replace(
    "<!---PROBLEM_COUNT-->", f"{count} problems solved 🚀"
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
