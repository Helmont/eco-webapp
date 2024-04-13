from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Abuja, Nigeria',
    'Salary': 'N900,000',
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Lagos, Nigeria',
    'Salary': 'N1,900,000',
}, {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'Kano, Nigeria',
}, {
    'id': 4,
    'title': 'Full stack webdeveloper',
    'location': 'Kaduna, Nigeria',
    'Salary': 'N950,000',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Ecoplorer')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
