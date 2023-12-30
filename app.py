from flask import Flask, request, render_template
from flask_cors import CORS
from datetime import datetime

from izipay import initForm, get_signature
from keys import CONFIG

app = Flask(__name__)
cors = CORS(app)

@app.get('/')
def root():
    order = datetime.now().strftime("Order-%Y%m%d%H%M%S")
    return render_template('index.html', data={"order": order})

@app.post('/confirm', )
def confirm():
    paymentConfig = initForm()
    paymentConfig["vads_cust_first_name"] = request.form["firstname"]
    paymentConfig["vads_cust_last_name"] = request.form["lastname"]
    paymentConfig["vads_cust_email"] = request.form["email"]
    paymentConfig["vads_order_id"] = request.form["order"]
    paymentConfig["vads_amount"] = int(request.form['amount']) * 100
    paymentConfig["vads_url_return"] = request.host_url + 'status?order=' + request.form["order"]
    paymentConfig["vads_return_mode"] = "GET"

    paymentConfig["signature"] = get_signature(paymentConfig, CONFIG['CLAVE'])

    return render_template('confirm.html', data=paymentConfig, URL=CONFIG['URL'])

@app.get('/status')
def paymentResult():
    args = request.args
    amount = int(args.get('vads_amount')) / 100
    return render_template('status.html', data=args, amount=amount)


@app.post('/ipn')
def ipn():
    if ( request.form.get("vads_hash") == None ): return "Invalid data", 400

    signature = get_signature(request.form, CONFIG["CLAVE"])

    if ( not (request.form["signature"] == signature) ): return "Signature Invalid", 200

    return f"Transaccion is {request.form["vads_trans_status"]}!", 200


if __name__ == '__main__':
    app.run(debug=True)
