# CSS: Cascading Style Sheets Explained

## What Does CSS Stand For?

CSS stands for **Cascading Style Sheets**.

## Understanding the Name

Let's break down each part of the name to understand what CSS is all about:

*   **Cascading:** This refers to how styles are applied to HTML elements. Styles can originate from various sources (e.g., external CSS files, inline styles within HTML, browser defaults). CSS uses a set of rules to determine which styles take precedence. Think of it like a waterfall  styles "cascade" down, and the most specific style wins.

*   **Style:** This is where the visual presentation comes in! CSS allows you to control the look and feel of your website, including aspects like:
    *   Colors
    *   Fonts
    *   Layout
    *   Spacing

*   **Sheets:** CSS rules are typically stored in separate files called "style sheets" (with the `.css` extension). This promotes clean and organized HTML. You link these style sheets to your HTML documents.

## CSS Example

Here's a basic CSS example:

```css
body {
  background-color: lightblue;
}

h1 {
  color: navy;
  text-align: center;
}

p {
  font-family: verdana;
  font-size: 16px;
}
```

In this example:

*   `body` is a *selector* that targets the `<body>` element in your HTML.
*   `background-color: lightblue;` is a *declaration* that sets the background color of the body to light blue.
*   `h1` is a selector that targets all `<h1>` heading elements.
*   `color: navy;` and `text-align: center;` are declarations that set the text color to navy and center the text within the `<h1>` element.
*   `p` is a selector that targets all `<p>` paragraph elements.
*   `font-family: verdana;` and `font-size: 16px;` are declarations that set the font family to Verdana and the font size to 16 pixels.

## Linking CSS to HTML

You link CSS style sheets to HTML documents using the `<link>` tag, typically within the `<head>` section:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Webpage</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Welcome to my website!</h1>
  <p>This is a paragraph of text.</p>
</body>
</html>
```

In this example, the `style.css` file (containing the CSS code from the previous example) will be applied to the HTML document. The `rel="stylesheet"` attribute tells the browser that the linked file is a style sheet.

## Benefits of Using CSS

Using CSS provides several key benefits:

*   **Separation of Concerns:** Styling is kept separate from HTML content, making code easier to read, maintain, and update.
*   **Consistency:** Apply the same styles across multiple pages, ensuring a consistent look and feel for your entire website.
*   **Accessibility:** Helps create accessible websites by allowing you to control how content is presented to users with different needs.
*   **Efficiency:** Reduces code duplication, leading to smaller file sizes and faster loading times.
*   **Flexibility:** Provides powerful tools for creating visually appealing and responsive websites that adapt to different screen sizes and devices.