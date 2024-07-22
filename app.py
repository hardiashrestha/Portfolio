from flask import Flask, render_template_string

app = Flask(__name__)

# Sample portfolio data
portfolio_data = {
    "name": "Shrestha Hardia",
    "email": "hardiashrestha@gmail.com",
    "linkedin": "1234...",
    "about": "An ambitious and dedicated individual with a strong passion for AI and machine learning, actively engaged in research, coding projects, and competitive events to build a robust profile for a future in Computer Science and Engineering.",
    "experience": [
        {
            "title": "Research Intern, Incognito Blueprints Summer Bootcamp",
            "duration": "May, 2024 – Present",
            "details": [
                "Employed advanced deep learning techniques to enhance classification accuracy of dermatological diseases.",
                "Secured 1st Place, Incognito Blueprints Summer Bootcamp, 2024"
            ]
        },
        {
            "title": "Member, Buildspace N&W",
            "duration": "Jun 2024 - Present",
            "details": [
                "Building a music streaming platform named Streamify (currently under development)."
            ]
        }
    ],
    "github_stats": {
        "stats_url": "https://github-readme-stats.vercel.app/api?username=hardiashrestha&show_icons=true&theme=dracula",
        "streak_url": "https://github-readme-streak-stats.herokuapp.com/?user=hardiashrestha&theme=dracula"
    }
}

# HTML Template as a string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.name }}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="static/css/styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@400;700&display=swap" rel="stylesheet">
    <script src="https://kit.fontawesome.com/1bd99a004e.js" crossorigin="anonymous"></script>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
    <div class="container">
        <a class="navbar-brand" href="#">HOME</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="#about">About Me</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#research">Experience</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#tech">Tech I Use</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#contact">Contact</a>
                </li>
            </ul>
        </div>
    </div>
</nav>

<div class="container" style="margin-top: 80px;">
    <section id="about" class="section">
        <div class="text-center">
            <h1><span class="name">{{ data.name }}</span></h1>
            <p>Email: {{ data.email }} | LinkedIn: {{ data.linkedin }}</p>
            <img align="center" alt="Coding" width="400" src="https://cdn.dribbble.com/users/1162077/screenshots/3848914/programmer.gif">
            <p class="highlight">{{ data.about }}</p>
        </div>
    </section>

    <section id="research" class="section text-center">
        <h2>Experience</h2>
        {% for job in data.experience %}
            <p><strong>{{ job.title }}</strong> ({{ job.duration }})</p>
            <ul class="list-unstyled"> <!-- Removed bullets -->
                {% for detail in job.details %}
                    <li>{{ detail }}</li>
                {% endfor %}
            </ul>
        {% endfor %}
    </section>

    <section id="tech" class="section text-center">
        <h2>Tech I Use</h2>
        <div class="row">
            <div class="col-md-4 mb-4">
                <div class="card tech-card">
                    <div class="card-body">
                        <i class="fab fa-python fa-3x tech-icon"></i>
                        <h5 class="card-title">Python</h5>
                        <p class="card-text">High-level programming language for general-purpose tasks.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card tech-card">
                    <div class="card-body">
                        <i class="fab fa-html5 fa-3x tech-icon"></i>
                        <h5 class="card-title">HTML</h5>
                        <p class="card-text">Markup language for creating web pages.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card tech-card">
                    <div class="card-body">
                        <i class="fab fa-css3-alt fa-3x tech-icon"></i>
                        <h5 class="card-title">CSS</h5>
                        <p class="card-text">Style sheet language for describing the presentation of a document.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card tech-card">
                    <div class="card-body">
                        <i class="fab fa-git-alt fa-3x tech-icon"></i>
                        <h5 class="card-title">Git</h5>
                        <p class="card-text">Distributed version control system for tracking changes in source code.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card tech-card">
                    <div class="card-body">
                        <i class="fas fa-database fa-3x tech-icon"></i>
                        <h5 class="card-title">SQL</h5>
                        <p class="card-text">Programming language for managing data in relational databases.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card tech-card">
                    <div class="card-body">
                        <i class="fab fa-django fa-3x tech-icon"></i>
                        <h5 class="card-title">Django</h5>
                        <p class="card-text">High-level Python web framework for rapid development.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card tech-card">
                    <div class="card-body">
                        <i class="fab fa-react fa-3x tech-icon"></i>
                        <h5 class="card-title">React</h5>
                        <p class="card-text">JavaScript library for building user interfaces.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card tech-card">
                    <div class="card-body">
                        <i class="fab fa-js-square fa-3x tech-icon"></i>
                        <h5 class="card-title">JavaScript</h5>
                        <p class="card-text">High-level programming language for web development.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="github-stats" class="section text-center">
        <h2>GitHub Stats</h2>
        <p align="center">
            <img src="{{ data.github_stats.stats_url }}" alt="GitHub Stats" />
            <img src="{{ data.github_stats.streak_url }}" alt="GitHub Streak" />
        </p>
    </section>

    <section id="contact" class="section text-center">
        <h2>Contact Me</h2>
        <div class="contact-icons">
            <a href="mailto:hardiashrestha@gmail.com" class="contact-icon">
                <i class="fas fa-envelope fa-2x"></i>
            </a>
            <a href="https://discord.com/users/1046787841738412093" class="contact-icon">
                <i class="fab fa-discord fa-2x"></i>
            </a>
            <a href="https://x.com/shresthahardia" class="contact-icon">
                <i class="fab fa-x fa-2x"></i>
            </a>
            <a href="https://github.com/hardiashrestha" class="contact-icon">
                <i class="fab fa-github fa-2x"></i>
            </a>
        </div>
    </section>
</div>

<footer>
    <div class="container text-center">
        <p>© 2024 {{ data.name }}. All rights reserved.</p>
    </div>
</footer>

<script>
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
</script>

</body>
</html>
"""

@app.route('/')
def home():
    """Render the home page with portfolio data."""
    return render_template_string(HTML_TEMPLATE, data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
