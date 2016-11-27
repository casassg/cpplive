import json

import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def ffmain():
    return render_template('parallel.html')


# ToDo: change 'code' for ref
@app.route("/execute", methods=['POST'])
def ffprint():
    with open("code.cc", "w") as code:
        code.write(request.form.get('code'))
    # inp = open("code.in", "w")
    # inp.write(request.form.get('inp'))
    # inp.close()
    out = ''
    if os.system("g++ code.cc -o code.out 2>code.err") == 0:
        # os.system("./code.out <code.in >code.txt")
        os.system("./code.out  >code.txt 2>code.err")
        with open("code.txt", "r") as f:
            out = f.read()
        errno = 0
    else:
        errno = 1

    with open('code.err', 'r') as f:
        err = f.read()

    return json.dumps({"out": out, "errno": errno, 'err': err})

if __name__ == "__main__":
    app.run(debug=True)
