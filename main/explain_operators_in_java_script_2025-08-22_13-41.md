# JavaScript Operators: A Beginner's Guide

## What are Operators?

Operators are special symbols in JavaScript that perform operations on values, known as operands. Think of them as instructions that tell the JavaScript engine how to manipulate data. For example, in the expression `2 + 3`, the `+` symbol is the operator, and `2` and `3` are the operands.

## Types of Operators

JavaScript provides a variety of operators. Here's a look at some of the most common categories:

### 1. Arithmetic Operators

These operators perform mathematical calculations:

*   **Addition (`+`):** Adds two operands.

    ```javascript
    let sum = 5 + 3; // sum is 8
    console.log(sum);
    ```

*   **Subtraction (`-`):** Subtracts the second operand from the first.

    ```javascript
    let difference = 10 - 4; // difference is 6
    console.log(difference);
    ```

*   **Multiplication (`*`):** Multiplies two operands.

    ```javascript
    let product = 6 * 7; // product is 42
    console.log(product);
    ```

*   **Division (`/`):** Divides the first operand by the second.

    ```javascript
    let quotient = 20 / 5; // quotient is 4
    console.log(quotient);
    ```

*   **Modulus (`%`):** Returns the remainder of a division operation.

    ```javascript
    let remainder = 15 % 4; // remainder is 3 (because 15 divided by 4 is 3 with a remainder of 3)
    console.log(remainder);
    ```

*   **Increment (`++`):** Increases the value of a variable by 1. Can be used as a prefix or postfix.

    ```javascript
    let x = 5;
    x++; // Postfix increment: x is now 6
    console.log(x);

    let y = 3;
    ++y; // Prefix increment: y is now 4
    console.log(y);
    ```

*   **Decrement (`--`):** Decreases the value of a variable by 1. Similar to increment, it has prefix and postfix versions.

    ```javascript
    let a = 8;
    a--; // Postfix decrement: a is now 7
    console.log(a);

    let b = 12;
    --b; // Prefix decrement: b is now 11
    console.log(b);
    ```

### 2. Assignment Operators

These operators assign values to variables.

*   **Assignment (`=`):** Assigns the value on the right to the variable on the left.

    ```javascript
    let age = 30; // Assigns the value 30 to the variable age
    console.log(age);
    ```

*   **Addition Assignment (`+=`):** Adds the right operand to the left operand and assigns the result to the left operand.

    ```javascript
    let score = 10;
    score += 5; // Equivalent to score = score + 5; score is now 15
    console.log(score);
    ```

*   **Subtraction Assignment (`-=`):** Subtracts the right operand from the left operand and assigns the result to the left operand.

    ```javascript
    let quantity = 25;
    quantity -= 10; // Equivalent to quantity = quantity - 10; quantity is now 15
    console.log(quantity);
    ```

*   **Multiplication Assignment (`*=`):** Multiplies the left operand by the right operand and assigns the result to the left operand.

    ```javascript
    let price = 8;
    price *= 2; // Equivalent to price = price * 2; price is now 16
    console.log(price);
    ```

*   **Division Assignment (`/=`):** Divides the left operand by the right operand and assigns the result to the left operand.

    ```javascript
    let total = 100;
    total /= 4; // Equivalent to total = total / 4; total is now 25
    console.log(total);
    ```

*   **Modulus Assignment (`%=`):** Calculates the modulus of the left operand by the right operand and assigns the result to the left operand.

    ```javascript
    let counter = 23;
    counter %= 5; // Equivalent to counter = counter % 5; counter is now 3
    console.log(counter);
    ```

### 3. Comparison Operators

These operators compare two operands and return a Boolean value (`true` or `false`).

*   **Equal to (`==`):** Checks if two operands are equal in value (may perform type conversion).

    ```javascript
    console.log(5 == "5"); // true (type conversion happens - string "5" is converted to number 5)
    ```

*   **Not equal to (`!=`):** Checks if two operands are not equal in value (may perform type conversion).

    ```javascript
    console.log(10 != "10"); // false (type conversion happens - string "10" is converted to number 10)
    ```

*   **Strict equal to (`===`):** Checks if two operands are equal in both value and type (no type conversion).

    ```javascript
    console.log(5 === "5"); // false (because 5 is a number and "5" is a string)
    ```

*   **Strict not equal to (`!==`):** Checks if two operands are not equal in either value or type (no type conversion).

    ```javascript
    console.log(10 !== "10"); // true (because 10 is a number and "10" is a string)
    ```

*   **Greater than (`>`):** Checks if the left operand is greater than the right operand.

    ```javascript
    console.log(12 > 8); // true
    ```

*   **Less than (`<`):** Checks if the left operand is less than the right operand.

    ```javascript
    console.log(3 < 7); // true
    ```

*   **Greater than or equal to (`>=`):** Checks if the left operand is greater than or equal to the right operand.

    ```javascript
    console.log(9 >= 9); // true
    ```

*   **Less than or equal to (`<=`):** Checks if the left operand is less than or equal to the right operand.

    ```javascript
    console.log(4 <= 6); // true
    ```

### 4. Logical Operators

These operators are used to combine or modify Boolean expressions.

*   **Logical AND (`&&`):** Returns `true` if both operands are `true`. Otherwise, it returns `false`.

    ```javascript
    let sunny = true;
    let warm = true;
    console.log(sunny && warm); // true (because both sunny and warm are true)

    let raining = true;
    let cold = false;
    console.log(raining && cold); // false (because cold is false)
    ```

*   **Logical OR (`||`):** Returns `true` if at least one of the operands is `true`. Returns `false` only if both operands are `false`.

    ```javascript
    let weekend = true;
    let vacation = false;
    console.log(weekend || vacation); // true (because weekend is true)

    let busy = false;
    let sick = false;
    console.log(busy || sick); // false (because both busy and sick are false)
    ```

*   **Logical NOT (`!`):** Reverses the Boolean value of an operand. If the operand is `true`, it returns `false`, and vice versa.

    ```javascript
    let isLoggedIn = false;
    console.log(!isLoggedIn); // true (because isLoggedIn is false, !isLoggedIn reverses it to true)

    let hasPermission = true;
    console.log(!hasPermission); // false (because hasPermission is true, !hasPermission reverses it to false)
    ```

### 5. String Operators

JavaScript also provides operators specifically for working with strings.

*   **Concatenation (`+`):** Joins two strings together.

    ```javascript
    let firstName = "John";
    let lastName = "Doe";
    let fullName = firstName + " " + lastName; // fullName is "John Doe"
    console.log(fullName);
    ```

*   **Concatenation Assignment (`+=`):** Appends a string to an existing string.

    ```javascript
    let message = "Hello";
    message += " world!"; // message is now "Hello world!"
    console.log(message);
    ```

### 6. Conditional (Ternary) Operator

This operator is the only JavaScript operator that takes three operands: a condition followed by a question mark (`?`), an expression to execute if the condition is truthy, followed by a colon (`:`) and finally the expression to execute if the condition is falsy.  It provides a concise way to write simple `if...else` statements.

```javascript
let age = 20;
let canVote = (age >= 18) ? "Yes" : "No"; // canVote is "Yes" because age is greater than or equal to 18
console.log(canVote);

let isMember = false;
let discount = isMember ? 0.10 : 0;
console.log(discount);
```

## Operator Precedence

Operator precedence determines the order in which operators are evaluated in an expression. For instance, multiplication and division take precedence over addition and subtraction. Use parentheses `()` to explicitly control the order of operations and make your code more readable.

```javascript
let result = 2 + 3 * 4; // result is 14 (3 * 4 is evaluated first, then 2 is added)
console.log(result);

let result2 = (2 + 3) * 4; // result2 is 20 (2 + 3 is evaluated first because of the parentheses, then the result is multiplied by 4)
console.log(result2);
```

Understanding operator precedence is essential for writing correct and predictable JavaScript code. Refer to the official JavaScript documentation for a comprehensive list of operator precedence rules.