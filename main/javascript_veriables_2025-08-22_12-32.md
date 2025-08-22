# JavaScript Variables: A Beginner's Guide

## Understanding Variables

Variables are fundamental building blocks in JavaScript. Think of them as named containers that hold data your program can use. This data can be various types, including numbers, text, and true/false values. The variable's name serves as the label for this container.

## Declaring Variables

Before using a variable, you must declare it. JavaScript provides three keywords for declaring variables: `var`, `let`, and `const`. While `var` was the original method, `let` and `const` are now preferred for their improved scoping rules.

### `let` (Modern Approach)

`let` declares variables with *block scope*. This means the variable is only accessible within the block of code where it's defined (e.g., inside an `if` statement or a `for` loop). `let` allows you to reassign a new value to the variable after its initial declaration.

```javascript
let age = 30;
console.log(age); // Output: 30

if (true) {
  let age = 40;
  console.log(age); // Output: 40 (inside the if block)
}

console.log(age); // Output: 30 (outside the if block - different variable)

let score = 0;
score = score + 10;
console.log(score); // Output: 10
```

### `const` (For Constants)

`const` declares *constants*, variables whose values cannot be changed after they are initially assigned. Like `let`, `const` also has block scope. Use `const` for values that should not be modified during the program's execution.

```javascript
const PI = 3.14159;
console.log(PI); // Output: 3.14159

// PI = 3.14; // This will cause an error! You can't reassign a const variable.
```

**Important:** While you can't reassign a `const` variable itself, if the `const` variable holds an object or an array, you *can* modify the properties of that object or the elements of that array.

```javascript
const myObject = {
  name: "Bob",
  age: 25
};

myObject.age = 26; // This is allowed!
console.log(myObject); // Output: { name: "Bob", age: 26 }

const myArray = [1, 2, 3];
myArray.push(4); // This is also allowed!
console.log(myArray); // Output: [1, 2, 3, 4]
```

### `var` (Historically Used)

`var` was the original way to declare variables in JavaScript. However, due to its *function scope*, it can lead to unexpected behavior in larger programs. It's generally recommended to use `let` or `const` instead of `var` in modern JavaScript.

```javascript
var myName = "Alice";
console.log(myName); // Output: Alice
```

## Variable Naming Conventions

Follow these conventions for clear and maintainable code:

*   **Case-sensitive:** `myName` is different from `myname`.
*   **Start with:** A letter, underscore (`_`), or dollar sign (`$`).
*   **Cannot start with:** A number.
*   **Contain:** Letters, numbers, underscores, and dollar signs.
*   **Descriptive:** Use names that clearly indicate the variable's purpose (e.g., `userName` instead of `u`).
*   **camelCase:** Follow the camelCase convention (e.g., `firstName`, `totalScore`). The first word is lowercase, and each subsequent word starts with an uppercase letter.

## Data Types

Variables in JavaScript can hold different types of data:

*   **String:** Text enclosed in single or double quotes (e.g., `"Hello"`, `'World'`).
*   **Number:** Integers or floating-point numbers (e.g., `10`, `3.14`).
*   **Boolean:** `true` or `false`.
*   **Array:** An ordered list of values (e.g., `[1, 2, 3]`, `["apple", "banana", "cherry"]`).
*   **Object:** A collection of key-value pairs (e.g., `{ name: "Alice", age: 30 }`).
*   **Undefined:** Represents a variable that has been declared but has not been assigned a value.
*   **Null:** Represents the intentional absence of a value.

```javascript
let myString = "This is a string";
let myNumber = 42;
let myBoolean = true;
let myArray = [1, "hello", true];
let myObject = { name: "John", city: "New York" };
let myUndefined; // Value is undefined
let myNull = null;
```

## Best Practices

*   **Declare first:** Always declare your variables before using them.
*   **`const` by default:** Use `const` for variables that should not be reassigned.
*   **`let` for reassignment:** Use `let` for variables that need to be reassigned.
*   **Avoid `var`:** Avoid using `var` in modern JavaScript code.
*   **Descriptive names:** Choose descriptive variable names for better code readability.
*   **Understand scope:** Be aware of the scope of your variables (where they are accessible).

By understanding and following these guidelines, you'll be well on your way to writing clean, maintainable, and error-free JavaScript code!