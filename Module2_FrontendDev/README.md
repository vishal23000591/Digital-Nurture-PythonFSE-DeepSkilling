# Module 2: Frontend Development – Digital Nurture 5.0

This directory contains implementation files, styles, and scripts for **Module 2: Frontend Development**, part of the **Digital Nurture 5.0 – Python Full Stack Engineer Track**.

It covers the fundamentals of building responsive, interactive, and API-driven user interfaces for the **Student Portal Web Application** using modern frontend technologies (HTML5, CSS3, ES6+ JavaScript, React, Angular, Vue, and Web Accessibility standards).

---

# Repository Structure

```
Module2_FrontendDev/
├── README.md                  # Dedicated Frontend Development README (This file)
└── Vishal S/
    ├── handson_01/            # Web Page Structure & HTML Semantics
    │   ├── index.html
    │   └── styles.css
    ├── handson_02/            # Styling and Responsive Layouts (Flexbox & Grid)
    │   ├── index.html
    │   └── styles.css
    ├── handson_03/            # DOM Manipulation and Event Handling
    │   ├── index.html
    │   ├── styles.css
    │   ├── data.js
    │   └── app.js
    ├── handson_04/            # Asynchronous JavaScript & API Integration
    │   ├── index.html
    │   ├── style.css
    │   ├── data.js
    │   └── app.js
    ├── handson_05/            # Introduction to React & Component Creation
    │   └── Student-Portal/
    │       ├── public/
    │       └── src/
    ├── handson_06/            # Single Page Application with React Router
    │   └── student-portal-react/
    │       ├── public/
    │       └── src/
    ├── handson_07/            # Building Student Portal Dashboard in Angular
    │   └── student-portal-angular/
    │       ├── public/
    │       └── src/
    ├── handson_08/            # Building Student Portal Dashboard in Vue
    │   └── student-portal-vue/
    │       ├── public/
    │       └── src/
    ├── handson_09/            # Web Accessibility Improvements (Aria-live, high contrast)
    │   ├── index.html
    │   ├── styles.css
    │   ├── data.js
    │   └── app.js
    └── handson_10/            # Advanced React State & Optimization (Hooks, Context API)
        └── student-portal-react/
            ├── public/
            └── src/
```

---

# Technologies & Tools Used

### Core Web Technologies
- **HTML5**: Semantics, form inputs, dynamic structural templates, ARIA labels.
- **CSS3**: CSS Custom Properties, Flexbox, CSS Grid, media queries, keyframe animations.
- **Modern JavaScript (ES6+)**: ES Modules (`import`/`export`), Promises, async/await, Array methods (`filter`, `map`, `sort`), DOM Manipulation.

### Frameworks & Libraries
- **React**: Component-driven architecture, Hooks (`useState`, `useEffect`, `useContext`), Context API, React Router.
- **Angular**: Modules, component hierarchy, TypeScript-driven architecture.
- **Vue**: Single File Components (SFCs), Vue Router, Pinia store management.
- **Axios**: Promise-based HTTP client for API request orchestration.

---

# Detailed Hands-On Breakdown

## Hands-On 1: Web Page Structure & HTML Semantics
- **Objective**: Establish the foundation of the Student Portal layout.
- **Key Implementations**:
  - Structured standard layout with semantic tags: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, and `<footer>`.
  - Created a Hero section and Course listings showing basic courses.

## Hands-On 2: Styling and Responsive Layouts (Flexbox & Grid)
- **Objective**: Design a visually rich dashboard and make it fully responsive.
- **Key Implementations**:
  - **Flexbox Navigation**: Developed a clean navigation bar and aligned stats items.
  - **CSS Grid Layout**: Displayed courses in a grid (`course-grid`) using standard responsive CSS.
  - **Responsiveness**: Leveraged Media Queries to ensure design adapts beautifully to mobile and desktop screens.

## Hands-On 3: DOM Manipulation and Event Handling
- **Objective**: Introduce user interaction through client-side dynamic search and sorting.
- **Key Implementations**:
  - Implemented dynamic rendering of courses based on mock data.
  - Added a search input field (`#search-courses`) filtering courses in real-time.
  - Added sorting capabilities (`#sort` button) to sort courses by credit weight.

## Hands-On 4: Asynchronous JavaScript & API Integration
- **Objective**: Connect the client interface to a backend REST API using asynchronous requests.
- **Key Implementations**:
  - Integrated **Axios** to make network requests to retrieve dynamic course listings and notifications.
  - Implemented load state management including displaying a loading spinner during requests.
  - Implemented comprehensive error handling and recovery mechanisms (such as a Retry button).

## Hands-On 5: Introduction to React & Component Creation
- **Objective**: Migrate the static layouts into a component-driven architecture using React.
- **Key Implementations**:
  - Built modular React components like `Header`, `Footer`, `Navbar`, and `CourseCard`.
  - Set up standard project structure with modularized imports.

## Hands-On 6: Single Page Application with React Router
- **Objective**: Construct a multi-page routing structure for the Student Portal.
- **Key Implementations**:
  - Integrated **React Router** for declarative client-side routing.
  - Implemented page components: **Dashboard**, **Courses**, and **Profile**.
  - Enabled smooth transition between views without reloading the page.

## Hands-On 7: Building Student Portal Dashboard in Angular
- **Objective**: Implement the Student Portal UI using the Angular framework.
- **Key Implementations**:
  - Developed custom Angular components for the main dashboard interface.
  - Leveraged Angular directives and TypeScript bindings for reliable data flow.

## Hands-On 8: Building Student Portal Dashboard in Vue
- **Objective**: Re-create the Student Portal application using Vue.
- **Key Implementations**:
  - Built reactive Single File Components (SFCs).
  - Used Vue Router for view management and Pinia for reactive state management.

## Hands-On 9: Web Accessibility Improvements
- **Objective**: Improve the accessibility score of the portal to WCAG compliance standards.
- **Key Implementations**:
  - Added appropriate **ARIA roles** and `aria-live="polite"` status notifications.
  - Implemented keyboard navigation support and focus outline indicators.
  - Adjusted background/foreground colors to meet contrast ratio recommendations.

## Hands-On 10: Advanced React State & Optimization
- **Objective**: Optimize application performance and global state management.
- **Key Implementations**:
  - Used the **Context API** (`useContext`) for cross-component theme and authorization state.
  - Optimized rendering performance using Hooks like `useMemo` and `useCallback`.

---

# How to Run & Verify

### Standard HTML/CSS/JS (Hands-on 1-4, 9)
1. Navigate to the specific hands-on directory:
   ```bash
   cd "Module2_FrontendDev/Vishal S/handson_03"
   ```
2. Serve the directory:
   ```bash
   python3 -m http.server 8000
   ```
3. Open `http://localhost:8000` in the browser.

### Framework Apps (React, Angular, Vue - Hands-on 5, 6, 7, 8, 10)
1. Navigate to the project root containing `package.json`:
   ```bash
   cd "Module2_FrontendDev/Vishal S/handson_06/student-portal-react"
   ```
2. Install dependencies and start the development server:
   ```bash
   npm install
   npm run dev
   ```

---

# Student Info

- **Name:** Vishal S
- **Course:** Digital Nurture 5.0 – Python Full Stack Engineer Track
