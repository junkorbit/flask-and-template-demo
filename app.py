from flask import Flask, render_template, redirect, request, session
import config

import random

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

blobs = [
    {'name': 'naughty cancer blob', 'image': 'naughty_blob_one.png'},
    {'name': 'naughty other thing blob', 'image':  'naughty_blob_two.png'},
    {'name': 'another naughty blob name', 'image':  'naughty_blob_three.png'},
]

@app.route('/', methods=['GET', 'POST'])
def index():

    successes = session.get('successes', 0)
    blob = session.get('blob', random.choice(blobs))
    session['blob'] = blob

    if request.method == 'POST':

        guess = request.form.get('blob')

        if guess.lower() == blob['name'].lower():

            session['successes'] = successes + 1
            session['blob'] = random.choice(blobs)

            return redirect('/')

        else:
            session['successes'] = 0

            session['blob'] = random.choice(blobs)

            return render_template('wrong.html', successes=successes, blob_name=blob['name'])

    return render_template('index.html', image=blob['image'], successes=successes, failed=True)


if __name__ == '__main__':
    app.run()
