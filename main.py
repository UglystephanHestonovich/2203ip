from flask import Flask, request

app = Flask(__name__)


@app.route('/sum/', methods=['POST'])
def hello_world():
    a = request.json['a']
    b = request.json['b']
    c = {'sum': a + b}
    return c

@app.route('/sum2/', methods=['POST'])
def hello_world2():
    a = list(request.json['data'])
    b = sum(a)
    c = {'sum': b}
    return c

@app.route('/sum3/', methods=['POST'])
def hello_world3():
    a = request.json.values()
    b = sum(a)
    c = {'sum': b}
    return c

@app.route('/nextround/', methods=['POST'])
def hello_world4():
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
def hello_world5():
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

@app.route('/imt/', methods=['POST'])
def hello_world6():
    a = request.json
    if 'imt' not in a:
        a['imt'] = int(a['weight'] / (a['height'] / 100)**2)
        return {'status': 'ok', 'imt': a['imt']}
    if 'weight' not in a:
        a['weight'] = int(a['imt'] * (a['height'] / 100)**2)
        return {'status': 'ok', 'weight': a['weight']}
    if 'height' not in a:
        a['height'] = int((((a['weight'] / a['imt']) ** 0.5) * 100))
        return {'status': 'ok', 'height': a['height']}


app.run(host='128.1.12.94', port=5000)

