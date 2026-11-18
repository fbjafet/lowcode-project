# Contact Form Website

A simple Flask contact form application with server-side validation. The
form is available at `/contact`, checks that the required fields are
completed, validates the email address, and displays a confirmation page
after a successful submission.

> **Note:** This project does not save submissions or send emails. It
> only validates the form and displays a success message.

## Features

-   Contact form served at `GET /contact`.
-   Form submission handled by `POST /contact`.
-   Required fields: name, email address, and message.
-   Server-side validation for empty fields and email format.
-   Clear validation messages displayed on the form.
-   Successful submissions redirect to a confirmation page showing
    **"Thanks for your message"**.
-   No database or other data storage is used.
-   Automated tests for the main form behaviours.

## Technologies

-   Python 3
-   Flask
-   HTML
-   CSS
-   pytest

## Project structure

``` text
contact_form_site/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── contact.html
│   └── success.html
├── static/
│   └── styles.css
└── tests/
    └── test_contact.py
```

## Getting started

### 1. Clone the repository

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your GitHub details:

``` bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 2. Create and activate a virtual environment

**Windows (Git Bash):**

``` bash
python -m venv venv
source venv/Scripts/activate
```

**macOS / Linux:**

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

If you are setting up the project without the requirements file, install
Flask and pytest:

``` bash
pip install Flask pytest
```

### 4. Run the application

``` bash
python app.py
```

Open this address in your browser:

``` text
http://127.0.0.1:5000/contact
```

Stop the development server with `Ctrl + C` in the terminal.

## How the application works

1.  A visitor opens `/contact` and the application displays the contact
    form.
2.  The visitor enters their name, email address, and message.
3.  The browser sends the form fields to the server using `POST`.
4.  Flask checks the submitted values on the server:
    -   The name must not be empty.
    -   The email address must have a valid basic email format.
    -   The message must not be empty.
5.  If validation fails, the form is displayed again with a visible
    error message.
6.  If validation succeeds, the visitor is redirected to the success
    page.

Server-side validation is important because browser-side checks alone
can be bypassed. The server therefore checks the submitted values before
accepting the form.

## Main application code

The following is the core Flask route logic in `app.py`:

``` python
import re

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        errors = {}

        if not name:
            errors["name"] = "Please enter your name."

        if not email:
            errors["email"] = "Please enter your email address."
        elif not EMAIL_PATTERN.match(email):
            errors["email"] = "Please enter a valid email address."

        if not message:
            errors["message"] = "Please enter a message."

        if errors:
            return render_template(
                "contact.html",
                errors=errors,
                name=name,
                email=email,
                message=message,
            ), 400

        return redirect(url_for("success"), code=303)

    return render_template(
        "contact.html",
        errors={},
        name="",
        email="",
        message="",
    )


@app.route("/contact/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
```

The email expression provides a basic format check. It does not verify
that the mailbox exists or that the visitor owns it.

## Templates

### `templates/contact.html`

The contact template contains the form and displays validation errors
returned by Flask. Its form should use `method="POST"` and submit to the
`/contact` route.

A simplified example of the form markup:

``` html
<form action="{{ url_for('contact') }}" method="POST">
    <label for="name">Name</label>
    <input id="name" name="name" type="text"
           value="{{ name }}" required>
    {% if errors.get('name') %}
        <p class="error">{{ errors.get('name') }}</p>
    {% endif %}

    <label for="email">Email</label>
    <input id="email" name="email" type="email"
           value="{{ email }}" required>
    {% if errors.get('email') %}
        <p class="error">{{ errors.get('email') }}</p>
    {% endif %}

    <label for="message">Message</label>
    <textarea id="message" name="message" required>{{ message }}</textarea>
    {% if errors.get('message') %}
        <p class="error">{{ errors.get('message') }}</p>
    {% endif %}

    <button type="submit">Send message</button>
</form>
```

### `templates/success.html`

The success template confirms that the form passed validation:

``` html
<h1>Thanks for your message</h1>
<p>Your form has been submitted successfully.</p>
```

The project's `static/styles.css` file contains the presentation styles.
Static files are referenced from the templates using Flask's
`url_for('static', filename='styles.css')`.

## Running the tests

The tests use pytest and Flask's test client. From the project root,
run:

``` bash
pytest
```

To stop a test run that is currently in progress, press `Ctrl + C`.

The test suite covers:

-   The contact page loads successfully.
-   An empty name is rejected.
-   An empty message is rejected.
-   An invalid email address is rejected.
-   A valid submission redirects to the success page and displays the
    confirmation message.

## Uploading the project to GitHub

If you have not already created a Git repository in the project folder,
run:

``` bash
git init
git add .
git commit -m "Add Flask contact form"
```

Create an empty repository on GitHub, then connect and push your local
project. Replace the URL with your repository URL:

``` bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

If the repository already has a remote called `origin`, do not add it
again. Check the configured remote with:

``` bash
git remote -v
```

## Limitations and possible improvements

-   The application does not store, email, or otherwise persist
    messages.
-   The email check verifies basic syntax only; it does not confirm that
    an address exists.
-   `debug=True` is suitable only for local development. Turn debug mode
    off when deploying the application.
-   Before using the form in production, consider adding CSRF
    protection, rate limiting, stronger input-handling controls, and an
    email or database integration if submissions need to be received or
    retained.

## License

Add a licence here if you intend to publish or distribute this project
under specific terms.
