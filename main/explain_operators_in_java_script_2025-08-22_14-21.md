# JavaScript Operators: A Beginner's Guide

## What are Operators?

Operators are special symbols in JavaScript that perform operations on values. Think of them as verbs that instruct the JavaScript engine to manipulate data. The values that operators act upon are called operands.

## Types of Operators

JavaScript provides a rich set of operators for various purposes. Let's explore some of the most common categories:

### 1. Arithmetic Operators

These operators are used to perform mathematical calculations.

*   **Addition (+):** Adds two operands.

    ```javascript
    let x = 5;
    let y = 3;
    let sum = x + y; // sum will be 8
    console.log(sum);
    ```

*   **Subtraction (-):** Subtracts the second operand from the first.

    ```javascript
    let x = 5;
    let y = 3;
    let difference = x - y; // difference will be 2
    console.log(difference);
    ```

*   **Multiplication (*):** Multiplies two operands.

    ```javascript
    let x = 5;
    let y = 3;
    let product = x * y; // product will be 15
    console.log(product);
    ```

*   **Division (/):** Divides the first operand by the second.

    ```javascript
    let x = 15;
    let y = 3;
    let quotient = x / y; // quotient will be 5
    console.log(quotient);
    ```

*   **Modulus (%):** Returns the remainder of a division operation.

    ```javascript
    let x = 5;
    let y = 2;
    let remainder = x % y; // remainder will be 1
    console.log(remainder);
    ```

*   **Exponentiation (**):** Raises the first operand to the power of the second operand.

    ```javascript
    let x = 2;
    let y = 3;
    let result = x ** y; // result will be 8 (2 * 2 * 2)
    console.log(result);
    ```

*   **Increment (++):** Increases the value of a variable by 1. Can be used as a prefix (`++x`) or postfix (`x++`). The prefix version increments the value and returns the incremented value. The postfix version increments the value, but returns the original value before it was incremented.

    ```javascript
    let x = 5;
    x++; // x will be 6 (postfix)
    console.log(x);

    let y = 5;
    ++y; // y will be 6 (prefix)
    console.log(y);
    ```

*   **Decrement (--):** Decreases the value of a variable by 1. Similar to increment, it can be used as a prefix (`--x`) or postfix (`x--`) with similar behavior regarding the return value.

    ```javascript
    let x = 5;
    x--; // x will be 4 (postfix)
    console.log(x);

    let y = 5;
    --y; // y will be 4 (prefix)
    console.log(y);
    ```

### 2. Assignment Operators

These operators assign values to variables.

*   **Assignment (=):** Assigns the value on the right to the variable on the left.

    ```javascript
    let x = 10; // Assigns the value 10 to the variable x
    console.log(x);
    ```

*   **Addition Assignment (+=):** Adds the right operand to the left operand and assigns the result to the left operand.

    ```javascript
    let x = 5;
    x += 3; // Equivalent to x = x + 3; x will be 8
    console.log(x);
    ```

*   **Subtraction Assignment (-=):** Subtracts the right operand from the left operand and assigns the result to the left operand.

    ```javascript
    let x = 5;
    x -= 3; // Equivalent to x = x - 3; x will be 2
    console.log(x);
    ```

*   **Multiplication Assignment (\*=):** Multiplies the left operand by the right operand and assigns the result to the left operand.

    ```javascript
    let x = 5;
    x *= 3; // Equivalent to x = x * 3; x will be 15
    console.log(x);
    ```

*   **Division Assignment (/=):** Divides the left operand by the right operand and assigns the result to the left operand.

    ```javascript
    let x = 15;
    x /= 3; // Equivalent to x = x / 3; x will be 5
    console.log(x);
    ```

*   **Modulus Assignment (%=):** Calculates the modulus of the left operand divided by the right operand and assigns the result to the left operand.

    ```javascript
    let x = 5;
    x %= 2; // Equivalent to x = x % 2; x will be 1
    console.log(x);
    ```

*   **Exponentiation Assignment (\*\*=):** Raises the left operand to the power of the right operand and assigns the result to the left operand.

    ```javascript
    let x = 2;
    x **= 3; // Equivalent to x = x ** 3; x will be 8
    console.log(x);
    ```

### 3. Comparison Operators

These operators compare two operands and return a Boolean value (`true` or `false`).

*   **Equal to (==):** Checks if two operands are equal (performs type coercion, meaning it tries to convert the operands to the same type before comparing).

    ```javascript
    let x = 5;
    let y = "5";
    console.log(x == y); // Returns true (because "5" is coerced to 5)
    ```

*   **Not equal to (!=):** Checks if two operands are not equal (performs type coercion).

    ```javascript
    let x = 5;
    let y = "5";
    console.log(x != y); // Returns false (because "5" is coerced to 5)
    ```

*   **Strict equal to (===):** Checks if two operands are equal in value and type (no type coercion).

    ```javascript
    let x = 5;
    let y = "5";
    console.log(x === y); // Returns false (because they are of different types)
    ```

*   **Strict not equal to (!==):** Checks if two operands are not equal in value or type (no type coercion).

    ```javascript
    let x = 5;
    let y = "5";
    console.log(x !== y); // Returns true (because they are of different types)
    ```

*   **Greater than (>):** Checks if the left operand is greater than the right operand.

    ```javascript
    let x = 5;
    let y = 3;
    console.log(x > y); // Returns true
    ```

*   **Less than (<):** Checks if the left operand is less than the right operand.

    ```javascript
    let x = 5;
    let y = 3;
    console.log(x < y); // Returns false
    ```

*   **Greater than or equal to (>=):** Checks if the left operand is greater than or equal to the right operand.

    ```javascript
    let x = 5;
    let y = 5;
    console.log(x >= y); // Returns true
    ```

*   **Less than or equal to (<=):** Checks if the left operand is less than or equal to the right operand.

    ```javascript
    let x = 5;
    let y = 5;
    console.log(x <= y); // Returns true
    ```

### 4. Logical Operators

These operators are used to combine or modify Boolean expressions.

*   **Logical AND (&&):** Returns `true` if both operands are `true`.

    ```javascript
    let x = 5;
    let y = 3;
    console.log(x > 0 && y < 10); // Returns true (both conditions are true)
    ```

*   **Logical OR (||):** Returns `true` if at least one operand is `true`.

    ```javascript
    let x = 5;
    let y = 3;
    console.log(x < 0 || y < 10); // Returns true (y < 10 is true)
    ```

*   **Logical NOT (!):** Returns the opposite of the operand's truthiness. If the operand is `true`, it returns `false`, and vice versa.

    ```javascript
    let x = 5;
    console.log(!(x > 0)); // Returns false (because x > 0 is true, and !true is false)
    ```

### 5. String Operators

JavaScript also has operators that work specifically with strings.

*   **Concatenation (+):** Joins two strings together.

    ```javascript
    let firstName = "John";
    let lastName = "Doe";
    let fullName = firstName + " " + lastName; // fullName will be "John Doe"
    console.log(fullName);
    ```

*   **Concatenation Assignment (+=):** Appends a string to an existing string.

    ```javascript
    let message = "Hello";
    message += " world!"; // message will be "Hello world!"
    console.log(message);
    ```

### 6. Conditional (Ternary) Operator

This operator is a shorthand way of writing an `if...else` statement.

*   **(condition) ? (expression if true) : (expression if false)**

    ```javascript
    let age = 20;
    let canVote = (age >= 18) ? "Yes" : "No"; // canVote will be "Yes"
    console.log(canVote);
    ```

### 7. Type Operators

These operators deal with the type of operands.

*   **`typeof`:** Returns the type of a variable or expression as a string.

    ```javascript
    let x = 5;
    let y = "Hello";
    console.log(typeof x);   // Output: "number"
    console.log(typeof y);   // Output: "string"
    console.log(typeof null);  // Output: "object"  (This is a known JavaScript quirk)
    console.log(typeof undefined); // Output: "undefined"
    ```

*   **`instanceof`:** Checks if an object is an instance of a particular class or constructor function.

    ```javascript
    class Car {}
    let myCar = new Car();

    console.log(myCar instanceof Car); // Output: true

    let str = "Hello";
    console.log(str instanceof String); // Output: false (because str is a primitive string, not a String object)
    ```

## Operator Precedence

Operator precedence determines the order in which operators are evaluated in an expression. Operators with higher precedence are evaluated before operators with lower precedence. You can use parentheses `()` to override the default precedence.

For example:

```javascript
let result = 5 + 3 * 2; // Multiplication is performed before addition
console.log(result); // Output: 11

let result2 = (5 + 3) * 2; // Parentheses force addition to be performed first
console.log(result2); // Output: 16
```

Understanding operator precedence is crucial for writing code that behaves as expected. Refer to the official documentation for a complete precedence table.

## Conclusion

Operators are fundamental building blocks in JavaScript. By mastering these different types of operators, you'll be well on your way to writing more complex and powerful JavaScript code. Keep practicing and experimenting to solidify your understanding!