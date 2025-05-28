# CSS: Cascading Style Sheets Explained

## What Does CSS Stand For?

CSS stands for **Cascading Style Sheets**.

## Breaking Down the Name

Let's break down each part of the name to understand what CSS is all about:

*   **Cascading:** This refers to how styles are applied to HTML elements. Styles "cascade" down from different sources, and rules can override each other based on their *specificity* and *order*. This allows you to define styles in multiple places, with CSS determining which style to apply based on a defined set of rules.

*   **Style:** This refers to the visual appearance of HTML elements, including:

    *   Colors (text, background, borders)
    *   Fonts (family, size, weight)
    *   Layout (positioning, margins, padding)
    *   And much more!

*   **Sheets:** This refers to the files where you write your CSS code. These files typically have a `.css` extension. While you *can* embed styles directly within your HTML, using separate style sheets is generally considered best practice for organization and maintainability.

## A Simple Example

Here's a basic example of CSS in action:

```css
/* This is a CSS comment */

h1 {
  color: blue;
  text-align: center;
}

p {
  font-family: Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5;
}
```

In this example:

*   `h1` and `p` are *selectors* that target HTML heading and paragraph elements.
*   `color`, `text-align`, `font-family`, `font-size`, and `line-height` are *properties* that define the styles.
*   `blue`, `center`, `Arial, sans-serif`, `16px`, and `1.5` are the *values* assigned to those properties.

This CSS code would make all `<h1>` headings on your webpage blue and centered. All `<p>` paragraphs would use the Arial font (or a generic sans-serif font if Arial isn't available), have a font size of 16 pixels, and a line height of 1.5.

## Why Use CSS?

CSS is crucial for web development because it allows you to:

*   **Separate content from presentation:** Keep your HTML focused on the structure of your content, while CSS handles the visual styling.
*   **Maintain consistency:** Apply the same styles across multiple pages, ensuring a consistent look and feel.
*   **Improve accessibility:** Use CSS to enhance the accessibility of your website for users with disabilities.
*   **Reduce code duplication:** Avoid repeating style definitions throughout your HTML.
*   **Create responsive websites:** Adapt your website's layout to different screen sizes and devices.