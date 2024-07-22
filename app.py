from flask import Flask, render_template

app = Flask(__name__)

# Sample data
portfolio_data = {
    "name": "Shrestha Hardia",
    "email": "hardiashrestha@gmail.com",
    "linkedin": "1234...",
    "about": "Ambitious high school graduate with a strong foundation in research and technology.",
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
    "skills": [
        "Learning and enhancing Python skills",
        "Excellent written and verbal communication skills",
        "Team collaboration and leadership"
    ],
    "languages": "Hindi (Native), English",
    "github_stats": {
        "stats_url": "https://github-readme-stats.vercel.app/api?username=hardiashrestha&show_icons=true&theme=dracula",
        "streak_url": "https://github-readme-streak-stats.herokuapp.com/?user=hardiashrestha&theme=dracula"
    }
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
