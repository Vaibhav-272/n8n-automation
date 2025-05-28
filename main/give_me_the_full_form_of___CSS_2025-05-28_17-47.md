# CSS: Cascading Style Sheets Explained

## What Does CSS Stand For?

CSS stands for **Cascading Style Sheets**.

## Understanding the Name

Let's break down each word in "Cascading Style Sheets":

*   **Cascading:** This refers to how styles are applied based on a hierarchy. Styles from various sources (e.g., external stylesheets, inline styles, browser defaults) "cascade" together. Precedence is determined by specific rules, which we'll explore later.

*   **Style:** This refers to the visual presentation of a webpage, including aspects like colors, fonts, layout, and spacing. CSS is responsible for defining these elements.

*   **Sheets:** CSS rules are typically organized into separate files called "stylesheets" (with a `.css` extension). This promotes separation of concerns by keeping the HTML structure distinct from the visual styling.

## What Does CSS Do?

CSS is a language that describes the look and formatting of a document written in HTML (or XML). It controls:

*   **Colors:** Defines text color, background colors, and border colors.

    ```css
    body {
      background-color: #f0f0f0; /* Light gray background */
      color: #333; /* Dark gray text */
    }
    ```

*   **Fonts:** Specifies font families, sizes, and styles.

    ```css
    h1 {
      font-family: Arial, sans-serif;
      font-size: 3em;
      font-weight: bold;
    }
    ```

*   **Layout:** Positions elements on the page, creates grids, and manages spacing.

    ```css
    .container {
      width: 80%;
      margin: 0 auto; /* Centers the container */
      padding: 20px;
    }
    ```

*   **Responsiveness:** Adapts the layout to different screen sizes (desktops, tablets, and phones).

    ```css
    @media (max-width: 768px) {
      .container {
        width: 100%;
        padding: 10px;
      }
    }
    ```

*   **Animations and Transitions:** Adds visual effects and interactivity.

    ```css
    button {
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: lightblue;
    }
    ```

## Why is CSS Important?

*   **Separation of Concerns:** It keeps HTML focused on structure, while CSS handles presentation.
*   **Maintainability:** Updating a website's look and feel is easier by modifying CSS files instead of HTML.
*   **Consistency:** It ensures a consistent visual experience across all pages of a website.
*   **Accessibility:** It facilitates the creation of accessible websites that can adapt to different user needs.
*   **Responsiveness:** It enables websites to adapt to various devices and screen sizes.