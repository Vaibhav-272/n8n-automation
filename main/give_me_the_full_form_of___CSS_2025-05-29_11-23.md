# CSS: Cascading Style Sheets

## What Does CSS Stand For?

CSS stands for **Cascading Style Sheets**.

## Breaking Down the Name

Let's break down each part of the acronym:

*   **Cascading:** This refers to the order in which styles are applied. If multiple styles conflict, CSS uses rules to determine which style takes precedence. This is the "cascade" in action. For example, inline styles (defined directly within an HTML element) generally override styles defined in an external stylesheet.

    ```html
    <p style="color:red;">This text will be red.</p>

    <style>
      p {
        color: blue; /* This will be overridden */
      }
    </style>
    ```

*   **Style:** CSS defines the style of HTML elements. This includes properties like:

    *   `color`: Text color
    *   `font-size`: Text size
    *   `font-family`: Font type (e.g., Arial, Times New Roman)
    *   `background-color`: Background color
    *   `margin`: Space around an element
    *   `padding`: Space inside an element

    ```css
    body {
      font-family: sans-serif;
      background-color: #f0f0f0;
    }

    h1 {
      color: navy;
      text-align: center;
    }
    ```

*   **Sheets:** CSS rules are typically stored in separate `.css` files, linked to HTML documents. This separates content (HTML) and presentation (CSS), improving maintainability. You can also embed CSS directly within an HTML document using the `<style>` tag, but external stylesheets are generally preferred for larger projects.

    ```html
    <head>
      <link rel="stylesheet" href="styles.css">
    </head>
    ```

## Why Use CSS?

CSS is essential for web development because it provides:

*   **Separation of Concerns:**  Keeps HTML structure and visual styling separate.
*   **Maintainability:** Makes it easier to update and modify the look and feel of a website.
*   **Consistency:**  Ensures a consistent look across multiple pages.
*   **Accessibility:**  Helps create accessible websites by controlling content presentation for users with disabilities.
*   **Responsive Design:** Allows websites to adapt to different screen sizes and devices.

## Example

Here's a simple example of how CSS is used:

**HTML (index.html):**

```html
<!DOCTYPE html>
<html>
<head>
  <title>My First CSS Example</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Welcome to My Website!</h1>
  <p>This is a paragraph of text.</p>
</body>
</html>
```

**CSS (style.css):**

```css
body {
  font-family: Arial, sans-serif;
  background-color: #e6f7ff;
}

h1 {
  color: #003366;
  text-align: center;
}

p {
  font-size: 16px;
  line-height: 1.5;
}
```

This example demonstrates how CSS styles the text, background color, and layout of a webpage. The HTML file links to the CSS file containing the styling rules. Open `index.html` in your browser to see the styled webpage.