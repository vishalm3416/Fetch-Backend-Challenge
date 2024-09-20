from flask import Flask, request, jsonify

app = Flask(__name__)


transactions = []
balance = {}

@app.route('/add', methods=['POST'])
def addPts():

    data = request.get_json()

    if not all(k in data for k in ('payer', 'points', 'timestamp')):
        return 'Invalid Request.', 400
    
    transactions.append({
        'payer': data['payer'],
        'points': data['points'],
        'timestamp': data['timestamp']
    })

    if data['payer'] in balance:
        balance[data['payer']] += data['points']
    else:
        balance[data['payer']] = data['points']

    return '', 200

@app.route('/spend', methods=['POST'])
def spendPts():

    data = request.get_json()

    if 'points' not in data:
        return 'Invalid Request.', 400
    
    ptsToSpend = data['points']
    ptsAvailable = sum(balance.values())

    if ptsToSpend > ptsAvailable:
        return 'User does not have enough points.', 400

    trSorted = sorted(transactions, key=lambda t: t['timestamp'])
    res = {}

    for tr in trSorted:

        if tr['points'] <= ptsToSpend:
            ptsToSpend -= tr['points']
            balance[tr['payer']] -= tr['points']

            if tr['payer'] in res:
                res[tr['payer']] -= tr['points']
            else:
                res[tr['payer']] = -tr['points']

            tr['points'] = 0
        else:
            tr['points'] -= ptsToSpend
            balance[tr['payer']] -= ptsToSpend

            res[tr['payer']] = -ptsToSpend

            ptsToSpend = 0
            break

    result = [{"payer": company, "points": points} for company, points in res.items()]
    return jsonify(result), 200

@app.route('/balance', methods=['GET'])
def getBal():
    return jsonify(balance), 200

if __name__ == '__main__':
    app.run(port=8000)