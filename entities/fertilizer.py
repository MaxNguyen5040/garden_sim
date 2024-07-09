class Fertilizer:
    def __init__(self, name, nutrient_boost):
        self.name = name
        self.nutrient_boost = nutrient_boost

from flask import Flask, jsonify, request
from soil import Soil
from fertilizer import Fertilizer

app = Flask(__name__)
soil = Soil()
fertilizers = {
    "basic": Fertilizer("Basic Fertilizer", 10),
    "premium": Fertilizer("Premium Fertilizer", 20),
}

@app.route('/add_fertilizer', methods=['POST'])
def add_fertilizer():
    fertilizer_type = request.json.get('type')
    fertilizer = fertilizers.get(fertilizer_type)
    if fertilizer:
        soil.add_fertilizer(fertilizer.nutrient_boost)
        return jsonify({"message": f"{fertilizer.name} added", "nutrient_levels": soil.get_nutrient_levels()})
    else:
        return jsonify({"message": "Invalid fertilizer type"}), 400

if __name__ == "__main__":
    app.run(debug=True)
