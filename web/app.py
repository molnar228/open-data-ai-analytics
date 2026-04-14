import os
import json
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

REPORTS_DIR = "/app/reports"
PLOTS_DIR = "/app/plots"


def load_json(filename):
    path = os.path.join(REPORTS_DIR, filename)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": f"Файл {filename} ще не створено."}


@app.route('/')
def index():
    quality_data = load_json("quality_report.json")
    research_data = load_json("research_report.json")

    return render_template('index.html', quality=quality_data, research=research_data)


@app.route('/plots/<filename>')
def serve_plot(filename):
    return send_from_directory(PLOTS_DIR, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)