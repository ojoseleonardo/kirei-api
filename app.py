from flask import Flask, jsonify
from Players.LeagueLeaders.OfficialLeaders.routes import official_leaders_bp

app = Flask(__name__)

# Registrar blueprints
app.register_blueprint(official_leaders_bp)

app.run(port=5000, host='localhost', debug=True)