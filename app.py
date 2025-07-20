from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/api/data/terms_of_service')
def get_terms_of_service():
    return render_template('terms_of_service.html')

@app.route('/api/data/privacy_policy')
def get_privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/api/data/community_guidelines')
def get_community_guidelines():
    return render_template('community_guidelines.html')

@app.route('/api/data/report_vulnerability')
def get_report_vulnerability():
    return render_template('report_vulnerability.html')

if __name__ == "__main__":
    app.run(debug=True)