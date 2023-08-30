from flask import Flask, request, jsonify
from webScraperBot import TrademarkBot

app = Flask(__name__)

# Initialize the TrademarkBot instance
bot = TrademarkBot()

@app.route("/check-trademark", methods=["POST"])
def check_trademark():
    try:
        data = request.get_json()
        trademark = data.get("trademark")

        availability = bot.check_availability(trademark)

        return jsonify({"available": availability})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
    print('WOOOOOOOOOO')
