# CSS: Cascading Style Sheets Explained

## What Does CSS Stand For?

CSS stands for **Cascading Style Sheets**.

## Breaking Down the Name

Let's examine each word in "Cascading Style Sheets" to understand its meaning:

*   **Cascading:** This refers to how styles are applied to HTML elements. Styles can originate from various sources, including:
    *   Browser default styles
    *   User-defined styles
    *   Website-defined styles

    When conflicts arise (multiple styles targeting the same element), CSS uses a set of rules to determine which style takes precedence. This prioritization process is the "cascade."

*   **Style:** This refers to the visual presentation of elements on a webpage. Styles control aspects like:
    *   Colors (text, background, borders)
    *   Fonts (family, size, weight)
    *   Layout (positioning, margins, padding)
    *   And much more!

*   **Sheets:** This refers to the fact that styles are typically defined in separate documents (CSS files) or within the HTML document itself using `<style>` tags. Separating style from content (HTML) promotes maintainability and reusability.

## A Simple CSS Example

Here's a basic example of CSS code that changes the color of a heading:

```css
h1 {
  color: blue;
}
```

In this example:

*   `h1` is the **selector**. It targets all `<h1>` elements in the HTML.
*   `color: blue;` is the **declaration**. It sets the `color` property of the selected element to blue.

## How CSS Works With HTML

CSS styles HTML elements. You can link a CSS file to an HTML document using the `<link>` tag within the `<head>` section:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Webpage</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>This is a Heading</h1>
  <p>This is a paragraph.</p>
</body>
</html>
```

In this example, the `<link>` tag connects the `styles.css` file to the HTML. Any styles defined in `styles.css` will then be applied to the corresponding HTML elements.

## Inline Styles

You can also add CSS directly to HTML elements using the `style` attribute. However, this is generally discouraged for larger projects because it can make the code harder to maintain.

```html
<p style="color: green;">This paragraph has inline styles.</p>
```

## Why Use CSS?

CSS offers several key benefits:

*   **Separation of Concerns:** Keeps styling separate from content, improving readability and maintainability.
*   **Reusability:** Styles can be applied to multiple pages, ensuring a consistent look and feel.
*   **Accessibility:** CSS enables the creation of visually appealing and accessible websites.
*   **Flexibility:** Provides precise control over the appearance of web pages.
*   **Efficiency:** Reduces the amount of code needed to style a website.