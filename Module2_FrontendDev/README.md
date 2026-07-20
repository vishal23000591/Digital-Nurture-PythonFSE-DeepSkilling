# Module 2: Frontend Development – Digital Nurture 5.0

This directory contains implementation files, styles, and scripts for **Module 2: Frontend Development**, part of the **Digital Nurture 5.0 – Python Full Stack Engineer Track**.

It covers the fundamentals of building a responsive, interactive, and API-driven user interface for the **Student Portal Web Application** using HTML5, CSS3, ES6+ JavaScript, DOM Manipulation, and Asynchronous programming.

---

# Repository Structure

```
Module2_FrontendDev/
├── README.md                  # Dedicated Frontend Development README (This file)
└── Vishal S/
    ├── handson_01/
    │   ├── index.html         # Basic HTML Layout & Structure
    │   └── styles.css         # Basic Typography & Element Styles
    ├── handson_02/
    │   ├── index.html         # Portal Dashboard with Stats
    │   └── styles.css         # Grid & Flexbox Layouts, Responsive Design
    ├── handson_03/
    │   ├── index.html         # Dynamic Course Explorer
    │   ├── styles.css         # Element Styling
    │   ├── data.js            # Mock Course Data
    │   └── app.js             # DOM Manipulation, Search, & Sorting Logic
    └── handson_04/
        ├── index.html         # API-Integrated Student Portal
        ├── style.css          # Layout and loading states (spinner)
        ├── data.js            # Offline Fallback/Mock Course Data
        └── app.js             # Async/Await API Fetch, Axios Integration, & Error Handling
```

---

# Technologies & Tools Used

### Core Web Technologies
- **HTML5**: Semantics, form inputs, dynamic structural templates.
- **CSS3**: CSS Custom Properties, Flexbox, CSS Grid, media queries, transitions.
- **Modern JavaScript (ES6+)**: ES Modules (`import`/`export`), Array methods (`filter`, `map`, `sort`), DOM Querying and Manipulation, Event Listeners.

### Libraries & External Tools
- **Axios**: Promise-based HTTP client for API request orchestration.
- **GitHub**: Source code version control.

---

# Detailed Hands-On Breakdown

## Hands-On 1: Web Page Structure & HTML Semantics
- **Objective**: Establish the foundation of the Student Portal layout.
- **Key Implementations**:
  - Structured standard layout with semantic tags: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, and `<footer>`.
  - Created a Hero section and Course listings showing basic courses (Python Programming, Web Development, Java Programming).
  - Wired basic CSS stylesheets for element spacing.

## Hands-On 2: Styling and Responsive Layouts (Flexbox & Grid)
- **Objective**: Design a visually rich dashboard and make it fully responsive.
- **Key Implementations**:
  - **Flexbox Navigation**: Developed a clean navigation bar and aligned stats items.
  - **CSS Grid Layout**: Displayed courses in a grid (`course-grid`) using standard responsive CSS.
  - **Stats Dashboard**: Introduced a statistics panel displaying Courses Enrolled, GPA, and Current Semester.
  - **Responsiveness**: Leveraged Media Queries to ensure design adapts beautifully to mobile and desktop screens.

## Hands-On 3: DOM Manipulation and Event Handling
- **Objective**: Introduce user interaction through client-side dynamic search and sorting.
- **Key Implementations**:
  - Implemented dynamic rendering of courses based on mock data in `data.js`.
  - Added a search input field (`#search-courses`) filtering courses in real-time as the user types.
  - Added sorting capabilities (`#sort` button) to sort courses by credit weight.
  - Tracked and printed aggregate properties like total credits.

## Hands-On 4: Asynchronous JavaScript & API Integration
- **Objective**: Connect the client interface to a backend REST API using asynchronous requests.
- **Key Implementations**:
  - Integrated **Axios** to make network requests to retrieve dynamic course listings and notifications.
  - Implemented load state management including displaying a loading spinner (`#notification-loading`) during requests.
  - Implemented comprehensive error handling and recovery mechanisms (such as a Retry button if the API request fails).
  - Programmed smooth user notifications updates.

---

# How to Run & Verify

### Viewing Pages Locally
Since the modules are built with standard browser-native HTML, CSS, and ES Modules:
1. Open the directory of the hands-on you want to run:
   ```bash
   cd "Module2_FrontendDev/Vishal S/handson_01"
   # Or any other hands-on
   ```
2. For scripts running ES modules (like Hands-on 3 and Hands-on 4), open the directory using a local web server (e.g., Live Server in VS Code, or Python's built-in http server):
   ```bash
   python3 -m http.server 8000
   ```
3. Open your browser and navigate to `http://localhost:8000`.

---

# Student Info

- **Name:** Vishal S
- **Course:** Digital Nurture 5.0 – Python Full Stack Engineer Track
