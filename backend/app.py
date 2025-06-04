from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

usuarios = [
    {"id": 1, "nombre": "Andrés", "edad": 17},
    {"id": 2, "nombre": "Jean", "edad": 20}
]

@app.route('/')
def interfaz():
    return render_template('index.html')

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario)

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    if not datos or 'nombre' not in datos or 'edad' not in datos:
        return jsonify({"error": "Datos incompletos"}), 400
    nuevo_id = max([u["id"] for u in usuarios], default=0) + 1
    nuevo_usuario = {"id": nuevo_id, "nombre": datos["nombre"], "edad": datos["edad"]}
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    datos = request.get_json()
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    usuario.update({
        "nombre": datos.get("nombre", usuario["nombre"]),
        "edad": datos.get("edad", usuario["edad"])
    })
    return jsonify(usuario)

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    global usuarios
    usuarios = [u for u in usuarios if u['id'] != id]
    return jsonify({"mensaje": "Usuario eliminado"}), 200

if __name__ == '__main__':
    app.run(debug=True)