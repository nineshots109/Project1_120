from flask import Flask, render_template

app = Flask(__name__)

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    # Define variables for dynamic content
    name = "Your Name"
    bio = "Brief Bio Here"

    # Render the home.html template with dynamic content
    return render_template('home.html')

@app.route('/project1')
def project1():
    # Define variables for dynamic content
    project_title = "Project 1"
    project_description = "Brief description of Project 1"

    # Render the project1.html template with dynamic content
    return render_template('project1.html', project_title=project_title, project_description=project_description)

@app.route('/project2')
def project2():
    # Define variables for dynamic content
    project_title = "Project 2"
    project_description = "Brief description of Project 2"

    # Render the project2.html template with dynamic content
    return render_template('project2.html', project_title=project_title, project_description=project_description)

@app.route('/project3')
def project3():
    # Define variables for dynamic content
    project_title = "Project 3"
    project_description = "Brief description of Project 3"

    # Render the project3.html template with dynamic content
    return render_template('project3.html', project_title=project_title, project_description=project_description)

if __name__ == '__main__':
    app.run(debug=True)
