# Python Unit Testing & Code Coverage

Practice project for **Test-Driven Development (TDD)** using Python's `unittest` and `nose2`, with **100% code coverage**.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| `uv` | Package & project manager |
| `unittest` | Built-in test framework |
| `unittest.mock` | Mocking & test doubles |
| `nose2` | Test runner |
| `coverage` | Code coverage measurement |

---

## Project Structure

```
project/
├── coe_6810110275/   # Source code (algorithms)
└── tests/            # Unit tests
```

---

## Algorithms Covered

- **Basics:** FizzBuzz, Staircase, Prime Checker
- **HackerRank:** Cat and Mouse, Funny String, Alternating Characters, Caesar Cipher, Two Characters, Grid Challenge
- **Mocking:** Random number generation (`randint`, `uniform`) using `@patch`

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/psu6810110275/project.git
cd project

# Install dependencies
uv sync
```

## Running Tests

```bash
# Run all tests
uv run nose2

# Run with coverage report
uv run coverage run -m nose2
uv run coverage report -m
```
