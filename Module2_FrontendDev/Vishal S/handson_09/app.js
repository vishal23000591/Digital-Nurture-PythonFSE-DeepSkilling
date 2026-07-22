// CanIUse check:
// Feature: CSS Grid (https://caniuse.com/css-grid)
// Support: 97.5% global support. Fully supported in all major browsers (Chrome 57+, Firefox 52+, Safari 10.1+, Edge 16+).

const courses = [
  { id: 1, name: "Python Programming", code: "CS101", credits: 4, grade: "A" },
  { id: 2, name: "Java Programming", code: "CS102", credits: 3, grade: "B+" },
  { id: 3, name: "React Development", code: "CS201", credits: 4, grade: "A+" },
  { id: 4, name: "Database Systems", code: "CS202", credits: 3, grade: "A" },
  { id: 5, name: "Data Structures", code: "CS203", credits: 4, grade: "A" }
];

let coursesList = [...courses];

const grid = document.querySelector('.course-grid');
const searchInput = document.querySelector('#search-courses');
const statusCount = document.querySelector('#status-count');
const sortBtn = document.querySelector('#sort-credits');
const totalCreditsEl = document.querySelector('#total-credits');

function renderCourses(list) {
  grid.innerHTML = '';
  const fragment = document.createDocumentFragment();

  list.forEach(course => {
    const article = document.createElement('article');
    article.className = 'course-card';
    article.tabIndex = 0;
    article.setAttribute('data-id', course.id);
    article.innerHTML = `
      <h3>${course.name}</h3>
      <p>Code: ${course.code}</p>
      <p>Credits: ${course.credits}</p>
      <p>Grade: ${course.grade}</p>
    `;
    fragment.appendChild(article);
  });

  grid.appendChild(fragment);

  const total = list.reduce((sum, c) => sum + c.credits, 0);
  totalCreditsEl.textContent = `Total Credits: ${total}`;
  statusCount.textContent = `${list.length} courses found.`;
}

searchInput.addEventListener('input', (e) => {
  const query = e.target.value.toLowerCase();
  const filtered = coursesList.filter(c => c.name.toLowerCase().includes(query));
  renderCourses(filtered);
});

sortBtn.addEventListener('click', () => {
  coursesList.sort((a, b) => b.credits - a.credits);
  renderCourses(coursesList);
});

grid.addEventListener('click', (e) => {
  const card = e.target.closest('.course-card');
  if (card) {
    const id = parseInt(card.getAttribute('data-id'), 10);
    const course = coursesList.find(c => c.id === id);
    if (course) {
      alert(`Course: ${course.name}\nCode: ${course.code}\nCredits: ${course.credits}\nGrade: ${course.grade}`);
    }
  }
});

grid.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    const card = e.target.closest('.course-card');
    if (card) {
      const id = parseInt(card.getAttribute('data-id'), 10);
      const course = coursesList.find(c => c.id === id);
      if (course) {
        alert(`Course: ${course.name}\nCode: ${course.code}\nCredits: ${course.credits}\nGrade: ${course.grade}`);
      }
    }
  }
});

document.addEventListener('DOMContentLoaded', () => {
  renderCourses(coursesList);
});
