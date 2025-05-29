# JavaScript Operators: A Beginner's Guide

## What are Operators?

Operators are special symbols in JavaScript that perform operations on values and variables, known as operands. Think of them as actions that manipulate data.

## Types of Operators

JavaScript offers a variety of operators. Here's a breakdown of some of the most common ones:

### 1. Arithmetic Operators

These operators perform mathematical calculations:

*   `+` (Addition): Adds two operands.

    ```javascript
    let x = 5;
    let y = 2;
    let sum = x + y; // sum is 7
    console.log(sum);
    ```

*   `-` (Subtraction): Subtracts the second operand from the first.

    ```javascript
    let x = 5;
    let y = 2;
    let difference = x - y; // difference is 3
    console.log(difference);
    ```

*   `*` (Multiplication): Multiplies two operands.

    ```javascript
    let x = 5;
    let y = 2;
    let product = x * y; // product is 10
    console.log(product);
    ```

*   `/` (Division): Divides the first operand by the second.

    ```javascript
    let x = 10;
    let y = 2;
    let quotient = x / y; // quotient is 5
    console.log(quotient);
    ```

*   `%` (Modulus): Returns the remainder of a division operation.

    ```javascript
    let x = 10;
    let y = 3;
    let remainder = x % y; // remainder is 1
    console.log(remainder);
    ```

*   `**` (Exponentiation): Raises the first operand to the power of the second.

    ```javascript
    let x = 2;
    let y = 3;
    let power = x ** y; // power is 8 (2*2*2)
    console.log(power);
    ```

*   `++` (Increment): Increases the value of a variable by 1. Can be used as a prefix (`++x`) or postfix (`x++`).

    ```javascript
    let x = 5;
    x++; // x is now 6
    console.log(x);
    ```

*   `--` (Decrement): Decreases the value of a variable by 1. Can be used as a prefix (`--x`) or postfix (`x--`).

    ```javascript
    let x = 5;
    x--; // x is now 4
    console.log(x);
    ```

### 2. Assignment Operators

These operators assign values to variables:

*   `=` (Assignment): Assigns the value on the right to the variable on the left.

    ```javascript
    let x = 10; // Assigns the value 10 to the variable x
    ```

*   `+=` (Addition Assignment): Adds the value on the right to the variable on the left and assigns the result to the variable.

    ```javascript
    let x = 5;
    x += 3; // x is now 8 (x = x + 3)
    console.log(x);
    ```

*   `-=` (Subtraction Assignment): Subtracts the value on the right from the variable on the left and assigns the result to the variable.

    ```javascript
    let x = 5;
    x -= 3; // x is now 2 (x = x - 3)
    console.log(x);
    ```

*   `*=` (Multiplication Assignment): Multiplies the variable on the left by the value on the right and assigns the result to the variable.

    ```javascript
    let x = 5;
    x *= 3; // x is now 15 (x = x * 3)
    console.log(x);
    ```

*   `/=` (Division Assignment): Divides the variable on the left by the value on the right and assigns the result to the variable.

    ```javascript
    let x = 15;
    x /= 3; // x is now 5 (x = x / 3)
    console.log(x);
    ```

*   `%=` (Modulus Assignment): Calculates the modulus of the variable on the left by the value on the right and assigns the result to the variable.

    ```javascript
    let x = 10;
    x %= 3; // x is now 1 (x = x % 3)
    console.log(x);
    ```

*   `**=` (Exponentiation Assignment): Raises the variable on the left to the power of the value on the right and assigns the result to the variable.

    ```javascript
    let x = 2;
    x **= 3; // x is now 8 (x = x ** 3)
    console.log(x);
    ```

### 3. Comparison Operators

These operators compare two operands and return a Boolean value (`true` or `false`):

*   `==` (Equal to): Checks if two operands are equal in value (but not necessarily in type). **Avoid using this! Use `===` instead.**

    ```javascript
    let x = 5;
    let y = "5";
    console.log(x == y); // true (because of type coercion)
    ```

*   `===` (Strict Equal to): Checks if two operands are equal in value *and* type.

    ```javascript
    let x = 5;
    let y = "5";
    console.log(x === y); // false (because they are different types)
    ```

*   `!=` (Not Equal to): Checks if two operands are not equal in value (but not necessarily in type). **Avoid using this! Use `!==` instead.**

    ```javascript
    let x = 5;
    let y = "5";
    console.log(x != y); // false (because of type coercion)
    ```

*   `!==` (Strict Not Equal to): Checks if two operands are not equal in value *or* type.

    ```javascript
    let x = 5;
    let y = "5";
    console.log(x !== y); // true (because they are different types)
    ```

*   `>` (Greater Than): Checks if the left operand is greater than the right operand.

    ```javascript
    let x = 5;
    let y = 2;
    console.log(x > y); // true
    ```

*   `<` (Less Than): Checks if the left operand is less than the right operand.

    ```javascript
    let x = 5;
    let y = 2;
    console.log(x < y); // false
    ```

*   `>=` (Greater Than or Equal to): Checks if the left operand is greater than or equal to the right operand.

    ```javascript
    let x = 5;
    let y = 5;
    console.log(x >= y); // true
    ```

*   `<=` (Less Than or Equal to): Checks if the left operand is less than or equal to the right operand.

    ```javascript
    let x = 5;
    let y = 5;
    console.log(x <= y); // true
    ```

### 4. Logical Operators

These operators perform logical operations, typically used with Boolean values:

*   `&&` (Logical AND): Returns `true` if both operands are `true`.

    ```javascript
    let x = 5;
    let y = 2;
    console.log(x > 0 && y < 5); // true (because both conditions are true)
    ```

*   `||` (Logical OR): Returns `true` if at least one of the operands is `true`.

    ```javascript
    let x = 5;
    let y = 2;
    console.log(x < 0 || y < 5); // true (because the second condition is true)
    ```

*   `!` (Logical NOT): Returns the opposite of the operand's Boolean value.

    ```javascript
    let x = 5;
    console.log(!(x > 0)); // false (because x > 0 is true, and !true is false)
    ```

### 5. String Operators

JavaScript also has operators for working with strings:

*   `+` (Concatenation): Joins two strings together.

    ```javascript
    let firstName = "John";
    let lastName = "Doe";
    let fullName = firstName + " " + lastName; // fullName is "John Doe"
    console.log(fullName);
    ```

*   `+=` (Concatenation Assignment): Appends the value on the right to the string variable on the left and assigns the result to the variable.

    ```javascript
    let message = "Hello";
    message += " World!"; // message is now "Hello World!"
    console.log(message);
    ```

### 6. Conditional (Ternary) Operator

This is a shorthand way of writing an `if...else` statement.

*   `condition ? expression1 : expression2`

    If the `condition` is `true`, `expression1` is executed. Otherwise, `expression2` is executed.

    ```javascript
    let age = 20;
    let message = (age >= 18) ? "You are an adult." : "You are a minor.";
    console.log(message); // You are an adult.
    ```

## Operator Precedence

Operators have a specific order of precedence, which determines the order in which they are evaluated in an expression. You can use parentheses `()` to override the default precedence. For example:

```javascript
let result = 5 + 2 * 3; // result is 11 (multiplication is done before addition)
let result2 = (5 + 2) * 3; // result2 is 21 (parentheses force addition first)
```

## Conclusion

Understanding operators is crucial for writing effective JavaScript code. Experiment with different operators and expressions to solidify your knowledge. Good luck!