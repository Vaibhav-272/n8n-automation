avaScript Operators: A Beginner's Guide
hat are Operators?
erators are special symbols in JavaScript that perform operations on values. Think of them as verbs that instruct the JavaScript engine to manipulate data (called operands) and produce a result.
ypes of Operators
vaScript provides a variety of operators. Let's explore some of the most common categories:
Arithmetic Operators
ese operators perform mathematical calculations:
ddition): Adds two operands.
ubtraction): Subtracts one operand from another.
ultiplication): Multiplies two operands.
ivision): Divides one operand by another.
odulus): Returns the remainder of a division.
xponentiation): Raises a number to a power.
ncrement): Increases the value of a variable by 1.
ecrement): Decreases the value of a variable by 1.
avascript
t x = 10;
t y = 5;
nsole.log(x + y);   // Output: 15
nsole.log(x - y);   // Output: 5
nsole.log(x * y);   // Output: 50
nsole.log(x / y);   // Output: 2
nsole.log(x % y);   // Output: 0
nsole.log(x ** y);  // Output: 100000
nsole.log(x);       // Output: 11
nsole.log(y);       // Output: 4
Assignment Operators
ese operators assign values to variables:
ssignment): Assigns a value to a variable.
ddition Assignment): Adds a value to a variable and assigns the result.
ubtraction Assignment): Subtracts a value from a variable and assigns the result.
ultiplication Assignment): Multiplies a variable by a value and assigns the result.
ivision Assignment): Divides a variable by a value and assigns the result.
odulus Assignment): Calculates the modulus of a variable by a value and assigns the result.
xponentiation Assignment): Raises a variable to the power of a value and assigns the result.
avascript
t a = 5;
Equivalent to a = a + 3
nsole.log(a);  // Output: 8
Equivalent to a = a - 2
nsole.log(a);  // Output: 6
Equivalent to a = a * 4
nsole.log(a);  // Output: 24
Equivalent to a = a / 3
nsole.log(a);  // Output: 8
Equivalent to a = a % 5
nsole.log(a);  // Output: 3
Equivalent to a = a ** 2
nsole.log(a);  // Output: 9
Comparison Operators
ese operators compare two operands and return a Boolean value (`true` or `false`):
qual to): Checks if two operands are equal (type coercion may occur).
trict Equal to): Checks if two operands are equal in value and type.
ot equal to): Checks if two operands are not equal (type coercion may occur).
trict Not equal to): Checks if two operands are not equal in value or type.
reater than): Checks if the left operand is greater than the right operand.
ess than): Checks if the left operand is less than the right operand.
reater than or equal to): Checks if the left operand is greater than or equal to the right operand.
ess than or equal to): Checks if the left operand is less than or equal to the right operand.
avascript
t num1 = 10;
t num2 = "10";
nsole.log(num1 == num2);   // Output: true (because of type coercion)
nsole.log(num1 === num2);  // Output: false (different types)
nsole.log(num1 != num2);   // Output: false (because of type coercion)
nsole.log(num1 !== num2);  // Output: true (different types)
nsole.log(num1 > 5);    // Output: true
nsole.log(num1 < 12);   // Output: true
nsole.log(num1 >= 10);   // Output: true
nsole.log(num1 <= 8);    // Output: false
Logical Operators
ese operators combine or modify Boolean expressions:
ogical AND): Returns `true` if both operands are `true`.
ogical OR): Returns `true` if at least one operand is `true`.
ogical NOT): Returns the opposite Boolean value of the operand.
avascript
t sunny = true;
t warm = true;
nsole.log(sunny && warm);  // Output: true (both are true)
nsole.log(sunny || false); // Output: true (at least one is true)
nsole.log(!sunny);       // Output: false (negation of true)
String Operators
e `+` operator can also be used to concatenate strings:
avascript
t firstName = "John";
t lastName = "Doe";
t fullName = firstName + " " + lastName;
nsole.log(fullName);  // Output: John Doe
Conditional (Ternary) Operator
is is a shorthand way to write an `if...else` statement:
ondition ? expressionIfTrue : expressionIfFalse`
avascript
t age = 20;
t canVote = age >= 18 ? "Yes" : "No";
nsole.log(canVote);  // Output: Yes
perator Precedence
erators have a specific order of precedence, which determines the order in which they are evaluated. If you're unsure, use parentheses to explicitly define the order.
r example:
avascript
t result = 5 + 3 * 2; // Multiplication is performed before addition
nsole.log(result); // Output: 11
t result2 = (5 + 3) * 2; // Parentheses change the order
nsole.log(result2); // Output: 16
onclusion
derstanding operators is crucial for writing effective JavaScript code. Experiment with these operators and explore others to become a proficient JavaScript developer!