# Epic Language Interpreter

## Overview

Epic is a minimalist procedural programming language with dynamic typing, implemented using ANTLR. This README provides instructions on how to build the interpreter, run tests, and use the language.


## Setting Up the Project

To set up the Epic language interpreter project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/epic-language.git
   cd epic-language
   ```

2. **Install dependencies**:
   Use `uv` to install the project dependencies defined in `pyproject.toml`:
   ```bash
   uv sync
   ```

## Building the Project

To build the Epic language interpreter, follow these steps:

1. **Generate the parser and lexer**:
   Use ANTLR to generate the parser and lexer from the grammar file. Run the following command:
   ```bash
   antlr4 EpicLang.g4 -Dlanguage=Python3 -visitor  
   ```

   This will generate the necessary Python files for the lexer and parser.

## Running Tests

To run the tests for the Epic interpreter, follow these steps:

1. **Run the test script**:
   You can run the tests using the following command:
   ```bash
   uv run tests/test.py
   ```

## Usage

To use the Epic language interpreter, follow these steps:

1. **Create a source file**:
   Write your Epic code in a file with the `.epic` extension. For example, create a file named `example.epic`.

2. **Run the interpreter**:
   Use the following command to run your Epic code:
   ```bash
   uv run interp.py example.epic
   ```

   This will execute the code in `example.epic` and print the output to the console.


## Contributing

Contributions are welcome! If you have suggestions for improvements or want to report a bug, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Educational Purpose

This project is developed as part of the educational process at the [EPIC Institute of Technologies](https://epic-institute.io/). 

## Resources

**ANTLR**: The ANTLR tool used for generating the lexer and parser can be found at [ANTLR Official Website](https://www.antlr.org/).
