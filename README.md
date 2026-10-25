# Bug Fixing Using Cursor AI

This project demonstrates the identification and correction of a bug in a Python program using AI-assisted development with Cursor AI.

## Files Included

### buggy_[program.py](http://program.py)

Contains the original Python program with an indexing error that can cause a list index out of range error.

### fixed_[program.py](http://program.py)

Contains the corrected version of the program.

## Bug Identified

The original program used:

`range(len(numbers) + 1)`

This attempts to access an index beyond the valid range of the list.

## Fix Applied

The loop was corrected to:

`range(len(numbers))`

This ensures that only valid list indexes are accessed.

## Technologies Used

- Python
- Cursor AI
- Functions
- Lists
- Loops

## Objective

The objective is to demonstrate how Cursor AI can assist in identifying and fixing programming errors while improving understanding of the corrected code.

## Author

**Shoryaveer Singh Rathore**  
[B.Tech](http://B.Tech) Computer Science Engineering  
JECRC University