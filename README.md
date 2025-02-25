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

The tests are located in [tests](tests) folder.To run the tests for the Epic interpreter, follow these steps:

1. **Run the test script**:
   You can run the tests using the following command:
   ```bash
   uv run test.py
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

## Examples

To better understand the syntax of the Epic language, here are some examples:

### Example 1: Variables

```epic
func main() {
    x = 42;              // Integer
    y = true;            // Boolean
    z = [1, 2, 3];       // List
    w = none;            // None
}
```

### Example 2: Arithmetic Operations

```epic
func main() {
    a = 10 + 5;          // Addition
    b = 20 - 7;          // Subtraction
    c = 3 * 4;           // Multiplication
    d = 15 / 3;          // Division
    e = 10 % 3;          // Modulus
}
```

### Example 3: Lists

```epic
func main() {
    list = [1, 2, [3, 4], true];
    print list[2][1];    // Access nested list: prints 4
}
```

### Example 4: Functions

```epic
func add(x, y) {
    return x + y;
}

func main() {
    result = add(3, 5);  // Call function
    print result;        // Prints 8
}
```

### Example 5: Control Structures

```epic
func main() {
    x = 7;
    if x > 10 then {
        x = 0;
        print x;
    } else {
        x = 100;
        print x;
    }

    // While loop
    i = 0;
    while i < 5 do {
        print i;
        i = i + 1;
    }

    // For loop
    for j in 1..10 do {
        print j;
    }
}
```

### Example 6: Break and Continue

```epic
func main() {
    for i in 1..10 do {
        if i == 5 then {
            break;       // Exit the loop when i is 5
        }
        if i % 2 == 0 then {
            continue;    // Skip even numbers
        }
        print i;
    }
}
```

### Complete Example Program

```epic
func main() {
    count = 500;

    is_prime = [false, false];
    while len(is_prime) < count do
        is_prime = is_prime + [true];

    for i in 2..count do {
        if !is_prime[i] then continue;
        j = i*i;
        while j < count do {
            is_prime[j] = false;
            j = j + i;
        }
    }

    primes = [];
    for i in 0..count do {
        if is_prime[i] then
            primes = primes + [i];
    }
    print(primes);
}
```


## Contributing

Contributions are welcome! If you have suggestions for improvements or want to report a bug, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Educational Purpose

This project is developed as part of the educational process at the [EPIC Institute of Technologies](https://epic-institute.io/). 

## Resources

**ANTLR**: The ANTLR tool used for generating the lexer and parser can be found at [ANTLR Official Website](https://www.antlr.org/).
