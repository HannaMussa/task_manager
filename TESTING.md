## Automated vs Manual Testing

## Code Validation

### HTML Validation

<details>
<summary> Click here to view HTML Validation </summary>
HTML was validated using [The W3C Markup Validation Service](https://validator.w3.org/).
</details>

### CSS Validation

<details>
<summary> Click here to view the CSS Validation </summary>
CSS was validated using [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/).
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

## WAVE Web Accessibility Evaluation Tool

<details>
<summary>Click here to view the WAVE Feedback </summary>
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
<summary>Click here to view the testing for existing features</summary>
</details>

### Authentication Functionality Tests

<details>
<summary>Click here to view the Authentication Functionality Tests</summary>

| Test Name         | Steps                           | Expected Result       | Screenshot                                          |
| ----------------- | ------------------------------- | --------------------- | --------------------------------------------------- |
| Signup page loads | Visit /signup/                  | Form displays         | ![Signup Page](tasks/static/documentation/--)       |
| Successful signup | Enter valid username + password | Redirect to task list | ![Successful Signup](tasks/static/documentation/--) |
| Login page loads  | Visit /login/                   | Form displays         | ![Login Page](tasks/static/documentation/--)        |
| Successful login  | Enter valid credentials         | Redirect to tasks     | ![Successful Login](tasks/static/documentation/--)  |
| Logout            | Click "Logout"                  | Redirect to login     | ![Logout](tasks/static/documentation/--)            |

</details>

### CRUD Functionality Tests

<details>
<summary>Click here to view the CRUD Functionality Tests</summary>

| Feature          | Steps                        | Expected Outcome           | Screenshots                                           |
| ---------------- | ---------------------------- | -------------------------- | ----------------------------------------------------- |
| Create Task      | Fill form, then click Submit | Task appears in list       | [//](tasks/static/documentation/create-task.png)      |
| Read Tasks       | Visit homepage               | Displays user's tasks only | [//](tasks/static/documentation/read-tasks.png)       |
| Edit Task        | Click Edit, then click Save  | Updated task shown         | [//](tasks/static/documentation/edit-task.png)        |
| Delete Task      | Click Delete                 | Task removed               | [//](tasks/static/documentation/delete-task.png)      |
| Toggle Completed | Click Toggle                 | Completed state changes    | [//](tasks/static/documentation/toggle-completed.png) |

</details>

## Automatic Testing

## Bugs

<details>
<summary>Click here to view the Bugs </summary>
</details>

## Unfixed Bugs

## pending:

- HTML Validation
- CSS Validation
- WAVE
- Testing Existing Features
- Authentication & CRUD testing (Add pics)
- bugs

bugs:
css doesn't load, order of css
logout page doesn't work
navbar doesn't work- try adding collapse, update to latest query

