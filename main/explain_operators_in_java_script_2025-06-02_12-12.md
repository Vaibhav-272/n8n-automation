# JavaScript Operators: A Beginner's Guide

## What are Operators  ?

Operators are special symbols in JavaScript that perform operations on values, known as operands. They instruct the JavaScript engine to carry out mathematical, logical, or other manipulations, producing a result. Think of them as the verbs of the JavaScript language.

## Types of Operators

JavaScript offers a variety of operators. Here's a look at some of the most commonly used ones:

### 1. Arithmetic Operators

These operators perform mathematical calculations:

*   **Addition (+):** Adds two operands.

    ```javascript
    let x = 5;
    let y = 3;
    let sum = x + y; // sum is 8
    console.log(sum);
    ```

*   **Subtraction (-):** Subtracts one operand from another.

    ```javascript
    let x = 5;
    let y = 3;
    let difference = x - y; // difference is 2
    console.log(difference);
    ```

*   **Multiplication (\*):** Multiplies two operands.

    ```javascript
    let x = 5;
    let y = 3;
    let product = x * y; // product is 15
    console.log(product);
    ```

*   **Division (/):** Divides one operand by another.

    ```javascript
    let x = 15;
    let y = 3;
    let quotient = x / y; // quotient is 5
    console.log(quotient);
    ```

*   **Modulus (%):** Returns the remainder of a division operation.

    ```javascript
    let x = 5;
    let y = 2;
    let remainder = x % y; // remainder is 1
    console.log(remainder);
    ```

*   **Increment (++):** Increases the value of a variable by 1.

    ```javascript
    let x = 5;
    x++; // x is now 6
    console.log(x);
    ```

*   **Decrement (--):** Decreases the value of a variable by 1.

    ```javascript
    let x = 5;
    x--; // x is now 4
    console.log(x);
    ```

*   **Exponentiation (\*\*):** Raises the first operand to the power of the second operand.

    ```javascript
    let x = 2;
    let power = x ** 3; // power is 8 (2 * 2 * 2)
    console.log(power);
    ```

### 2. Assignment Operators

These operators assign values to variables:

*   **Assignment (=):** Assigns the value of the right operand to the left operand.

    ```javascript
    let x = 5; // Assigns the value 5 to the variable x
    console.log(x);
    ```

*   **Addition Assignment (+=):** Adds the right operand to the left operand and assigns the result to the left operand.  Equivalent to `x = x + y`.

    ```javascript
    let x = 5;
    x += 3; // x is now 8 (x = x + 3)
    console.log(x);
    ```

*   **Subtraction Assignment (-=):** Subtracts the right operand from the left operand and assigns the result to the left operand. Equivalent to `x = x - y`.

    ```javascript
    let x = 5;
    x -= 3; // x is now 2 (x = x - 3)
    console.log(x);
    ```

*   **Multiplication Assignment (\*=):** Multiplies the left operand by the right operand and assigns the result to the left operand. Equivalent to `x = x * y`.

    ```javascript
    let x = 5;
    x *= 3; // x is now 15 (x = x * 3)
    console.log(x);
    ```

*   **Division Assignment (/=):** Divides the left operand by the right operand and assigns the result to the left operand. Equivalent to `x = x / y`.

    ```javascript
    let x = 15;
    x /= 3; // x is now 5 (x = x / 3)
    console.log(x);
    ```

*   **Modulus Assignment (%=):** Calculates the modulus of the left operand by the right operand and assigns the result to the left operand. Equivalent to `x = x % y`.

    ```javascript
    let x = 5;
    x %= 2; // x is now 1 (x = x % 2)
    console.log(x);
    ```

*   **Exponentiation Assignment (\*\*=):** Raises the left operand to the power of the right operand and assigns the result to the left operand. Equivalent to `x = x ** y`.

    ```javascript
    let x = 2;
    x **= 3; // x is now 8 (x = x ** 3)
    console.log(x);
    ```

### 3. Comparison Operators

These operators compare two operands and return a Boolean value (`true` or `false`):

*   **Equal to (==):** Checks if two operands are equal (performs type coercion).

    ```javascript
    let x = 5;
    let y = "5";
    console.log(x == y); // true (because "5" is coerced to 5)
    ```

*   **Not equal to (!=):** Checks if two operands are not equal (performs type coercion).

    ```javascript
    let x = 5;
    let y = "5";
    console.log(x != y); // false (because "5" is coerced to 5)
    ```

*   **Strict equal to (===):** Checks if two operands are equal and of the same type (no type coercion).

    ```javascript
    let x = 5;
    let y = "5";
    console.log(x === y); // false (because x is a number and y is a string)
    ```

*   **Strict not equal to (!==):** Checks if two operands are not equal or not of the same type (no type coercion).

    ```javascript
    let x = 5;
    let y = "5";
    console.log(x !== y); // true (because x is a number and y is a string)
    ```

*   **Greater than (>):** Checks if the left operand is greater than the right operand.

    ```javascript
    let x = 5;
    let y = 3;
    console.log(x > y); // true
    ```

*   **Less than (<):** Checks if the left operand is less than the right operand.

    ```javascript
    let x = 5;
    let y = 3;
    console.log(x < y); // false
    ```

*   **Greater than or equal to (>=):** Checks if the left operand is greater than or equal to the right operand.

    ```javascript
    let x = 5;
    let y = 5;
    console.log(x >= y); // true
    ```

*   **Less than or equal to (<=):** Checks if the left operand is less than or equal to the right operand.

    ```javascript
    let x = 5;
    let y = 5;
    console.log(x <= y); // true
    ```

### 4. Logical Operators

These operators perform logical operations on Boolean values:

*   **Logical AND (&&):** Returns `true` if both operands are `true`; otherwise, it returns `false`.

    ```javascript
    let x = 5;
    let y = 3;
    console.log(x > 0 && y < 5); // true (both conditions are true)
    ```

*   **Logical OR (||):** Returns `true` if at least one operand is `true`; otherwise, it returns `false`.

    ```javascript
    let x = 5;
    let y = 3;
    console.log(x < 0 || y < 5); // true (one condition is true)
    ```

*   **Logical NOT (!):** Reverses the Boolean value of the operand.

    ```javascript
    let x = 5;
    console.log(!(x > 0)); // false (because x > 0 is true, and !true is false)
    ```

### 5. String Operators

JavaScript also has operators for working with strings:

*   **Concatenation (+):** Joins two strings together.

    ```javascript
    let firstName = "John";
    let lastName = "Doe";
    let fullName = firstName + " " + lastName; // fullName is "John Doe"
    console.log(fullName);
    ```

*   **Concatenation Assignment (+=):** Appends the right operand to the left operand.

    ```javascript
    let message = "Hello";
    message += " World!"; // message is "Hello World!"
    console.log(message);
    ```

### 6. Conditional (Ternary) Operator

This operator is a shorthand for an `if...else` statement.

*   **Syntax:** `condition ? expression_if_true : expression_if_false`

    ```javascript
    let age = 20;
    let canVote = age >= 18 ? "Yes" : "No"; // canVote is "Yes"
    console.log(canVote);
    ```

### 7. Type Operators

These operators deal with the type of operands:

*   **`typeof`:** Returns a string indicating the type of a variable.

    ```javascript
    let x = 5;
    let y = "Hello";
    console.log(typeof x); // "number"
    console.log(typeof y); // "string"
    console.log(typeof true); // "boolean"
    console.log(typeof undefined); // "undefined"
    console.log(typeof null); // "object" (historical quirk)
    console.log(typeof {}); // "object"
    console.log(typeof []); // "object"
    ```

*   **`instanceof`:** Checks if an object is an instance of a particular class or constructor function.

    ```javascript
    class Car {}
    let myCar = new Car();
    console.log(myCar instanceof Car); // true

    let myArray = [];
    console.log(myArray instanceof Array); // true
    ```

## Operator Precedence

Operator precedence determines the order in which operators are evaluated in an expression. Operators with higher precedence are evaluated before operators with lower precedence. Use parentheses `()` to override the default precedence and explicitly control the order of operations.

For example:

```javascript
let result = 5 + 2 * 3; // result is 11 (multiplication is done before addition)
console.log(result);

result = (5 + 2) * 3; // result is 21 (parentheses force addition to be done first)
console.log(result);
```

## Conclusion

Understanding operators is fundamental to writing JavaScript code. By mastering these operators and their precedence, you'll be well on your way to creating powerful and dynamic web applications. Keep practicing and experimenting to solidify your knowledge!
