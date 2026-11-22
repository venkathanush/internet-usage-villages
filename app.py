import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Project data
PROJECT_DETAILS = {
    'title': 'Internet Usage in Villages',
    'locality': 'KOVUR, SPSR Nellore District, Andhra Pradesh',
    'team_leader': 'G. Suchethan',
    'team_members': [
        {'name': 'G.Dhanush Reddy', 'roll': '24JNA05275', 'phone': '7780295256', 'position': 'Team Member'},
        {'name': 'G.V.Leela Sai', 'roll': '24JNA05235', 'phone': '9493605797', 'position': 'Team Member'},
        {'name': 'G.Santhosh', 'roll': '24JNA05250', 'phone': '9014303875', 'position': 'Team Member'},
        {'name': 'G.Manoj Kumar', 'roll': '24JNA05246', 'phone': '9160391815', 'position': 'Team Member'}
    ],
    'project_dates': {
        'main': '1/6/26 to 12/7/26 (6 weeks)',
        'mini': '13/7/26 to 26/7/26 (2 weeks)'
    },
    'mini_project_stack': {
        'frontend': 'HTML, CSS, JavaScript (lightweight web/mobile UI)',
        'backend': 'Python / Flask (or static / local-storage MVP)',
        'database': 'SQLite / MySQL / CSV internet usage & agronomic rules database',
        'recommendation_logic': 'Rule-based constraint filtering + weighted scoring (connectivity, speed, accessibility, socioeconomic factors)',
        'data_source': 'Atmakur village farmer surveys, internet accessibility reports & agricultural references'
    },
    'project_dates_text': 'Main project: 1 June 2026 to 12 July 2026 (6 weeks)<br>Mini project: 13 July 2026 to 26 July 2026 (2 weeks)'
}

@app.route('/')
def index():
    return render_template('index.html', project=PROJECT_DETAILS)

@app.route('/photos/<path:filename>')
def serve_photos(filename):
    return send_from_directory('photos', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)