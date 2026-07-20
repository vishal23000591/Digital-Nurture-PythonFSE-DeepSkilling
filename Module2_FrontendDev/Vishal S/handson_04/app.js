import { courses } from "./data.js";

async function fetchUser(id) {
    try {
        const response = await fetch(
            "https://jsonplaceholder.typicode.com/users/" + id
        );

        const user = await response.json();

        console.log(user.name);

    } catch (error) {
        console.log("Error:", error);
    }
}

fetchUser(1);

async function fetchAllCourses() {
    await new Promise(resolve => setTimeout(resolve, 1000));

    return courses;
}


const courseGrid = document.querySelector(".course-grid");

const courseStatus = document.querySelector("#course-status");

function renderCourses(courseList) {
    courseGrid.innerHTML = "";

    courseList.forEach(course => {
        const article = document.createElement("article");

        article.className = "course-card";

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p>${course.code}</p>
            <p>${course.credits} Credits</p>
            <p>Grade: ${course.grade}</p>
        `;

        courseGrid.appendChild(article);
    });
}

async function loadCourses() {
    courseStatus.textContent = "Loading courses...";

    const courseData = await fetchAllCourses();

    renderCourses(courseData);

    courseStatus.textContent = "";
}


loadCourses();

async function fetchTwoUsers() {
    try {
        const responses = await Promise.all([
            fetch("https://jsonplaceholder.typicode.com/users/1"),
            fetch("https://jsonplaceholder.typicode.com/users/2")
        ]);

        const users = await Promise.all(
            responses.map(response => response.json())
        );

        console.log(users[0].name);
        console.log(users[1].name);

    } catch (error) {
        console.log("Error:", error);
    }
}

fetchTwoUsers();

async function apiFetch(url) {
    const response = await axios.get(url);

    return response.data;
}

async function testApi() {
    try {
        const data = await apiFetch(
            "https://jsonplaceholder.typicode.com/posts"
        );
        console.log(data);
    } catch (error) {
        console.error("apiFetch error:", error);
    }
}

testApi();

const notificationList = document.querySelector(".notification-list");

const notificationLoading = document.querySelector(
    "#notification-loading"
);

const notificationError = document.querySelector("#notification-error");

const retryButton = document.querySelector("#retry-button");
axios.interceptors.request.use(config => {
    console.log("API call started: " + config.url);

    return config;
});


function renderNotifications(posts) {
    notificationList.innerHTML = "";

    posts.forEach(post => {
        const article = document.createElement("article");

        article.className = "notification-card";

        article.innerHTML = `
            <h3>${post.title}</h3>
            <p>${post.body}</p>
        `;

        notificationList.appendChild(article);
    });
}

async function loadNotifications(url = "https://jsonplaceholder.typicode.com/nonexistent") {
    notificationLoading.classList.remove("hidden");
    notificationError.textContent = "";
    retryButton.classList.add("hidden");

    try {
        const posts = await apiFetch(url);

        renderNotifications(posts);

    } catch (error) {
        notificationError.textContent = "Unable to load notifications. Please try again.";
        retryButton.classList.remove("hidden");
    }
    finally {
        notificationLoading.classList.add("hidden");
    }
}

loadNotifications();

retryButton.addEventListener("click", () => {
    loadNotifications(
        "https://jsonplaceholder.typicode.com/posts"
    );
});

async function fetchUserPosts() {
    try {
        const response = await axios.get(
            "https://jsonplaceholder.typicode.com/posts",
            {
                params: {
                    userId: 1
                }
            }
        );

        console.log(response.data);

    } catch (error) {
        console.log("Error:", error);
    }
}

fetchUserPosts();

/*
FETCH vs AXIOS

1. JSON Parsing
   Fetch: Requires response.json() to parse JSON.
   Axios: Automatically parses JSON and provides response.data.

2. Error Handling
   Fetch: Does not throw an error for HTTP errors like 404 or 500.
          We must check response.ok manually.
   Axios: Automatically rejects the Promise for non-2xx responses.

3. Query Parameters
   Fetch: Query parameters are usually added manually to the URL.
   Axios: Provides a params object to handle query parameters.
*/