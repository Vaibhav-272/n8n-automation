# CSS: Cascading Style Sheets Explained

## What Does CSS Stand For?

CSS stands for **Cascading Style Sheets**.

## Breaking Down the Name

Let's break down the full name to understand its purpose:

*   **Cascading:** This refers to how CSS rules are applied. Styles "cascade" from different sources (e.g., browser default styles, external stylesheets, and inline styles) and are applied in a specific order of priority. When conflicting styles arise, the cascade determines which style takes precedence.

*   **Style:** This is straightforward. CSS is about styling your HTML content, controlling the look and feel of your web pages, including colors, fonts, and layouts.

*   **Sheets:** Styles are defined in separate documents called stylesheets, typically with a `.css` extension. This separation of concerns keeps your HTML clean and your styling organized.

## Why Use CSS?

Instead of embedding styling directly within HTML tags (common in the early days of the web), CSS provides a structured and efficient way to manage a website's presentation.

Consider this example:

**Without CSS (Inline Styles - Not Recommended):**

```html
<h1 style="color: blue; font-size: 24px;">This is a Heading</h1>
<p style="color: green; font-size: 16px;">This is a paragraph.</p>
```

**With CSS (External Stylesheet - Recommended):**

First, in your `style.css` file:

```css
h1 {
  color: blue;
  font-size: 24px;
}

p {
  color: green;
  font-size: 16px;
}
```

Then, in your HTML file:

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>This is a Heading</h1>
  <p>This is a paragraph.</p>
</body>
</html>
```

The CSS approach is cleaner, more maintainable, and allows you to apply the same styles to multiple elements across your entire website.

## Basic CSS Syntax

A CSS rule consists of:

*   **Selector:**  Targets the HTML element(s) you want to style (e.g., `h1`, `p`, `.my-class`, `#my-id`).
*   **Property:**  The style attribute you want to modify (e.g., `color`, `font-size`, `margin`).
*   **Value:**  The value you want to assign to the property (e.g., `blue`, `24px`, `10px`).

```css
selector {
  property: value;
}
```

Example:

```css
body {
  background-color: #f0f0f0;
  font-family: sans-serif;
}
```

This CSS code sets the background color of the entire `body` of your webpage to light gray and the font to a sans-serif font.

## How to Include CSS in Your HTML

There are three main ways to include CSS in your HTML:

1.  **External Stylesheet:** (Recommended) Link a separate `.css` file using the `<link>` tag within the `<head>` section of your HTML. (See the example above)

2.  **Internal Stylesheet:** Embed CSS rules directly within the `<style>` tag inside the `<head>` section of your HTML.

    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        h1 {
          color: red;
        }
      </style>
    </head>
    <body>
      <h1>This is a Heading</h1>
    </body>
    </html>
    ```

3.  **Inline Styles:** Apply styles directly to individual HTML elements using the `style` attribute (as shown in the first example; generally discouraged for maintainability).

## Conclusion

CSS, or Cascading Style Sheets, is essential for web development. Understanding its components and how it works is a great first step towards creating beautiful and well-structured websites. Happy styling!