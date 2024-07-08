from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            listed_price = float(request.form['listed_price'])
            sold_price = float(request.form['sold_price'])
        except (KeyError, ValueError) as e:
            return render_template('index.html', error="Invalid input. Please enter valid numbers.")

        commission_rate = 0.075  # Example: 7.5%
        vat_rate = 0.15  # Example: 15% VAT

        commission = sold_price * commission_rate
        vat = commission * vat_rate
        net_commission = commission - vat
        agent_share = net_commission / 2

        return render_template('index.html', 
                               listed_price=listed_price, 
                               sold_price=sold_price, 
                               commission=round(commission, 2), 
                               vat=round(vat, 2), 
                               net_commission=round(net_commission, 2), 
                               agent_share=round(agent_share, 2))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
