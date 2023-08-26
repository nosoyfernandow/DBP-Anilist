from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Cargar datos desde el archivo anime.json
with open('anime.json') as f:
    data = json.load(f)
animes = data['anime']

@app.route('/')
def index():
    return data

@app.route('/anime', methods=['GET'])
def get_animes():
    return jsonify(animes)

@app.route('/anime/<int:id>', methods=['GET'])
def get_anime(id):
    anime = next((anime for anime in animes if anime['id'] == id), None)
    if anime:
        return jsonify(anime)
    return jsonify({"Anime no encontrado"}), 404

@app.route('/anime', methods=['POST'])
def create_anime():
    new_anime = request.json
    new_anime['id'] = len(animes) + 1
    animes.append(new_anime)
    with open('anime.json', 'w') as f:
        json.dump(data, f, indent=4)
    return jsonify(new_anime), 201

@app.route('/anime/<int:id>', methods=['PUT'])
def update_anime(id):
    anime = next((anime for anime in animes if anime['id'] == id), None)
    if anime:
        updated_anime = request.json
        anime.update(updated_anime)
        with open('anime.json', 'w') as f:
            json.dump(data, f, indent=4)
        return jsonify(anime)
    return jsonify({"Anime no encontrado"}), 404

@app.route('/anime/<int:id>', methods=['PATCH'])
def patch_anime(id):
    anime = next((anime for anime in animes if anime['id'] == id), None)
    if anime:
        updates = request.json
        anime.update(updates)
        with open('anime.json', 'w') as f:
            json.dump(data, f, indent=4)
        return jsonify(anime)
    return jsonify({"Anime no encontrado"}), 404

@app.route('/anime/<int:id>', methods=['DELETE'])
def delete_anime(id):
    anime = next((anime for anime in animes if anime['id'] == id), None)
    if anime:
        animes.remove(anime)
        with open('anime.json', 'w') as f:
            json.dump(data, f, indent=4)
        return jsonify({"Anime eliminado"})
    return jsonify({"Anime no encontrado"}), 404

if __name__ == '__main__':
    app.run()