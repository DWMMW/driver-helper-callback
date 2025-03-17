from flask import Flask, request

app = Flask(__name__)

@app.route('/result', methods=['POST'])
def result():
    data = request.form
    order_id = data.get('orderid')
    amount = data.get('amount')
    status = data.get('status')
    if status == '1':
        print(f"Оплата {order_id} на {amount} RUB успешна!")
        return "OK", 200
    return "FAIL", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
