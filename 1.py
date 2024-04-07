from flask import Flask, render_template, redirect
import json
from random import randint

app = Flask(__name__)

with open('templates/members.json') as f:
    members = json.load(f)


@app.route('/')
def main():
    return redirect('/member')


@app.route('/member')
def member():
    member = members[randint(0, len(members) - 1)]
    member['professional'] = sorted(member['professional'])
    prof = ', '.join(member['professional'])
    return render_template('auto_answer.html', member=member,prof=prof)


app.run()
