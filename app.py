from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Lagos, Nigeria',
  'salary': '#550,000'
},
{
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Abuja, Nigeria',
  'salary': '#610,000'
},
{
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
},
{
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Enugu, Nigeria',
  'salary': '#570,000'
},
]

@app.route("/")
def hello_Tocheel():
  return render_template('home.html',
                        jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
  