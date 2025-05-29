# CSS: Cascading Style Sheets

## What Does CSS Stand For?

CSS stands for **Cascading Style Sheets**.

## Understanding the Name

Let's break down each part of the name:

*   **Cascading:** This refers to how styles are applied. When multiple styles conflict, CSS uses a set of rules to determine which style takes precedence. This "cascade" allows for complex styling in a manageable way. We'll explore this in more detail later.

*   **Style:** This is straightforward. CSS focuses on styling HTML elements, including colors, fonts, and layouts.

*   **Sheets:** CSS rules are typically stored in separate files with a `.css` extension. These files are linked to your HTML document, separating content (HTML) from presentation (CSS).

## What Does CSS Do?

CSS controls the visual presentation of HTML elements on a webpage. It defines:

*   **Colors:** Text color, background color, border color, etc.

    ```css
    body {
      background-color: #f0f0f0; /* Light gray background */
      color: #333; /* Dark gray text */
    }
    ```

*   **Fonts:** Font family, font size, font weight, etc.

    ```css
    h1 {
      font-family: Arial, sans-serif;
      font-size: 3em;
      font-weight: bold;
    }
    ```

*   **Layout:** Positioning elements, creating grids, and managing spacing.

    ```css
    .container {
      width: 80%;
      margin: 0 auto; /* Centers the container */
    }
    ```

*   **Responsiveness:** Adapting the layout and styling to different screen sizes and devices.

    ```css
    @media (max-width: 768px) {
      .container {
        width: 100%; /* Full width on smaller screens */
      }
    }
    ```

*   **Animations & Transitions:** Adding visual effects to elements.

    ```css
    button {
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: lightblue;
    }
    ```

## Why Use CSS?

*   **Separation of Concerns:** Keeps HTML focused on content and CSS focused on presentation.
*   **Maintainability:** Simplifies website updates by modifying CSS files instead of individual HTML pages.
*   **Consistency:** Ensures a uniform look and feel across your website.
*   **Responsiveness:** Enables your website to adapt to various devices and screen sizes.
*   **Accessibility:** Proper CSS usage can improve website accessibility for users with disabilities.

## Where Can You Include CSS?

There are three primary ways to apply CSS to your HTML:

1.  **Inline Styles:** Directly within HTML elements using the `style` attribute. Avoid this for large projects.

    ```html
    <p style="color: blue; font-size: 16px;">This is a paragraph with inline styles.</p>
    ```

2.  **Internal Styles:** Within the `<style>` tag in the `<head>` section of your HTML document. Suitable for small, page-specific styles.

    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <title>My Page</title>
      <style>
        p {
          color: blue;
          font-size: 16px;
        }
      </style>
    </head>
    <body>
      <p>This is a paragraph with internal styles.</p>
    </body>
    </html>
    ```

3.  **External Styles:** In a separate `.css` file, linked to your HTML using the `<link>` tag. This is generally the preferred method.

    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <title>My Page</title>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <p>This is a paragraph with external styles.</p>
    </body>
    </html>
    ```

    **styles.css:**

    ```css
    p {
      color: blue;
      font-size: 16px;
    }
    ```

External stylesheets are recommended for their reusability and maintainability.