# CSS: Cascading Style Sheets Explained

## What Does CSS Stand For?

CSS stands for **Cascading Style Sheets**.

## Breaking Down the Name

Let's break down the meaning of each word:

*   **Cascading:** This refers to the order in which styles are applied. Styles defined later in the stylesheet, or closer to the element in the HTML, generally override earlier styles. This "cascade" allows for flexibility and control over your website's design.

*   **Style:** This refers to the visual presentation of a web page. This includes elements like colors, fonts, layout, and spacing.

*   **Sheets:** This refers to the practice of storing style rules in separate files (or within `<style>` tags in the HTML). This promotes reusable and maintainable code.

## Why Use CSS?

CSS allows you to separate the content (HTML) from the presentation (styling). This separation offers several benefits:

*   **Maintainability:** Design changes only need to be made in the CSS file, rather than in every HTML file.
*   **Consistency:** You can easily apply the same styles across multiple pages of your website, ensuring a unified look and feel.
*   **Accessibility:** Cleaner HTML code improves accessibility for screen readers and other assistive technologies.
*   **Bandwidth:** External CSS files are cached by the browser, reducing the amount of data that needs to be downloaded for each page and improving website loading times.

## Basic CSS Syntax

CSS rules are composed of selectors and declarations.

```css
selector {
  property: value;
}
```

*   **Selector:** Specifies the HTML element(s) you want to style (e.g., `p`, `h1`, `.my-class`, `#my-id`).
*   **Property:** The style attribute you want to change (e.g., `color`, `font-size`, `margin`).
*   **Value:** The value you want to assign to the property (e.g., `red`, `16px`, `10px`).

Here's an example:

```css
p {
  color: blue;
  font-size: 14px;
}
```

This CSS rule will make all paragraph text blue and set the font size to 14 pixels.

## Where to Include CSS

There are three main ways to include CSS in your HTML:

1.  **Inline CSS:** Styles are applied directly to HTML elements using the `style` attribute. Avoid this method for large projects due to maintainability issues.

    ```html
    <p style="color: green;">This is a paragraph with inline CSS.</p>
    ```

2.  **Internal CSS:** Styles are defined within a `<style>` tag inside the `<head>` section of your HTML document.

    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        h1 {
          color: purple;
        }
      </style>
    </head>
    <body>
      <h1>This is a heading with internal CSS.</h1>
    </body>
    </html>
    ```

3.  **External CSS:** Styles are defined in a separate `.css` file and linked to your HTML document using the `<link>` tag. This is the recommended approach for larger projects.

    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <h1>This is a heading with external CSS.</h1>
    </body>
    </html>
    ```

    (And in `style.css`:)

    ```css
    h1 {
      color: orange;
    }
    ```

## Understanding the Cascade

The "cascading" nature of CSS determines which styles are applied when multiple rules conflict. The general order of precedence is:

1.  **Inline styles** (highest priority)
2.  **Internal styles**
3.  **External styles** (lowest priority)

Within each of these categories, the specificity of the selector also plays a role; more specific selectors override less specific ones. Understanding the cascade is crucial for debugging and effectively controlling your website's appearance.