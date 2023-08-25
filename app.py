from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos de ejemplo para la lista de animes
animes = []

@app.route('/')
def index():
    return '¡Hola, mundo! Esta es mi primera API con Flask.'

@app.route('/anime', methods=['GET'])
def get_animes():
    return jsonify(animes)

@app.route('/anime/<int:id>', methods=['GET'])
def get_anime(id):
    return jsonify({"message": "Obtener detalles del anime con ID " + str(id)})

@app.route('/anime/<int:id>', methods=['DELETE'])
def delete_anime(id):
    return jsonify({"message": "Eliminar anime con ID " + str(id)})

@app.route('/anime', methods=['POST'])
def create_anime():
    new_anime = request.get_json()
    return jsonify(new_anime)

@app.route('/anime/<int:id>', methods=['PUT'])
def update_anime(id):
    updated_anime = request.get_json()
    return jsonify(updated_anime)

@app.route('/anime/<int:id>', methods=['PATCH'])
def partial_update_anime(id):
    updated_fields = request.get_json()
    return jsonify(updated_fields)

if __name__ == '__main__':
    app.run()