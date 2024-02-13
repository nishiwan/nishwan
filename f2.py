import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


with open('nom-email-ASIX2-2324.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    email_dict = {row['NOM']: row['EMAIL'] for row in csv_reader}

@app.route('/dashboard/<name>')
def dashboard(name):
  
    email = email_dict.get(name, 'Correo no encontrado')
    return f"Hello {name}, your email is {email}!"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('dashboard', name=user))
    else:
        user = request.args.get('name')
        return render_template('login.html', user=user)

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        new_name = request.form['new_name']
        new_email = request.form['new_email']

   
        email_dict[new_name] = new_email
        with open('nom-email-ASIX2-2324.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([new_name, new_email])

        return redirect(url_for('dashboard', name=new_name))
    else:
        return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
