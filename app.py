from flask import Flask, render_template

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

@app.route('/')
def home():
    """Render the home page with portfolio data."""
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)