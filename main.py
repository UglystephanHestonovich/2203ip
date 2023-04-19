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
        a['imt'] = int(a['weight'] / (a['height'] / 100) ** 2)
        return {'status': 'ok', 'imt': a['imt']}
    if 'weight' not in a:
        a['weight'] = int(a['imt'] * (a['height'] / 100) ** 2)
        return {'status': 'ok', 'weight': a['weight']}
    if 'height' not in a:
        a['height'] = int((((a['weight'] / a['imt']) ** 0.5) * 100))
        return {'status': 'ok', 'height': a['height']}
    
dogyears = {1:14, 1.5:20, 2:24, 3:30, 4:36, 5:40, 6:42, 7:49, 8:56, 9:63, 10:65, 11:71, 12:75}
humanyears = {14:1, 20:1.5, 24:2, 30:3, 36:4, 40:5, 42:6, 49:7, 56:8, 63:9, 65:10, 71:11, 75:12}
dogmonths = {2:14, 6:5, 8:9}
humanmonths = {14:2, 5:6, 9:8}
@app.route('/lebo1/', methods=['POST'])
def hello_world7():
    if request.json['type'] == 'dog' and request.json['units'] == 'years':
        a = dogyears[request.json['n']]
        return {'n': a, 'units': 'years', 'type': 'human'}
    elif request.json['type'] == 'human' and request.json['units'] == 'years' and request.json['n'] >= 14:
        b = humanyears[request.json['n']]
        return {'n': b, 'units': 'years', 'type': 'dog'}
    elif request.json['type'] == 'human' and request.json['units'] == 'month' and request.json['n'] == 14:
        b = humanmonths[request.json['n']]
        return {'n': b, 'units': 'month', 'type': 'dog'}
    elif request.json['type'] == 'dog' and request.json['units'] == 'month' and request.json['n'] > 2:
        a = dogmonths[request.json['n']]
        return {'n': a, 'units': 'years', 'type': 'human'}
    elif request.json['type'] == 'dog' and request.json['units'] == 'month' and request.json['n'] == 2:
        a = dogmonths[request.json['n']]
        return {'n': a, 'units': 'month', 'type': 'human'}
    elif request.json['type'] == 'human' and request.json['units'] == 'years' and request.json['n'] <= 9:
        b = humanmonths[request.json['n']]
        return {'n': b, 'units': 'month', 'type': 'dog'}

app.run(host='128.1.12.94', port=5000)

