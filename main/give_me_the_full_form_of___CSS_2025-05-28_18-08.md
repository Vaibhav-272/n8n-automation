# CSS: Cascading Style Sheets

## What Does CSS Stand For?

CSS stands for **Cascading Style Sheets**.

## Understanding the Name

Let's break down what each word in "Cascading Style Sheets" means:

*   **Cascading:** This refers to how styles are applied to HTML elements. Styles cascade from various sources, such as browser defaults, external stylesheets, and inline styles. The order in which these styles are applied determines which style takes precedence, a process known as the cascade.

*   **Style:** This refers to the visual formatting of HTML elements, including:

    *   Colors (text, background)
    *   Fonts (size, family, weight)
    *   Layout (positioning, margins, padding)
    *   And much more!

*   **Sheets:** CSS rules are typically written in separate files called "stylesheets" (with the `.css` extension). This separation keeps your styles organized and makes your code easier to maintain. Styles can also be included directly within the HTML document using `<style>` tags or inline styles.

## Example

Here's a simple CSS example:

```css
body {
  background-color: lightblue;
  font-family: sans-serif;
}

h1 {
  color: navy;
  text-align: center;
}

p {
  font-size: 16px;
  line-height: 1.5;
}
```

In this example:

*   `body` is the selector, targeting the entire `<body>` of the HTML document.
*   `background-color` and `font-family` are properties that are being set.
*   `lightblue` and `sans-serif` are the values assigned to those properties.

## How to Include CSS in HTML

There are three main ways to include CSS in your HTML:

1.  **External Stylesheets:** This is the recommended approach for most projects.  Create a separate `.css` file and link it to your HTML document using the `<link>` tag within the `<head>` section:

    ```html
    <head>
      <link rel="stylesheet" href="styles.css">
    </head>
    ```

2.  **Internal Stylesheets:** Embed CSS directly within your HTML document using the `<style>` tag inside the `<head>` section:

    ```html
    <head>
      <style>
        p {
          color: green;
        }
      </style>
    </head>
    ```

3.  **Inline Styles:** Apply styles directly to individual HTML elements using the `style` attribute:

    ```html
    <p style="color: red;">This text is red.</p>
    ```

    While convenient for quick tests, inline styles are generally not recommended for larger projects because they can make code harder to maintain.

## Why is CSS Important?

CSS is crucial for web development because it allows you to:

*   **Control the visual presentation** of your website.
*   **Separate content from presentation**, resulting in cleaner, more maintainable code.
*   **Create a consistent look and feel** across your entire website.
*   **Adapt your website to different devices** (responsive design).