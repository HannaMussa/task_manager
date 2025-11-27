## Code Validation

### HTML Validation

<details>
<summary> Click here to view HTML Validation </summary><br>

HTML was validated using [The W3C Markup Validation Service](https://validator.w3.org/).<br>

![HTML validator](tasks/static/documentation/html.png)

</details>

### CSS Validation

<details>
<summary> Click here to view the CSS Validation </summary> <br>

CSS was validated using [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/).
<br>

HTML was validated using [The W3C Markup Validation Service](https://validator.w3.org/).<br>

![HTML validator](tasks/static/documentation/css.png)

 </details>

## Browser Compatibility

<details>
<summary>Click here to view the Browser Compatibility </summary>

<br> The app has been tested across several popular browsers, including Google Chrome, Mozilla Firefox, Opera, and Brave. It was fully compatible with all browsers tested.

| Browser | Screenshot                                            |
| ------- | ----------------------------------------------------- |
| Chrome  | ![screenshot](tasks/static/documentation/chrome.png)  |
| Firefox | ![screenshot](tasks/static/documentation/firefox.png) |
| Opera   | ![screenshot](tasks/static/documentation/opera.png)   |
| Brave   | ![screenshot](tasks/static/documentation/brave.png)   |

</details>

## Responsiveness

<details>
<summary>Click here to view the responsiveness</summary>

<br> The app has been tested on the following devices and was responsive across the devices tested.

| Browser | Screenshot                                           |
| ------- | ---------------------------------------------------- |
| Mobile  | ![screenshot](tasks/static/documentation/mobile.png) |
| Tablet  | ![screenshot](tasks/static/documentation/tablet.png) |
| Laptop  | ![screenshot](tasks/static/documentation/laptop.png) |

</details>

## Lighthouse Audit

<details>
<summary>Click here to view the Lighthouse Audit </summary>

Chrome Lighthouse evaluates web pages for performance, accessibility and SEO- the audit showed positive results for both desktop and mobile.

| Lighthouse | Screenshot                                                |
| ---------- | --------------------------------------------------------- |
| Mobile     | ![screenshot](tasks/static/documentation/lighthousem.png) |
| Desktop    | ![screenshot](tasks/static/documentation/lighthoused.png) |

</details>

## User Story Testing

<details>
<summary>Click here to view the User Story Testing</summary>

| User Story                                         | Expected Result                                                       | Screenshot                                                 |
| -------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------- |
| First-time user can create, view, and manage tasks | Task is created, visible in the list, and editable                    | ![Task Management](tasks/static/documentation/list.png)    |
| Assign due dates to tasks                          | Task displays correct due date                                        | ![Due Date](tasks/static/documentation/date.png)           |
| Secure logout of account                           | User is redirected to login page, session ends                        | ![Logout](tasks/static/documentation/logout.png)           |
| Mobile responsiveness                              | Navbar collapses correctly; tasks visible and usable on small screens | ![Mobile](tasks/static/documentation/responsive.png)       |
| Delete tasks no longer needed                      | Task is removed from the task list                                    | ![Delete Task](tasks/static/documentation/delete.png)      |
| Mark tasks as complete                             | Task status changes to "Completed"                                    | ![Complete Task](tasks/static/documentation/completed.png) |
| Data security of tasks                             | Tasks cannot be accessed without login                                | ![Data Security](tasks/static/documentation/logout.png)    |

</details>

## Testing Existing Features

<details>
<summary>Click here to view the Tests for Existing Features</summary>

| **Feature**                | **Test Description**                                                          | **Expected Result**                                                   | **Screenshot**                                 |
| -------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------- |
| **User Signup**            | Test if a new user can sign up successfully.                                  | New user is can access task page.                                     | ![](tasks/static/documentation/signup.png)     |
| **User Login**             | Test if the user can log in with correct credentials.                         | User is logged in and redirected to their task list.                  | ![](tasks/static/documentation/login.png)      |
| **User Logout**            | Test if the user can log out.                                                 | User is logged out and redirected to the login page.                  | ![](tasks/static/documentation/logout.png)     |
| **Create Tasks**           | Test if a user can create a new task.                                         | Task appears in the task list.                                        | ![](tasks/static/documentation/list.png)       |
| **Due Date Feature**       | Test if a user can assign a due date to a task.                               | Task displays the correct due date.                                   | ![](tasks/static/documentation/date.png)       |
| **View Tasks**             | Test if all tasks are displayed for the logged-in user.                       | All tasks created by the logged-in user are shown on the main page.   | ![](tasks/static/documentation/list1.png)      |
| **Edit Tasks**             | Test if a user can edit task details.                                         | User is able to edit task details.                                    | ![](tasks/static/documentation/edit.png)       |
| **Delete Tasks**           | Test if a user can delete a task.                                             | Task is removed from the task list permanently.                       | ![](tasks/static/documentation/delete.png)     |
| **Toggle Task Completion** | Test if a user can mark a task as completed.                                  | Task is marked as completed (checkbox is checked).                    | ![](tasks/static/documentation/completed.png)  |
| **Responsive Layout**      | Test if the layout works on different screen sizes (mobile, tablet, desktop). | Navbar collapses on smaller screens, task list is properly displayed. | ![](tasks/static/documentation/responsive.png) |
| **Navigation Bar**         | Test if the navbar links (My Tasks, Login, Logout) work as expected.          | Links lead to the correct pages (task list, login, logout).           | All links lead to the correct pages.           |

</details>

## Authentication Functionality Tests

<details>
<summary>Click here to view the Authentication Functionality Tests</summary>

| Test Name         | Steps                           | Expected Result       | Screenshot                                                 |
| ----------------- | ------------------------------- | --------------------- | ---------------------------------------------------------- |
| Signup page loads | Signup/                         | Form displays         | ![Signup Page](tasks/static/documentation/signup.png)      |
| Successful signup | Enter valid username + password | Redirect to task list | ![Successful Signup](tasks/static/documentation/login.png) |
| Login page loads  | Visit /login/                   | Form displays         | ![Login Page](tasks/static/documentation/logout.png)       |
| Successful login  | Enter valid credentials         | Redirect to tasks     | ![Successful Login](tasks/static/documentation/login.png)  |
| Logout            | Click "Logout"                  | Redirect to login     | ![Logout](tasks/static/documentation/logout.png)           |

</details>

## CRUD Functionality Tests

<details>
<summary>Click here to view the CRUD Functionality Tests</summary>

| Feature          | Steps                        | Expected Outcome           | Screenshots                                              |
| ---------------- | ---------------------------- | -------------------------- | -------------------------------------------------------- |
| Create Task      | Fill form, then click Submit | Task appears in list       | ![Signup Page](tasks/static/documentation/list.png)      |
| Read Tasks       | Visit homepage               | Displays user's tasks only | ![Signup Page](tasks/static/documentation/list1.png)     |
| Edit Task        | Click Edit, then click Save  | Updated task shown         | ![Signup Page](tasks/static/documentation/edit.png)      |
| Delete Task      | Click Delete                 | Task removed               | ![Signup Page](tasks/static/documentation/delete.png)    |
| Toggle Completed | Click Toggle                 | Completed state changes    | ![Signup Page](tasks/static/documentation/completed.png) |

</details>

## Bugs

<details>
<summary>Click here to view the Bugs </summary>
</details>

## Unfixed Bugs
-  There are no unfixed bugs accoridng to my understanding.

## pending:
- add comments into work
- Bugs testting

- bugs:
  css doesn't load, order of css:css doesn't load, order of css was issue, i put bootstarp link below css so that was overriding, i had to put css below bootstrap to allow it to load


  logout page doesn't work: 
  the redirect urls werent configuered right after login it wasnt taking me to the tasks page, so i chnaged  login_redirect_url and logout_redirect_url in settings.py and that sorted it

  navbar doesn't work- try adding collapse, update to latest query
navbar doesn't work- try adding collapse, update to latest query, i used the wrong link of jqery i used the slim version so wasnt allowing me to use the features of collapse bar, i used the updated link without slim and the burger menu worked

css not wokring after deployemnt:
after deploying, none of my css was loading cos static files werent being served correctly  i had to installed whitenoise anad add to middleware, and ran python manage.py collectstatic again to fix it

i tried deploying to render, it wasnt working cos i never had Gunicorn, so i had to download that to allow it to work

page not loading cos  i forgot to add {% load static %} at the top of the template so i add {% load static %} to the template and the page loaded 

static folder wrong location i accidentally put the css in the wrong folder static/css/ instead of static/css/ si moved the files into the correct static/css/ and wokried

bootstrap was overriding my custom css and vise versa so i had to use dev tools make chnages from there removed the conflicting css rule and add new css, to see the issue and then updated into my actual css file

