from flask import Flask, flash, redirect, url_for
from flask_restful import Api
from flask_restful import Resource
from flask import request
from pydash import get
from functions import add_msg_to_stock, get_msg
from functions import stock
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjahkjshkjdhjs'
# api = Api(app)
# api.add_resource(Msg, '/msg')


@app.route('/', methods=['GET', 'POST'])
def send():
    messages = None
    if request.method == 'POST':
        recipient = request.form.get('recipient')
        sender = request.form.get('sender')
        msg = request.form.get('message')
        if len(recipient) == 0 or len(sender) == 0 or len(msg)==0:
            flash('Message was not sent, Please fill out all required fields', category='error')
        else:
            add_msg_to_stock(stock, sender, recipient, msg)
            flash('message sent successfully')
    else:
        recipient = request.args.get('getrecipient')
        if recipient is not None:
            messages = get_msg(stock, recipient)
            return render_template("chats.html", messages=messages)
    return render_template("chats.html")


if __name__ == '__main__':
    app.run(debug=True)