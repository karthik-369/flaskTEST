from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Delhi, India',
        'salary': 'Rs. 9,00,000'
    },
    {
        'id':2,
        'title':'Developer',
        'location':'Chennai, India',
        'salary': 'Rs. 18,00,000'
    },
    {
        'id':3,
        'title':'Data Engineer',
        'location':'Bengaluru, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id':4,
        'title':'Data Scientist',
        'location':'Chicago, India',
        'salary': 'Rs. 20,00,000'
    }
]

@app.route('/')
def home():
    return render_template("home.html", jobs = JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run()

