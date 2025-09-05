import os
import re

base_path = "."
count = sum(
    1 for name in os.listdir(base_path)
    if os.path.isdir(os.path.join(base_path, name)) and name[0].isdigit()
)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_block = f"<!-- PROBLEM_COUNT:START -->\n{count} problems solved 🚀\n<!-- PROBLEM_COUNT:END -->"

pattern = r"<!-- PROBLEM_COUNT:START -->.*?<!-- PROBLEM_COUNT:END -->"
new_content = re.sub(pattern, new_block, content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
