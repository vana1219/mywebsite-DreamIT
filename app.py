from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Houston, TX',
    'salary': '$140,000'
}, {
    'id': 2,
    'title': 'Front-end Engineer',
    'location': 'San Francisco, CA',
    'salary': '$100,000'
}, {
    'id': 3,
    'title': 'Back-end Engineer',
    'location': 'San Francisco, CA',
    'salary': '$120,000'
}, {
    'id': 4,
    'title': 'Cyber-Security Engineer',
    'location': 'Remote'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
