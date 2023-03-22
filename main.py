from flask import Flask, request

app = Flask(__name__)


@app.route('/sum/', methods=['POST'])
def hello_world():
    a = request.json['a']
    b = request.json['b']
    c = {'sum': a + b}
    return c

@app.route('/sum2/', methods=['POST'])
def hello_world():
    a = list(request.json['data'])
    b = sum(a)
    c = {'sum': b}
    return c

@app.route('/sum3/', methods=['POST'])
def hello_world():
    a = request.json.values()
    b = sum(a)
    c = {'sum': b}
    return c

@app.route('/nextround/', methods=['POST'])
def hello_world():
    n = request.json['n']
    k = request.json['k']
    d = request.json['data']
    a = 0

    for i in range(n):
        c = d[k]
        if d[i] >= c and d[i] > 0:
            a += 1

    return {"res": a}

@app.route('/lexographically/', methods=['POST'])
def hello_world():
    a = request.json['a'].lower()
    b = request.json['b'].lower()
    c = 0

    for i in range(len(b)):
        if ord(a[i]) == ord(b[i]):
            c += 0

        elif ord(a[i]) > ord(b[i]):
            c += 1

        elif ord(a[i]) < ord(b[i]):
            c += -1

    return {'res': c}

app.run(host='128.1.12.94', port=5000)

