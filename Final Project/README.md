✨ Final Project — Backup Integrity Checker

Overview:

The Backup Integrity Checker is a practical, lightweight Python tool I built to verify whether a backup folder truly matches the source it’s meant to protect. I wanted something simple, transparent, and dependable — a program that gives a clear answer without relying on external libraries or complicated syncing systems. This project reflects the way I like to work: clean structure, intentional design, and functions that each do one job well.
The tool scans two folders, compares their contents using file timestamps, and produces a readable report showing which files are missing, which are outdated, and which are fully up‑to‑date. It’s designed for anyone who wants confidence that their backups are complete and current.
This project brings together everything I’ve learned in CS50P — file handling, functions, testing, modular design, and clear program structure — and applies it to a real‑world workflow.

Requirements:

• 	The project is fully implemented in Python.
• 	It solves a real problem: confirming backup integrity.
• 	The program is structured around clean, modular functions.
• 	Code is readable, intentional, and easy to maintain.
• 	A video walkthrough accompanies the submission.
• 	The project includes automated tests using .

Files:

1. project.py
This file contains the full implementation of the Backup Integrity Checker. It includes four top‑level functions:
• 	
Scans a folder and returns a dictionary of filenames mapped to their last‑modified timestamps. It focuses on regular files only, keeping the logic simple and predictable.
• 	
Compares the two dictionaries from  and categorizes files as missing, outdated, or matched. Timestamp comparison keeps the logic efficient and easy to test.
• 	
Produces a clean, human‑readable summary of the comparison results. The output is designed to be clear at a glance, making it easy to understand the state of a backup.
• 	
Orchestrates the program: prompts the user for folder paths, runs the scan and comparison, and prints the final report. It stays intentionally small so the core logic remains in testable helper functions.

2. test_project.py
This file contains automated tests for the three major functions:
, , and .
The tests use Python’s  module to create temporary directories, ensuring the tests are isolated, repeatable, and independent of the user’s actual filesystem. This reflects my preference for predictable, controlled testing environments.

3. README.md
The file you’re reading now. It explains the purpose of the project, the design decisions behind it, how the program works, and how to run it. I wanted the README to feel personal, clear, and thorough — something that reflects the care I put into the project itself.

4. requirements.txt
This project uses only Python’s standard library, so no external dependencies are required. The file exists to satisfy CS50P’s structure requirements.
Project Structure

Submission:

This project follows CS50P’s final project submission guidelines, including:
• 	A complete Python program
• 	A detailed README
• 	A video walkthrough demonstrating the project
• 	Automated tests using 
• 	Submission via 