from flask import Flask, render_template

app = Flask(__name__)

JOBS = {
  {
  'id': 1,
  'title': 'Data Scientist',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'
},
{
  'id': 2,
  'title': 'Data Analyst',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,00,000'
},
{
  'id': 3,
  'title': 'frontend Engineer',
  'location': 'Remote',
  'salary': 'Rs. 12,00,000'
},
{
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Francisco, USA',
  'salary': 'Rs. $2,00,000'
}
},

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS, company_name='Tocheel')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
  