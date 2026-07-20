import { courses } from "./data.js";

console.log(courses);

for (const course of courses) {
    const { name, credits } = course;
    console.log(name);
    console.log(credits);
}

const result = courses.map(course => {
    return `${course.code} - ${course.name} (${course.credits} credits)`
});

console.log(result);

const count = courses.filter(course => {
    return course.credits >= 4;
});

console.log(count);

const total_credits = courses.reduce((total, course) => {
    return total + course.credits;
}, 0);

console.log(total_credits);

courses.forEach(course => {
    const { name, credits } = course;
    console.log(`${name} has ${credits} credits`);
});




const courseGrid = document.querySelector(".course-grid");

console.log(courseGrid);

const sort = document.querySelector("#sort");
console.log(sort);

const input = document.querySelector("#search-courses");
console.log(input);



function renderedCourses(courseList) {
    courseGrid.innerHTML = "";

    courseList.forEach(course => {
        const article = document.createElement("article");
        article.className = "course-card";
        article.dataset.id = course.id;
        article.innerHTML = `
        <h2>${course.name}</h2>
        <p>${course.code}</p>
        <p>${course.credits}</p>
    `;

        courseGrid.appendChild(article);
    });


}
renderedCourses(courses);

courseGrid.addEventListener("click", (event) => {
    const card = event.target.closest(".course-card");

    if (!card) return;
    const courseID = Number(card.dataset.id);
    const selectedCourse = courses.find(course => course.id === courseID);
    alert(`
        Course Name : ${selectedCourse.name}
        Course Code : ${selectedCourse.code}
        Course Credits : ${selectedCourse.credits}
        Course Grade : ${selectedCourse.grade}
        `);

})


const totalcredits = document.querySelector("#total-credits");

const credits = courses.reduce((total, course) => {
    return total + course.credits;
}, 0);

totalcredits.textContent = `Total Credits enrolled are ${credits}`;




sort.addEventListener("click", () => {
    const sortcourses = courses.sort((a, b) => {
        return b.credits - a.credits;

    })



    renderedCourses(sortcourses);

});

input.addEventListener("input", () => {
    const searchinput = input.value.toLowerCase();
    const filteredcourses = courses.filter(course => {
        return course.name.toLowerCase().includes(searchinput);
    });
    renderedCourses(filteredcourses);

}); 