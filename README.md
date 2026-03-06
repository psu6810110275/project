# Python Unit Testing & Code Coverage 

This repository contains a collection of Python algorithms and their corresponding unit tests.
The primary goal of this project is to practice Test-Driven Development (TDD), the Arrange-Act-Assert (AAA) pattern, and achieve **100% Code Coverage** using Python's `unittest` and `nose2` frameworks.

##  Technologies Used
* **Python 3**
* **uv** - Fast Python package and project manager
* **unittest** - Built-in Python testing framework
* **unittest.mock** - For Test Doubles and Mocking
* **nose2 & coverage** - Test runner and code coverage measurement

##  Project Structure
The project separates production code from test code:
* `coe_6810110275/` - Contains all the core logic and algorithm solutions.
* `tests/` - Contains all the unit tests corresponding to the production code.

## Implemented Challenges
1. **Warm-ups & Basics:**
   * Prime Number Checker
   * FizzBuzz
   * Staircase
2. **HackerRank Homework:**
   * Cat and a Mouse
   * Funny String
   * Alternating Characters
   * Caesar Cipher 1
   * Two Characters
   * Grid Challenge
3. **Mocking (Test Doubles):**
   * Testing random number generation (`randint` and `uniform`) using `@patch`.

## Setup & Installation

This project uses `uv` for dependency management. 

1. **Clone the repository:**
   ```bash
   git clone https://github.com/psu6810110275/project.git
   cd project
