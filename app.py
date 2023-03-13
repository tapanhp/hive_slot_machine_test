from flask import Flask
from services.slot_machine_service import get_all_slot_items_response
from services.credit_service import retrieve_all_cash_for_session
from dotenv import load_dotenv

# Same method is called in config file to run independent script, but it shouldn't
load_dotenv()
app = Flask(__name__)


# Should be attached to particular user's session
@app.route("/cash-out", methods=["GET"])
def cash_out():
    return retrieve_all_cash_for_session()


@app.route("/game/play", methods=["POST"])
def play_round():
    return {}


@app.route("/game/slot_items", methods=["GET"])
def get_game_items():
    return get_all_slot_items_response()


if __name__ == '__main__':
    app.run()
