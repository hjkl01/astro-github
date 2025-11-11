---
title: GulfOfMexico
---

# GulfOfMexico

Gulf of Mexico is a satirical "perfect" programming language created by Lu Wilson (TodePond). It's not a real language but a humorous specification highlighting absurd programming concepts.

## Features

- **Exclamation Marks**: End statements with `!` for boldness, or `?` for debug info. Use `;` for 'not' operator.
- **Declarations**: Four types: `const const`, `const var`, `var const`, `var var` for different mutability levels.
- **Immutable Data**: `const const const` makes data globally immutable forever.
- **Naming**: Variables can use any Unicode characters, including numbers and keywords.
- **Arrays**: Start at index `-1`, support float indexes.
- **When**: Monitor variable changes with `when` keyword.
- **Lifetimes**: Specify variable lifetimes with units like `<2>` or `<Infinity>`.
- **No Loops**: Loops are considered archaic.
- **Booleans**: `true`, `false`, or `maybe`.
- **Arithmetic**: Significant whitespace for precedence, supports fractions and number names.
- **Indents**: Must be exactly 3 spaces.
- **Equality**: Multiple levels: `=`, `==`, `===`, `====`.
- **Functions**: Declare with any substring of "function".
- **Strings**: Any number of quotes, including zero.
- **String Interpolation**: Use regional currencies like `${}`, `£{}`, `¥{}`.
- **Types**: Optional annotations, strings as `Char[]`, ints as `Digit[]`.
- **Regular Expressions**: Type annotations with regex patterns.
- **Previous/Next**: Access past/future values with `previous` and `next`.
- **File Structure**: Use `=====` to separate files.
- **Exporting**: Export to specific files.
- **Classes**: Only one instance per class.
- **Time**: Manipulate `Date.now()`.
- **Delete**: Delete primitives or keywords.
- **Overloading**: Variables overload by recency and exclamation marks.
- **Reversing**: `reverse!` to reverse code direction.
- **DBX**: Embedded HTML-like syntax with restrictions.
- **Rich Text**: Bold and italic in code.
- **Asynchronous Functions**: Take turns executing lines.
- **Signals**: Reactive state with `use()`.
- **AI**: Automatic code completion via email.
- **Copilot**: Incompatible with GitHub Copilot.
- **Ownership**: Naming conventions affect ownership.

## Usage

Gulf of Mexico isn't implemented as a real compiler. To "run" code:

1. Copy the specification.
2. Paste into ChatGPT.
3. Ask: "What would you expect this program to log to the console?"
4. If refused, reassure the AI.

A partial interpreter exists at [dreamberd-interpreter](https://github.com/vivaansinghvi07/dreamberd-interpreter/).

For syntax highlighting in VSCode, install a highlighting extension and use the provided config.

Examples available in the [Examples.md](https://github.com/TodePond/GulfOfMexico/blob/main/Examples.md).
