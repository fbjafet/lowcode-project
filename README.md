lowcode-project
# Lowcode Project - Flask Web Application



A minimal Flask 3.x web application that serves a single page displaying a personalized greeting.



\## What It Does



This application starts a local web server and serves a webpage at the custom URL path `/C:/Users/fabia/Documents/lowcode-project`, returning the text "Hello from Fabiana Jafet".



\## Requirements



\* Python 3.8 or higher

\* `pip` package manager ##FJ: Pip installs packages - packager manager for Python



\##FJ: It's requires also:

Werkzeug==3.0.3

Jinja2==3.1.4

ItsDangerous==2.2.0

Click==8.1.7



\## Installation



\##FJ: Code:



from flask import Flask



app = Flask(\_\_name\_\_)



\# Flask uses forward slashes for URL routing paths

@app.route("/C:/Users/fabia/Documents/lowcode-project")

def lowcode\_project():

&#x20;   return "<h1>Hello from Fabiana Jafet</h1>"



if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   app.run(debug=True)



1\. Clone or download this repository into your project folder.

2\. Open your terminal or Command Prompt in the project folder. 

3\. Install the required dependencies:



```bash

pip install -r requirements.txt

```



\## How to Run



1\. Start the Flask application:



```bash

python app.py

```



2\. Open your web browser and navigate to:



```text

http://127.0.0.1:5000/C:/Users/fabia/Documents/lowcode-project

```

## Project Idea

What would you build if it took an evening instead of a quarter?

If I only have an evening I would build an App to organize my agenda, both personal and professional. In this App I would gather the information from WhatsApp groups, email accounts and online calendars, and create tasks to be done by day and/or month as well as show me the subscriptions that are active on my accounts, future events, and bills to be paid. All things separated by sections on the App with respective push notifications.
For bills and subscriptions, the App will create a task on my calendar, job related tasks would be gathered in a planner, and for future events only a reminder will be shown with the option to engage or discard the event. This App will incorporate Microsoft and Google tools and will run an automation through all requested platforms.




3\. To stop the server, press `Ctrl + C` in your terminal.

