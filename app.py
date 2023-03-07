from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'Location': 'Lagos, Nigeria',
    'Salary': 'Rs. 500,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'Location': 'Abuja, Nigeria',
    'Salary': 'Rs. 550,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'Location': 'Remote',
    'Salary': 'Rs. $120,000'
  },
  {
    'id': 4,
    'title': 'Backtend Engineer',
    'Location': 'Enugu, Nigeria',
    'Salary': 'Rs. $50,000'
  }
]

@app.route("/")
def hello_Tocheel():
  return render_template('home.html', jobs=JOBS,
                          company_name='Tocheel')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
  