from flask import Flask, render_template
import json
app = Flask(__name__)
with open('portfolio_data.json') as f:
    portfolio_data = json.load(f)
@app.route('/')
def home():
    """Render the home page with portfolio data."""
    return render_template('index.html', data=portfolio_data)
if __name__ == '__main__':
    app.run(debug=True)
