# CSS: Cascading Style Sheets

## What Does CSS Stand For?

CSS stands for **Cascading Style Sheets**.

## Understanding the Name

Let's break down the name to better understand what CSS does:

*   **Cascading:** This refers to how styles are applied. When multiple style rules target the same HTML element, CSS uses a "cascade" to determine which style takes precedence. This cascade considers factors like specificity and the order in which styles are declared, creating a hierarchy where some styles have more weight than others.

*   **Style:** This refers to the visual presentation of a webpage. CSS controls elements like colors, fonts, layout, and responsiveness, allowing you to design the look and feel of your website.

*   **Sheets:** These are files (typically with a `.css` extension) that contain the style rules. While you can embed styles directly within your HTML, using separate style sheets is generally preferred for better organization and maintainability.

## How CSS Works

CSS works by applying rules to HTML elements. A CSS rule consists of two main parts:

*   **Selector:** This identifies the HTML element(s) you want to style (e.g., `p`, `h1`, `.my-class`, `#my-id`).

*   **Declaration Block:** This contains one or more declarations. Each declaration consists of a property (e.g., `color`, `font-size`, `margin`) and a value (e.g., `red`, `16px`, `10px`).

Here's an example:

```css
p {
  color: blue;
  font-size: 14px;
}
```

In this example:

*   `p` is the selector, targeting all paragraph elements.
*   `color: blue;` is a declaration that sets the text color to blue.
*   `font-size: 14px;` is a declaration that sets the font size to 14 pixels.

## Ways to Include CSS

You can include CSS in three ways:

1.  **Inline Styles:** Directly within HTML elements using the `style` attribute. This approach is best reserved for very specific, isolated cases.

    ```html
    <p style="color: green;">This is a green paragraph.</p>
    ```

2.  **Internal Styles:** Within the `<head>` section of your HTML document, enclosed in `<style>` tags.

    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <title>My Page</title>
      <style>
        p {
          color: purple;
        }
      </style>
    </head>
    <body>
      <p>This is a purple paragraph.</p>
    </body>
    </html>
    ```

3.  **External Stylesheets:** In separate `.css` files, linked to your HTML document using the `<link>` tag in the `<head>`. This is the recommended method for most projects.

    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <title>My Page</title>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <p>This paragraph's style is defined in styles.css.</p>
    </body>
    </html>
    ```

    And in `styles.css`:

    ```css
    p {
      color: orange;
    }
    ```

## Benefits of Using CSS

*   **Separation of Concerns:** CSS separates the presentation (style) of your website from the content (HTML). This separation results in cleaner, more maintainable, and better-organized code.

*   **Reusability:** You can reuse the same CSS rules across multiple pages, ensuring a consistent look and feel throughout your website.

*   **Maintainability:**  You can modify your website's style in one place (the CSS file) instead of editing every HTML page individually.

*   **Accessibility:** CSS enables you to create accessible websites by controlling the visual presentation without altering the underlying HTML structure.

*   **Responsiveness:** CSS allows you to create websites that adapt to different screen sizes and devices, providing an optimal user experience across platforms.