# Task Manager

## Project Rationale

- This project uses a simple, clear and user friendly web application To-Do List built with Django and Python. It allows users to customise their own tasks by creating, editing deleting, and marking tasks as completed. Each user has their own task list and can manage tasks efficiently. 

## UX 

### Target Audience

- The Task Manager App is intended for anyone who wants to manage personal tasks and stay organized.Anyone who is overstressed, has mind clutter or has many tasks can use this app to become more organsied, clear mind clutter and manage tasks efficiently. 

### How to operate the Task Manager

## User Stories

## Development Cycle 

## Wireframes

### Mobile Wireframes

### Tablet Wireframes

### Desktop Wireframes


## Features

### Existing Features

#### User Signup
- Users can create an account using a simple signup form. Each user is able to create, edit, delete and update their own tasks.

#### User Login
- Users with an account can securely log in using Django’s built-in authentication system and are taken straight to their personal task list.

#### User Logout
- Users can log out at any time and are redirected back to the login page.

#### Create Tasks
- Users can add new tasks using a form that includes fields for the task title, description, and optionally a due date. Each task is linked to the user who created it.

#### Due Date Feature
- Users can assign a due date and time when creating or editing a task. This helps them organise tasks more effectively by knowing when something is expected to be completed.

#### View Tasks
- All tasks belonging to the logged-in user are displayed clearly on the main task page so they can keep track of what needs to be done.

#### Edit Tasks
- Users can edit a task’s title, description, due date, and completion status. This allows changes without needing to create new tasks.

#### Delete Tasks
- Users can permanently remove tasks from their list with one click, keeping their task list tidy.

#### Responsive Layout
- The interface uses Bootstrap, ensuring the layout adjusts smoothly across mobile, tablet, and desktop screens.

#### Toggle Task Completion
- Users can quickly switch any task between “Completed” and “Not Completed” directly from the task list using a simple button.

#### Task Buttons
- Clear action buttons are included for “Add Task”, “Edit”, “Delete”, and “Toggle Completion”, making the interface easy to use and navigate.

#### Navigation Bar
- A Bootstrap-styled navigation bar appears at the top of each page. It includes links to the task list, login, logout and a welcome message when the user is logged in.

### Future Features

## Technologies Used

This section highlights the tools, languages, and frameworks used in the development of the project:

- **HTML** – For structuring the content of the web pages.
- **CSS** – For styling the appearance of the site.
- **JavaScript** – For Bootstrap Navbar interactivity.
- **Bootstrap 4** – For responsive layout and the Navbar.
- **Python 3** – Programming language used to write the backend logic.
- **pip** – Python package manager used to install dependencies.
- **venv** – Python virtual environment used to isolate project dependencies.
- **Django 5** – Web framework used for server-side logic, user authentication, and CRUD operations.
- **SQLite** – Database used to store tasks and user information.
- **Visual Studio Code** – Code editor used to build and manage the project.
- **Git** – Version control tool used to track changes in the project.
- **GitHub** – Hosting platform used to store the project repository.
- **Google Chrome DevTools** – Used for debugging, inspecting elements, and testing CSS.

## Code Attribution

Some parts of this project were inspired by or adapted from external sources:

- **Django Official Documentation** – https://docs.djangoproject.com/en/5.2/  
  Helped understand Django forms, models, and authentication system.

- **YouTube: Django To-Do List Tutorial** – https://www.youtube.com/watch?v=6Jf8-PbHoLM  
  Provided step-by-step guidance on setting up CRUD functionality with Django, demonstrating how to create and display tasks.

- **MDN Django Tutorials** – https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django  
  Explained Django concepts, useful for understanding form handling and template rendering.

- **W3Schools Django Guide** – https://www.w3schools.com/django/  
  Used as a quick reference for syntax and template examples.

- **YouTube: Bootstrap Navbar Implementation** – https://www.youtube.com/watch?v=H_cWdD-aXCQ&t=295s  
  Showed how to implement a responsive navbar, which was adapted for the project’s layout.

- **YouTube: Django Authentication** – https://www.youtube.com/watch?v=kDAnnEhb4_I  
  Explained login, logout, and signup flows, helping integrate user authentication.

All other code was written by Hanna Mussa.

## Content Credits

## Database
- Task model description
- Relationships 

## Testing

To view the testing carried out, please refer to the [TESTING.md](TESTING.md) file.

## Local Deployment
1.	Clone the repository by typing in the terminal:
`git clone https://github.com/HannaMussa/task_manager.git
cd task_manager`
2.	Create a virtual environment and activate it:
`python -m venv venv
venv\Scripts\activate` (Windows)
`source venv/bin/activate` (Mac/Linux)
3.	Install the dependencies:
`pip install -r requirements.txt`
4.	Apply the database migrations:
`python manage.py migrate`
5.	Run the server:
`python manage.py runserver`
6.	Open your browser and click the link displayed in the terminal to access the app.



# pending: 
- User Stories
- Development Cycle 
- Wireframes
- Credits
- Database
- How to operate the Task Manager
- Testing ( Manual testing of CRUD and auth, Any bugs found/fixed, html, cssvalidator.user stories (testing)testing features)
