import os
import re

# Language -> filename mapping
LANGUAGE_MAP = {
    "1": "solution.py",
    "2": "solution.java",
    "3": "solution.cpp",
    "4": "solution.sql",
}

# Difficulty selection
difficulty = input("Difficulty (Easy/Medium/Hard): ").strip().capitalize()

if difficulty not in ["Easy", "Medium", "Hard"]:
    print("Invalid difficulty.")
    exit()

# Problem title
title = input("Problem Title (e.g. 35. Search Insert Position): ").strip()

match = re.match(r"(\d+)\.\s*(.*)", title)

if not match:
    print("Invalid format. Example: 35. Search Insert Position")
    exit()

number = match.group(1)
name = match.group(2)

# Create folder name
folder_name = f"{number}-{name.replace(' ', '-')}"

# Language selection
print("\nChoose Language")
print("1. Python")
print("2. Java")
print("3. C++")
print("4. SQL")

choice = input("> ").strip()

if choice not in LANGUAGE_MAP:
    print("Invalid choice.")
    exit()

solution_file = LANGUAGE_MAP[choice]

# Create directory
path = os.path.join(difficulty, folder_name)

if os.path.exists(path):
    print("\nFolder already exists!")
    exit()

os.makedirs(path)

# Create solution file
open(os.path.join(path, solution_file), "w").close()

# Create notes.md
notes_template = f"""# {number}. {name}

## Intuition

<!-- Explain your thought process -->

## Approach

<!-- Explain what your code does -->

## Key Idea

<!-- Main trick used -->

## Time Complexity

<!-- O(?) -->

## Space Complexity

<!-- O(?) -->

## Pattern

<!-- e.g. Hash Map, Two Pointers, Binary Search -->

## Notes

<!-- Optional -->
"""

with open(os.path.join(path, "notes.md"), "w") as f:
    f.write(notes_template)

print("\n✅ Created successfully!\n")
print(path)
print("├──", solution_file)
print("└── notes.md")

print("\nSuggested Git Commands:\n")
print(f"git add {path}")
print(f'git commit -m "feat: solve {number} {name}"')
print("git push")

