from flask import Flask, jsonify, request
from flask_cors import CORS # para permitir el acceso a la API desde el frontend
import pymysql
import bcrypt # incriptar contrasena
from flasgger import Swagger

app = Flask(__name__)
CORS(app)
Swagger = Swagger(app)

#conexion a la base de datos
def conectar(vhost, vuser, vpass, vdb):
    conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset='utf8mb4')
    return conn

# ruta inicial
@app.route("/", methods=['GET'])
def index():
    return jsonify({"mensaje": "API del Banco de Alimentos"})


# consulta de tipo de usuario
@app.route("/tipo_usuario", methods=['GET'])
def tipo_usuario():
    """
    consulta de tipo_usuario
    ---
    responses:
      200:
        description: lista de tipos de usuario
    """
    try:
        conn = conectar('localhost','root','Es1084734914','proyecto') # se conecta a la base de datos
        cur = conn.cursor() # cursor para ejecutar consultas
        cur.execute("SELECT * FROM tipo_usuario") 
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_tipo_usuario':row[0], 
                'descripcion':row[1]
            }
            data.append(dato) # se agrega a la lista
        cur.close()
        conn.close()
        return jsonify({'tipo_usuario': data, 'mesaje': 'Lista De Tipo Usuario'})
    except Exception as ex:
        print(ex) # imprime el error
        return jsonify ({'mesaje': 'Error'})
    

# Ruta para eliminar registro por ID tipo_usuario
@app.route("/eliminar_tipo_usuario/<int:codigo>", methods=['DELETE'])
def eliminar_tipo_usuario(codigo):
    """
    Eliminar tipo de usuario por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Tipo de usuario eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM tipo_usuario WHERE id_tipo_usuario = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


    # Ruta para registrar un nuevo tipo_usuario
@app.route("/registro_tipo_usuario", methods=['POST'])
def registro_tipo_usuario():
    try:
        data = request.get_json()
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO tipo_usuario (descripcion) VALUES (%s)", (descripcion,))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
# Ruta para actualizar un tipo_usuario
@app.route("/actualizar_tipo_usuario/<codigo>", methods=["PUT"])
def actualizar_tipo_usuario(codigo):

    try:
        data = request.get_json()
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE tipo_usuario SET descripcion= %s WHERE id_tipo_usuario= %s", 
                    (descripcion,codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# ruta de tipo_documento
@app.route("/tipo_documento", methods=['GET'])
def tipo_documento():
    """
    consulta de tipo_documento
    ---
    responses:
      200:
        description: lista de tipo de documento
    """
    try:
        conn = conectar('localhost','root','Es1084734914','proyecto') # se conecta a la base de datos
        cur = conn.cursor() # cursor para ejecutar consultas
        cur.execute("SELECT * FROM tipo_documento") 
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_tipo_documento':row[0], 
                'nombre':row[1],
                'abreviatura':row[2]
            }
            data.append(dato) # se agrega a la lista
        cur.close()
        conn.close()
        return jsonify({'tipo_documento': data, 'mensaje': 'Lista De Tipo Documento'})
    except Exception as ex:
        print(ex) # imprime el error
        return jsonify ({'mensaje': 'Error'})

# Ruta para registrar un nuevo tipo_documento
@app.route("/registro_tipo_documento", methods=['POST'])
def registro_tipo_documento():
    try:
        data = request.get_json()
        nombre = data['nombre']
        abreviatura = data['abreviatura']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO tipo_documento (nombre, abreviatura) VALUES (%s, %s)", (nombre, abreviatura))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


# Ruta para actualizar un tipo_documento
@app.route("/actualizar_tipo_documento/<codigo>", methods=["PUT"])
def actualizar_tipo_documento(codigo):
    try:
        data = request.get_json()
        nombre = data['nombre']
        abreviatura = data['abreviatura']
        
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE tipo_documento SET nombre= %s, abreviatura= %s WHERE id_tipo_documento= %s", 
                    (nombre, abreviatura, codigo))
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
# Ruta para eliminar tipo_documento
@app.route("/eliminar_tipo_documento/<int:codigo>", methods=['DELETE'])
def eliminar_tipo_documento(codigo):
    """
    Eliminar tipo de documento por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: tipo de documento eliminado
    """

    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM tipo_documento WHERE id_tipo_documento = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# ruta tipo_gasto
@app.route("/tipo_gasto", methods=['GET'])
def tipo_gasto():
    """
    Consulta de lista de tipos de gasto
    ---
    responses:
      200:
        description: lista de tipos de gasto
    """
    try:
        conn = conectar('localhost','root','Es1084734914','proyecto') # se conecta a la base de datos
        cur = conn.cursor() # cursor para ejecutar consultas
        cur.execute("SELECT * FROM tipo_gasto") 
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_tipo_gasto':row[0], 
                'nombre':row[1],
                'descripcion':row[2]
            }
            data.append(dato) # se agrega a la lista
        cur.close()
        conn.close()
        return jsonify({'tipo_gasto': data, 'mensaje': 'Lista De Tipo Gasto'})
    except Exception as ex:
        print(ex) # imprime el error
        return jsonify ({'mensaje': 'Error'})

# Ruta para registrar un nuevo tipo_gasto
@app.route("/registro_tipo_gasto", methods=['POST'])
def registro_tipo_gasto():
    try:
        data = request.get_json()
        nombre = data['nombre']
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO tipo_gasto (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
# Ruta para actualizar un tipo_gasto
@app.route("/actualizar_tipo_gasto/<codigo>", methods=["PUT"])
def actualizar_tipo_gasto(codigo):
    try:
        data = request.get_json()
        nombre = data['nombre']
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE tipo_gasto SET nombre= %s, descripcion= %s WHERE id_tipo_gasto= %s", 
                    (nombre, descripcion, codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar tipo_gasto
@app.route("/eliminar_tipo_gasto/<int:codigo>", methods=['DELETE'])
def eliminar_tipo_gasto(codigo):
    """
    Eliminar un tipo de gasto
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: tipo de gasto eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM tipo_gasto WHERE id_tipo_gasto = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


# ruta para estado
@app.route("/estado", methods=['GET'])
def estado():
    """
    Consulta de lista de estados
    ---
    responses:
      200:
        description: lista de estados
    """
    try:
        conn = conectar('localhost','root','Es1084734914','proyecto') # se conecta a la base de datos
        cur = conn.cursor() # cursor para ejecutar consultas
        cur.execute("SELECT * FROM estado") 
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_estado':row[0], 
                'nombre':row[1],
                'descripcion':row[2]
            }
            data.append(dato) # se agrega a la lista
        cur.close()
        conn.close()
        return jsonify({'estado': data, 'mensaje': 'Lista De Estado'})
    except Exception as ex:
        print(ex) # imprime el error
        return jsonify ({'mensaje': 'Error'})

# Ruta para registrar un nuevo estado
@app.route("/registro_estado", methods=['POST'])
def registro_estado():
    try:
        data = request.get_json()
        nombre = data['nombre']
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO estado (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar un estado
@app.route("/actualizar_estado/<codigo>", methods=["PUT"])
def actualizar_estado(codigo):
    try:
        data = request.get_json()
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE tipo_usuario SET descripcion= %s WHERE id_tipo_usuario= %s", 
                    (descripcion,codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar estado
@app.route("/eliminar_estado/<int:codigo>", methods=['DELETE'])
def eliminar_estado(codigo):
    """
    Eliminar un estado
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Estado eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM estado WHERE id_estado = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


# ruta de gasto
@app.route("/gasto", methods=['GET'])
def gasto():
    """
    Consulta de lista de gastos
    ---
    responses:
      200:
        description: lista de gastos
    """
    try:
        conn = conectar('localhost','root','Es1084734914','proyecto') # se conecta a la base de datos
        cur = conn.cursor() # cursor para ejecutar consultas
        cur.execute("SELECT * FROM gasto") 
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_gasto':row[0], 
                'fecha':row[1],
                'monto':row[2],
                'descripcion':row[3],
                'tipo_gasto':row[4]
            }
            data.append(dato) # se agrega a la lista
        cur.close()
        conn.close()
        return jsonify({'gasto': data, 'mensaje': 'Lista De Gasto'})
    except Exception as ex:
        print(ex) # imprime el error
        return jsonify ({'mensaje': 'Error'})

# Ruta para registrar un nuevo gasto
@app.route("/registro_gasto", methods=['POST'])
def registro_gasto():
    try:
        data = request.get_json()
        fecha = data['fecha']
        monto = data['monto']
        descripcion = data['descripcion']
        tipo_gasto = data['tipo_gasto']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO gasto (fecha, monto, descripcion, tipo_gasto) VALUES (%s, %s, %s, %s)", (fecha, monto, descripcion, tipo_gasto))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
# Ruta para actualizar un gasto
@app.route("/actualizar_gasto/<codigo>", methods=["PUT"])
def actualizar_gasto(codigo):
    try:
        data = request.get_json()
        fecha = data['fecha']
        monto = data['monto']
        descripcion = data['descripcion']
        tipo_gasto = data['tipo_gasto']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE gasto SET fecha=%s, monto=%s, descripcion= %s, tipo_gasto= %s WHERE id_gasto= %s" , 
                    (fecha,monto,descripcion,tipo_gasto,codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar gasto
@app.route("/eliminar_gasto/<int:codigo>", methods=['DELETE'])
def eliminar_gasto(codigo):
    """
    Eliminar un gasto
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Gasto eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM gasto WHERE id_gasto = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# ruta consultar usuario 
@app.route("/usuarios", methods=['GET'])
def usuarios():
    """
    Consulta de lista de usuarios
    ---
    responses:
      200:
        description: lista de usuarios
    """
    try:
        conn = conectar('localhost','root','Es1084734914','proyecto') # se conecta a la base de datos
        cur = conn.cursor() # cursor para ejecutar consultas
        cur.execute("SELECT * FROM usuario") 
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_usuario':row[0], 
                'nombre_completo':row[1], 
                'numero_documento':row[2], 
                'gmail':row[3], 
                'contrasena':row[4], 
                'tipo_usuario':row[5], 
                'tipo_documento':row[6], 
                'estado':row[7]
            }
            data.append(dato) # se agrega a la lista
        cur.close()
        conn.close()
        return jsonify({'usuario': data, 'mesaje': 'Lista De Usuario'})
    except Exception as ex:
        print(ex) # imprime el error
        return jsonify ({'mesaje': 'Error'})
    
# Ruta para registrar un nuevo usuario
@app.route("/registro_usuarios", methods=['POST'])
def registro_usuarios():

    try:
        data = request.get_json()
        nombre_completo = data['nombre_completo']
        numero_documento = data['numero_documento']
        gmail = data['gmail']
        contrasena = data['contrasena']
        tipo_usuario = data['tipo_usuario']
        tipo_documento = data['tipo_documento']
        estado = data['estado']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO usuario (nombre_completo, numero_documento, gmail, contrasena, tipo_usuario, tipo_documento, estado) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nombre_completo, numero_documento, gmail, contrasena, tipo_usuario, tipo_documento, estado))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
# Ruta para actualizar un usuario
@app.route("/actualizar_usuarios/<codigo>", methods=["PUT"])
def actualizar_usuarios(codigo):
    try:
        data = request.get_json()
        nombre_completo = data['nombre_completo']
        numero_documento = data['numero_documento']
        gmail = data['gmail']
        contrasena = data['contrasena']
        tipo_usuario = data['tipo_usuario']
        tipo_documento = data['tipo_documento']
        estado = data['estado']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE usuario SET nombre_completo= %s, numero_documento= %s, gmail= %s, contrasena= %s, tipo_usuario= %s, tipo_documento= %s, estado= %s WHERE id_usuario= %s", 
                    (nombre_completo, numero_documento, gmail, contrasena, tipo_usuario, tipo_documento, estado, codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar usuario
@app.route("/eliminar_usuarios/<int:codigo>", methods=['DELETE'])
def eliminar_usuarios(codigo):
    """Eliminar un usuario por su ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Usuario eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM usuario WHERE id_usuario = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# ruta de tipo_donante
@app.route("/tipo_donante", methods=['GET'])
def tipo_donante():
    """
    Consulta de lista de tipos de donante
    ---
    responses:
      200:
        description: lista de tipos de donante
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM tipo_donante")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'ID':row[0], 
                'descripcion':row[1]
            }

            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'tipo_donante': data, 'mensaje': 'Lista De tipo_Donante'})
    except Exception as ex:
        print(ex)
        return jsonify ({'Mensaje': 'Error'})
# Ruta para registrar un nuevo tipo_donante
@app.route("/registro_tipo_donante", methods=['POST'])
def registro_tipo_donante():
    try:
        data = request.get_json()
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO tipo_donante (descripcion) VALUES (%s)", (descripcion,))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
# Ruta para actualizar un tipo donante
@app.route("/actualizar_tipo_donante/<codigo>", methods=["PUT"])
def actualizar_tipo_donante(codigo):
    try:
        data = request.get_json()
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE tipo_usuario SET descripcion= %s WHERE id_tipo_usuario= %s", 
                    (descripcion,codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar tipo_donante
@app.route("/eliminar_tipo_donante/<int:codigo>", methods=['DELETE'])
def eliminar_tipo_donante(codigo):
    """
    Eliminar un tipo de donante por su ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Tipo de donante eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM tipo_donante WHERE id_tipo_donante = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})



@app.route("/donante", methods=['GET'])
def donante():
    """
    Consulta de lista de donantes
    ---
    responses:
      200:
        description: lista de donantes
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM donante")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_donante':row[0], 
                'nombre':row[1], 
                'telefono':row[2], 
                'gmail':row[3], 
                'direccion':row[4], 
                'estado':row[5], 
                'tipo_documento':row[6] , 
                'tipo_donante':row[7]
            }

            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'donante': data, 'mensaje': 'Lista De Donante'})
    except Exception as ex:
        print(ex)
        return jsonify ({'Mensaje': 'Error'})

# Ruta para registrar un nuevo donante
@app.route("/registro_donante", methods=['POST'])
def registro_donante():
    try:
        data = request.get_json()
        nombre = data['nombre']
        telefono = data['telefono']
        gmail = data['gmail']
        direccion = data['direccion']
        estado = data['estado']
        tipo_documento = data['tipo_documento']
        tipo_donante = data['tipo_donante']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO donante (nombre, telefono, gmail, direccion, estado, tipo_documento, tipo_donante) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nombre, telefono, gmail, direccion, estado, tipo_documento, tipo_donante))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar un donante
@app.route("/actualizar_donante/<codigo>", methods=["PUT"])
def actualizar_donante(codigo):
    try:
        data = request.get_json()
        nombre = data['nombre']
        telefono = data['telefono']
        gmail = data['gmail']
        direccion = data['direccion']
        estado = data['estado']
        tipo_documento = data['tipo_documento']
        tipo_donante = data['tipo_donante']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE donante SET nombre= %s, telefono= %s, gmail= %s, direccion= %s, estado= %s, tipo_documento= %s, tipo_donante= %s WHERE id_donante= %s", 
                    (nombre, telefono, gmail, direccion, estado, tipo_documento, tipo_donante, codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar donante
@app.route("/eliminar_donante/<int:codigo>", methods=['DELETE'])
def eliminar_donante(codigo):
    """
    Eliminar donante por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Donante eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM donante WHERE id_donante = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


# ruta de tipo_donacion
@app.route("/tipo_donacion", methods=['GET'])
def tipo_donacion():
    """
    Consulta de lista de tipos de donación
    ---
    responses:
      200:
        description: lista de tipos de donación
    """
    try:
        conn = conectar('localhost','root','Es1084734914','proyecto') # se conecta a la base de datos
        cur = conn.cursor() # cursor para ejecutar consultas
        cur.execute("SELECT * FROM tipo_donacion") 
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'codigo':row[0], 
                'descripcion':row[1]
            }
            data.append(dato) # se agrega a la lista
        cur.close()
        conn.close()
        return jsonify({'tipo_donacion': data, 'mensaje': 'Lista De Tipo Donacion'})
    except Exception as ex:
        print(ex) # imprime el error
        return jsonify ({'mensaje': 'Error'})
# Ruta para registrar un nuevo tipo_donacion
@app.route("/registro_tipo_donacion", methods=['POST'])
def registro_tipo_donacion():
    try:
        data = request.get_json()
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO tipo_donante (descripcion) VALUES (%s)", (descripcion,))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
# Ruta para actualizar un tipo donacion
@app.route("/actualizar_tipo_donacion/<codigo>", methods=["PUT"])
def actualizar_tipo_donacion(codigo):
    try:
        data = request.get_json()
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE tipo_usuario SET descripcion= %s WHERE id_tipo_usuario= %s", 
                    (descripcion,codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar tipo_donacion
@app.route("/eliminar_tipo_donacion/<int:codigo>", methods=['DELETE'])
def eliminar_tipo_donacion(codigo):
    """
    Eliminar tipo de donación por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Tipo de donación eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM tipo_donacion WHERE codigo = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


@app.route("/donacion", methods=['GET'])
def donacion():
    """
    Consulta de lista de donaciones
    ---
    responses:
      200:
        description: lista de donaciones
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM donacion")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_donante':row[0], 
                'cantidad_donada':row[1], 
                'fecha_donacion':row[2], 
                'forma_donacion':row[3], 
                'observaciones':row[4]
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'donacion': data, 'mensaje': 'Lista De donacion'})
    except Exception as ex:
        print(ex)
        return jsonify ({'Mensaje': 'Error'})
# Ruta para registrar un nueva donacion
@app.route("/registro_donacion", methods=['POST'])
def registro_donacion():
    try:
        data = request.get_json()
        cantidad_donada = data['cantidad_donada']
        fecha_donacion = data['fecha_donacion']
        forma_donacion = data['forma_donacion']
        observaciones = data['observaciones']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO donacion (cantidad_donada, fecha_donacion, forma_donacion, observaciones) VALUES (%s, %s, %s, %s)", (cantidad_donada, fecha_donacion, forma_donacion, observaciones))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar donacion
@app.route("/actualizar_donacion/<codigo>", methods=["PUT"])
def actualizar_donacion(codigo):
    try:
        data = request.get_json()
        cantidad_donada = data['cantidad_donada']
        fecha_donacion = data['fecha_donacion']
        forma_donacion = data['forma_donacion']
        observaciones = data['observaciones']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE donacion SET cantidad_donada= %s, fecha_donacion= %s, forma_donacion= %s, observaciones= %s WHERE id_donacion= %s", 
                    (cantidad_donada, fecha_donacion, forma_donacion, observaciones, codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar donacion
@app.route("/eliminar_donacion/<int:codigo>", methods=['DELETE'])
def eliminar_donacion(codigo):
    """
    Eliminar donación por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Donación eliminada
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM donacion WHERE id_donante = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


# ruta de donacion_has_tipo_donacion
@app.route("/donacion_has_tipo_donacion", methods=['GET'])
def donacion_has_tipo_donacion():
    """
    Consulta de lista de donacion_has_tipo_donacion
    ---
    responses:
      200:
        description: lista de donacion_has_tipo_donacion
    """
    try:
        conn = conectar('localhost','root','Es1084734914','proyecto') # se conecta a la base de datos
        cur = conn.cursor() # cursor para ejecutar consultas
        cur.execute("SELECT * FROM donacion_has_tipo_donacion") 
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'ID':row[0], 
                'donacion':row[1],
                'tipo_donacion':row[2]
            }
            data.append(dato) # se agrega a la lista
        cur.close()
        conn.close()
        return jsonify({'donacion_has_tipo_donacion': data, 'mensaje': 'Lista De donacion_has_tipo_donacion'})
    except Exception as ex:
        print(ex) # imprime el error
        return jsonify ({'mensaje': 'Error'})
# Ruta para registrar un nuevo donacion_has_tipo_donacion
@app.route("/registro_donacion_has_tipo_donacion", methods=['POST'])
def registro_donacion_has_tipo_donacion():
    try:
        data = request.get_json()
        donacion = data['donacion']
        tipo_donacion = data['tipo_donacion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO donacion_has_tipo_donacion (donacion, tipo_donacion) VALUES (%s, %s)", (donacion, tipo_donacion))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar una donacion_has_tipo_donacion
@app.route("/actualizar_donacion_has_tipo_donacion/<codigo>", methods=["PUT"])
def actualizar_donacion_has_tipo_donacion(codigo):
    try:
        data = request.get_json()
        donacion = data['donacion']
        tipo_donacion = data['tipo_donacion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE donacion_has_tipo_donacion SET donacion= %s, tipo_donacion= %s WHERE id_donacion= %s", 
                    (donacion, tipo_donacion, codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar donacion_has_tipo_donacion
@app.route("/eliminar_donacion_has_tipo_donacion/<int:codigo>", methods=['DELETE'])
def eliminar_donacion_has_tipo_donacion(codigo):
    """
    Eliminar donacion_has_tipo_donacion por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: donacion_has_tipo_donacion eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM donacion_has_tipo_donacion WHERE ID = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# ruta de certificado_donante
@app.route("/certificado_donante", methods=['GET'])
def certificado_donante():
    try:
        conn = conectar('localhost','root','Es1084734914','proyecto') # se conecta a la base de datos
        cur = conn.cursor() # cursor para ejecutar consultas
        cur.execute("SELECT * FROM certificado_donante") 
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_certificado':row[0], 
                'fecha':row[1],
                'firma_representante':row[2],
                'donante':row[3],
                'estado':row[4],
                'tipo_documento':row[5],
                'tipo_donante':row[6],
                'tipo_donacion':row[7]
            }
            data.append(dato) # se agrega a la lista
        cur.close()
        conn.close()
        return jsonify({'certificado_donante': data, 'mensaje': 'Lista De certificado_donante'})
    except Exception as ex:
        print(ex) # imprime el error
        return jsonify ({'mensaje': 'Error'})

# Ruta para registrar un nuevo certificado_donante
@app.route("/registro_certificado_donante", methods=['POST'])
def registro_certificado_donante():
    try:
        data = request.get_json()
        fecha = data['fecha']
        firma_representante = data['firma_representante']
        donante = data['donante']
        estado = data['estado']
        tipo_documento = data['tipo_documento']
        tipo_donante = data['tipo_donante']
        tipo_donacion = data['tipo_donacion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO certificado_donante (fecha, firma_representante, donante, estado, tipo_documento, tipo_donante, tipo_donacion) VALUES (%s, %s, %s, %s, %s, %s, %s)", (fecha, firma_representante, donante, estado, tipo_documento, tipo_donante, tipo_donacion))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar un certificado_donante
@app.route("/actualizar_certificado_donante/<codigo>", methods=["PUT"])
def actualizar_certificado_donante(codigo):
    try:
        data = request.get_json()
        fecha = data['fecha']
        firma_representante = data['firma_representante']
        donante = data['donante']
        estado = data['estado']
        tipo_documento = data['tipo_documento']
        tipo_donante = data['tipo_donante']
        tipo_donacion = data['tipo_donacion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE certificado_donante SET fecha= %s, firma_representante= %s, donante= %s, estado= %s, tipo_documento= %s, tipo_donante= %s, tipo_donacion= %s WHERE id_certificado= %s", 
                    (fecha, firma_representante, donante, estado, tipo_documento, tipo_donante, tipo_donacion, codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar certificado_donante
@app.route("/eliminar_certificado_donante/<int:codigo>", methods=['DELETE'])
def eliminar_certificado_donante(codigo):
    """
    Eliminar certificado_donante por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: certificado_donante eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM certificado_donante WHERE id_certificado = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


# ruta para categoria_producto
@app.route("/categoria_producto", methods=['GET'])
def categoria_producto():
    """
    Consulta de lista de categorias de producto
    ---
    responses:
      200:
        description: lista de categorias de producto
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM categoria_producto")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'codigo':row[0], 
                'descripcion':row[1]
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'categoria_producto': data, 'mensaje': 'Lista De categoria_producto'})
    except Exception as ex:
        print(ex)
        return jsonify ({'Mensaje': 'Error'})
# Ruta para registrar un nuevo categoria_producto
@app.route("/registro_categoria_producto", methods=['POST'])
def registro_categoria_producto():
    try:
        data = request.get_json()
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO categoria_producto (descripcion) VALUES (%s)", (descripcion,))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar una categoria_producto
@app.route("/actualizar_categoria_producto/<codigo>", methods=["PUT"])
def actualizar_categoria_producto(codigo):
    try:
        data = request.get_json()
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE tipo_usuario SET descripcion= %s WHERE id_tipo_usuario= %s", 
                    (descripcion,codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar categoria_producto
@app.route("/eliminar_categoria_producto/<int:codigo>", methods=['DELETE'])
def eliminar_categoria_producto(codigo):
    """
    Eliminar categoria_producto por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: categoria_producto eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM categoria_producto WHERE codigo = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


    # ruta para consultar subcategoria_producto
@app.route("/subcategoria_producto", methods=['GET'])
def subcategoria_producto():
    """
    Consulta de lista de subcategorias de producto
    ---
    responses:
      200:
        description: lista de subcategorias de producto
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM subcategoria_producto")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'codigo':row[0], 
                'descripcion':row[1],
                'categoria_producto':row[2]
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'subcategoria_producto': data, 'mensaje': 'Lista De subcategoria_producto'})
    except Exception as ex:
        print(ex)
        return jsonify ({'Mensaje': 'Error'})
# Ruta para registrar un nuevo subcategoria_producto
@app.route("/registro_subcategoria_producto", methods=['POST'])
def registro_subcategoria_producto():
    try:
        data = request.get_json()
        descripcion = data['descripcion']
        categoria_producto = data['categoria_producto']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO subcategoria_producto (descripcion, categoria_producto) VALUES (%s, %s)", (descripcion, categoria_producto))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar un subcategoria_producto
@app.route("/actualizar_subcategoria_producto/<codigo>", methods=["PUT"])
def actualizar_subcategoria_producto(codigo):
    try:
        data = request.get_json()
        descripcion = data['descripcion']
        categoria_producto = data['categoria_producto']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE subcategoria_producto SET descripcion= %s, categoria_producto= %s WHERE id_subcategoria= %s", 
                    (descripcion,categoria_producto,codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar subcategoria_producto
@app.route("/eliminar_subcategoria_producto/<int:codigo>", methods=['DELETE'])
def eliminar_subcategoria_producto(codigo):
    """
    Eliminar subcategoria_producto por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: subcategoria_producto eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM subcategoria_producto WHERE codigo = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


# ruta para fecha_vencimiento
@app.route("/fecha_vencimiento", methods=['GET'])
def fecha_vencimiento():
    """
    Consulta de lista de fechas de vencimiento
    ---
    responses:
      200:
        description: lista de fechas de vencimiento
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM fecha_vencimiento")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_fecha_vencimiento':row[0], 
                'fecha':row[1]
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'fecha_vencimiento': data, 'mensaje': 'Lista De fecha_vencimiento'})
    except Exception as ex:
        print(ex)
        return jsonify ({'Mensaje': 'Error'})
# Ruta para registrar un nueva fecha_vencimiento
@app.route("/registro_fecha_vencimiento", methods=['POST'])
def registro_fecha_vencimiento():
    try:
        data = request.get_json()
        fecha = data['fecha']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO fecha_vencimiento (fecha) VALUES (%s)", (fecha,))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar una fecha_vencimiento
@app.route("/actualizar_fecha_vencimiento/<codigo>", methods=["PUT"])
def actualizar_fecha_vencimiento(codigo):
    try:
        data = request.get_json()
        fecha = data['fecha']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE fecha_vencimiento SET fecha= %s WHERE id_fecha_vencimiento= %s", 
                    (fecha,codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar fecha_vencimiento
@app.route("/eliminar_fecha_vencimiento/<int:codigo>", methods=['DELETE'])
def eliminar_fecha_vencimiento(codigo):
    """
    Eliminar fecha_vencimiento por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: fecha_vencimiento eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM fecha_vencimiento WHERE id_fecha_vencimiento = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


# ruta para acta_vencimiento
@app.route("/acta_vencimiento", methods=['GET'])
def acta_vencimiento():
    """
    Consulta de lista de actas de vencimiento
    ---
    responses:
      200:
        description: lista de actas de vencimiento
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM acta_vencimiento")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_acta':row[0], 
                'fecha':row[1], 
                'descripcion':row[2]
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'acta_vencimiento': data, 'mensaje': 'Lista De acta_vencimiento'})
    except Exception as ex:
        print(ex)
        return jsonify ({'Mensaje': 'Error'})
# Ruta para registrar un nuevo acta_vencimiento
@app.route("/registro_acta_vencimiento", methods=['POST'])
def registro_acta_vencimiento():
    try:
        data = request.get_json()
        fecha = data['fecha']
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO acta_vencimiento (fecha, descripcion) VALUES (%s, %s)", (fecha, descripcion))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar una acta_vencimiento
@app.route("/actualizar_acta_vencimiento/<codigo>", methods=["PUT"])
def actualizar_acta_vencimiento(codigo):
    try:
        data = request.get_json()
        fecha = data['fecha']
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE acta_vencimiento SET fecha= %s, descripcion= %s WHERE id_acta= %s", 
                    (fecha, descripcion, codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar acta_vencimiento
@app.route("/eliminar_acta_vencimiento/<int:codigo>", methods=['DELETE'])
def eliminar_acta_vencimiento(codigo):
    """
    Eliminar acta_vencimiento por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: acta_vencimiento eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM acta_vencimiento WHERE id_acta = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


# ruta para bodega
@app.route("/bodega", methods=['GET'])
def bodega():
    """
    Consulta de lista de bodegas
    ---
    responses:
      200:
        description: lista de bodegas
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM bodega")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_bodega':row[0], 
                'nombre_bodega':row[1], 
                'capacidad':row[2], 
                'estado':row[3]
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'bodega': data, 'mensaje': 'Lista De bodega'})
    except Exception as ex:
        print(ex)
        return jsonify ({'Mensaje': 'Error'})
# Ruta para registrar un nueva bodega
@app.route("/registro_bodega", methods=['POST'])
def registro_bodega():
    try:
        data = request.get_json()
        nombre_bodega = data['nombre_bodega']
        capacidad = data['capacidad']
        estado = data['estado']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO bodega (nombre_bodega, capacidad, estado) VALUES (%s, %s, %s)", (nombre_bodega, capacidad, estado))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
# Ruta para actualizar una bodega
@app.route("/actualizar_bodega/<codigo>", methods=["PUT"])
def actualizar_bodega(codigo):
    try:
        data = request.get_json()
        nombre_bodega = data['nombre_bodega']
        capacidad = data['capacidad']
        estado = data['estado']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE bodega SET nombre_bodega= %s, capacidad= %s, estado= %s WHERE id_bodega= %s", 
                    (nombre_bodega, capacidad, estado, codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar bodega
@app.route("/eliminar_bodega/<int:codigo>", methods=['DELETE'])
def eliminar_bodega(codigo):
    """
    Eliminar bodega por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: bodega eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM bodega WHERE id_bodega = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
    
# ruta unidad_de_medida

@app.route("/unidad_de_medida", methods=['GET'])
def unidad_de_medida():
    
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM unidad_de_medida")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'codigo':row[0], 
                'nombre':row[1], 
                'cantidad':row[2]
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'unidad_de_medida': data, 'mensaje': 'Lista De unidad_de_medida'})
    except Exception as ex:
        print(ex)   
        return jsonify ({'Mensaje': 'Error'})

# Ruta para registrar un nueva unidad de medida
@app.route("/registro_unidad_de_medida", methods=['POST'])
def registro_unidad_de_medida():
    try:
        data = request.get_json()
        nombre = data['nombre']
        cantidad = data['cantidad']
        estado = data['estado']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO unidad_de_medida (nombre, cantidad, estado) VALUES (%s, %s, %s)", (nombre, cantidad, estado))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar una unidad de medida
@app.route("/actualizar_unidad_de_medida/<codigo>", methods=["PUT"])
def actualizar_unidad_de_medida(codigo):
    try:
        data = request.get_json()
        nombre = data['nombre']
        cantidad = data['cantidad']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE unidad_de_medida SET nombre= %s, cantidad= %s WHERE id_unidad_de_medida= %s", 
                    (nombre, cantidad, codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar unidad_de_medida
@app.route("/eliminar_unidad_de_medida/<int:codigo>", methods=['DELETE'])
def eliminar_unidad_de_medida(codigo):
    """
    Eliminar unidad_de_medida por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: unidad_de_medida eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM unidad_de_medida WHERE codigo = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})



# ruta para tipo_organizacion
@app.route("/tipo_organizacion", methods=['GET'])
def tipo_organizacion():
    """
    Consulta de lista de tipo_organizacion
    ---
    responses:
      200:
        description: lista de tipo_organizacion
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM tipo_organizacion")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_tipo_organizacion':row[0], 
                'nombre':row[1]
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'tipo_organizacion': data, 'mensaje': 'Lista De tipo_organizacion'})
    except Exception as ex:
        print(ex)   
        return jsonify ({'Mensaje': 'Error'})

# Ruta para registrar un nuevo tipo organizacion
@app.route("/registro_tipo_organizacion", methods=['POST'])
def registro_tipo_organizacion():
    try:
        data = request.get_json()
        nombre = data['nombre']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO tipo_organizacion (nombre) VALUES (%s)", (nombre,))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
# Ruta para actualizar un tipo_organizacion
@app.route("/actualizar_tipo_organizacion/<codigo>", methods=["PUT"])
def actualizar_tipo_organizacion(codigo):
    try:
        data = request.get_json()
        nombre = data['nombre']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE tipo_organizacion SET nombre= %s WHERE id_tipo_organizacion= %s", 
                    (nombre,codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar tipo_organizacion
@app.route("/eliminar_tipo_organizacion/<int:codigo>", methods=['DELETE'])
def eliminar_tipo_organizacion(codigo):
    """
    Eliminar tipo_organizacion por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: tipo_organizacion eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM tipo_organizacion WHERE id_tipo_organizacion = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
    
# ruta para tipo_entrega
@app.route("/tipo_entrega", methods=['GET'])
def tipo_entrega():
    """
    Consulta de lista de tipo_entrega
    ---
    responses:
      200:
        description: lista de tipo_entrega
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM tipo_entrega")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_tipo_entrega':row[0], 
                'nombre':row[1]
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'tipo_entrega': data, 'mensaje': 'Lista De tipo_entrega'})
    except Exception as ex:
        print(ex)   
        return jsonify ({'Mensaje': 'Error'})
# Ruta para registrar un nuevo tipo de entrega
@app.route("/registro_tipo_entrega", methods=['POST'])
def registro_tipo_entrega():
    try:
        data = request.get_json()
        nombre = data['nombre']
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO tipo_entrega (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar un tipo_entrega
@app.route("/actualizar_tipo_entrega/<codigo>", methods=["PUT"])
def actualizar_tipo_entrega(codigo):
    try:
        data = request.get_json()
        nombre = data['nombre']
        descripcion = data['descripcion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE tipo_entrega SET nombre= %s, descripcion= %s WHERE id_tipo_entrega= %s", 
                    (nombre, descripcion, codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar tipo_entrega
@app.route("/eliminar_tipo_entrega/<int:codigo>", methods=['DELETE'])
def eliminar_tipo_entrega(codigo):
    """
    Eliminar tipo_entrega por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: tipo_entrega eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM tipo_entrega WHERE id_tipo_entrega = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})



# ruta para organizacion
@app.route("/organizacion", methods=['GET'])
def organizacion():
    """
    Consulta de lista de organizacion
    ---
    responses:
      200:
        description: lista de organizacion
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM organizacion")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'codigo':row[0], 
                'descripcion':row[1], 
                'nombre':row[2], 
                'responsable':row[3], 
                'telefono':row[4], 
                'direccion':row[5], 
                'tipo_entrega':row[6], 
                'tipo_organizacion':row[7]
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'organizacion': data, 'mensaje': 'Lista De organizacion'})
    except Exception as ex:
        print(ex)   
        return jsonify ({'Mensaje': 'Error'})
    # Ruta para registrar un nueva organizacion
@app.route("/registro_organizacion", methods=['POST'])
def registro_organizacion():
    try:
        data = request.get_json()
        nombre = data['nombre']
        descripcion = data['descripcion']
        nombre = data['nombre']
        responsable = data['responsable']
        telefono = data['telefono']
        direccion = data['direccion']
        tipo_entrega = data['tipo_entrega']
        tipo_organizacion = data['tipo_organizacion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO organizacion (nombre, descripcion, responsable, telefono, direccion, tipo_entrega, tipo_organizacion) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nombre, descripcion, responsable, telefono, direccion, tipo_entrega, tipo_organizacion))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar organizacion
@app.route("/actualizar_organizacion/<codigo>", methods=["PUT"])
def actualizar_organizacion(codigo):
    try:
        data = request.get_json()
        codigo = data['codigo']
        descripcion = data['descripcion']
        nombre = data['nombre']
        responsable = data['responsable']
        telefono = data['telefono']
        direccion = data['direccion']
        tipo_entrega = data['tipo_entrega']
        tipo_organizacion = data['tipo_organizacion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE organizacion SET nombre= %s, descripcion= %s, responsable= %s, telefono= %s, direccion= %s, tipo_entrega= %s, tipo_organizacion= %s WHERE codigo= %s", 
                    (nombre, descripcion, responsable, telefono, direccion, tipo_entrega, tipo_organizacion, codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar organizacion
@app.route("/eliminar_organizacion/<int:codigo>", methods=['DELETE'])
def eliminar_organizacion(codigo):
    """
    Eliminar organizacion por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: organizacion eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM organizacion WHERE codigo = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
    
# ruta para movimiento_producto
@app.route("/movimiento_producto", methods=['GET'])
def movimiento_producto():
    """
    Consulta de lista de movimiento_producto
    ---
    responses:
      200:
        description: lista de movimiento_producto
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM movimiento_producto")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id':row[0], 
                'movimiento':row[1], 
                'cantidad':row[2], 
                'observacion':row[3], 
                'tipo_donacion':row[4], 
                'organizacion':row[5], 
                'tipo_organizacion':row[6], 
                'tipo_entrega':row[7] 
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'movimiento_producto': data, 'mensaje': 'Lista De movimiento_producto'})
    except Exception as ex:
        print(ex)   
        return jsonify ({'Mensaje': 'Error'})
# Ruta para registrar un nuevo movimiento_producto
@app.route("/registro_movimiento_producto", methods=['POST'])
def registro_movimiento_producto():
    try:
        data = request.get_json()
        movimiento = data['movimiento']
        cantidad = data['cantidad']
        observacion = data['observacion']
        tipo_donacion = data['tipo_donacion']
        organizacion = data['organizacion']
        tipo_organizacion = data['tipo_organizacion']
        tipo_entrega = data['tipo_entrega']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO movimiento_producto (movimiento, cantidad, observacion, tipo_donacion, organizacion, tipo_organizacion, tipo_entrega) VALUES (%s, %s, %s, %s, %s, %s, %s)", (movimiento, cantidad, observacion, tipo_donacion, organizacion, tipo_organizacion, tipo_entrega))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar movimiento_producto
@app.route("/actualizar_movimiento_producto/<id>", methods=["PUT"])
def actualizar_movimiento_producto(id):
    try:
        data = request.get_json()
        movimiento = data['movimiento']
        cantidad = data['cantidad']
        observacion = data['observacion']
        tipo_donacion = data['tipo_donacion']
        organizacion = data['organizacion']
        tipo_organizacion = data['tipo_organizacion']
        tipo_entrega = data['tipo_entrega']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE movimiento_producto SET movimiento= %s, cantidad= %s, observacion= %s, tipo_donacion= %s, organizacion= %s, tipo_organizacion= %s, tipo_entrega= %s WHERE id= %s", 
                    (movimiento, cantidad, observacion, tipo_donacion, organizacion, tipo_organizacion, tipo_entrega, id))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para eliminar movimiento_producto
@app.route("/eliminar_movimiento_producto/<int:codigo>", methods=['DELETE'])
def eliminar_movimiento_producto(codigo):
    """
    Eliminar movimiento_producto por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: movimiento_producto eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM movimiento_producto WHERE id = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
# ruta para producto
@app.route("/producto", methods=['GET'])
def producto():
    
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM producto")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_producto':row[0], 
                'nombre':row[1], 
                'descripcion':row[2], 
                'cantidad':row[3], 
                'codigo_barras':row[4], 
                'stock':row[5], 
                'stock_maximo':row[6], 
                'categoria_producto':row[7],
                'subcategoria_producto':row[8],
                'estado':row[9],
                'unidad_de_medida':row[10],
                'acta_vencimiento':row[11],
                'movimiento_producto':row[12],
                'tipo_donacion':row[13],
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'movimiento_producto': data, 'mensaje': 'Lista De movimiento_producto'})
    except Exception as ex:
        print(ex)   
        return jsonify ({'Mensaje': 'Error'})

# Ruta para registrar un nuevo producto
@app.route("/registro_producto", methods=['POST'])
def registro_producto():
    try:
        data = request.get_json()
        nombre = data['nombre']
        descripcion = data['descripcion']
        cantidad = data['cantidad']
        codigo_barras = data['codigo_barras']
        stock = data['stock']
        stock_maximo = data['stock_maximo']
        stock_minimo = data['stock_minimo']
        categoria_producto = data['categoria_producto']
        subcategoria_producto = data['subcategoria_producto']
        estado = data['estado']
        unidad_de_medida = data['unidad_de_medida']
        acta_vencimiento = data['acta_vencimiento']
        tipo_donacion = data['tipo_donacion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO producto (nombre, descripcion, cantidad, codigo_barras, stock, stock_maximo, stock_minimo, categoria_producto, subcategoria_producto, estado, unidad_de_medida, acta_vencimiento, tipo_donacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nombre, descripcion, cantidad, codigo_barras, stock, stock_maximo, stock_minimo, categoria_producto, subcategoria_producto, estado, unidad_de_medida, acta_vencimiento, tipo_donacion))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar producto
@app.route("/actualizar_producto/<id>", methods=["PUT"])
def actualizar_producto(id):
    try:
        data = request.get_json()
        nombre = data['nombre']
        descripcion = data['descripcion']
        cantidad = data['cantidad']
        codigo_barras = data['codigo_barras']
        stock = data['stock']
        stock_maximo = data['stock_maximo']
        stock_minimo = data['stock_minimo']
        categoria_producto = data['categoria_producto']
        subcategoria_producto = data['subcategoria_producto']
        estado = data['estado']
        unidad_de_medida = data['unidad_de_medida']
        acta_vencimiento = data['acta_vencimiento']
        tipo_donacion = data['tipo_donacion']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE producto SET nombre= %s, descripcion= %s, cantidad= %s, codigo_barras= %s, stock= %s, stock_maximo= %s, stock_minimo= %s, categoria_producto= %s, subcategoria_producto= %s, estado= %s, unidad_de_medida= %s, acta_vencimiento= %s, tipo_donacion= %s WHERE id_producto= %s", 
                    (nombre, descripcion, cantidad, codigo_barras, stock, stock_maximo, stock_minimo, categoria_producto, subcategoria_producto, estado, unidad_de_medida, acta_vencimiento, tipo_donacion, id))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
# Ruta para eliminar producto
@app.route("/eliminar_producto/<int:codigo>", methods=['DELETE'])
def eliminar_producto(codigo):
    """
    Eliminar producto por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: producto eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM producto WHERE id_producto = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    

# ruta para producto_has_donante
@app.route("/producto_has_donante", methods=['GET'])
def producto_has_donante():
    """
    Consulta de lista de producto_has_donante
    ---
    responses:
      200:
        description: lista de producto_has_donante
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM producto_has_donante")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'ID':row[0], 
                'donante':row[1], 
                'tipo_documento':row[2], 
                'tipo_donante':row[3], 
                'producto':row[4], 
                'categoria_producto':row[5], 
                'subcategoria_producto':row[6]
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'producto_has_donante': data, 'mensaje': 'Lista De producto_has_donante'})
    except Exception as ex:
        print(ex)   
        return jsonify ({'Mensaje': 'Error'})

# Ruta para registrar un nuevo producto_has_donante
@app.route("/registro_producto_has_donante", methods=['POST'])
def registro_producto_has_donante():
    try:
        data = request.get_json()
        donante = data['donante']
        tipo_documento = data['tipo_documento']
        tipo_donante = data['tipo_donante']
        producto = data['producto']
        categoria_producto = data['categoria_producto']
        subcategoria_producto = data['subcategoria_producto']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("INSERT INTO donacion_has_tipo_donacion (donante, tipo_donante, producto, categoria_producto, subcategoria_producto) VALUES (%s, %s, %s, %s, %s)", (donante, tipo_donante, producto, categoria_producto, subcategoria_producto))
        conn.commit()  # Para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar producto_has_donante
@app.route("/actualizar_producto_has_donante/<id>", methods=["PUT"])
def actualizar_producto_has_donante(id):
    try:
        data = request.get_json()
        donante = data['donante']
        tipo_documento = data['tipo_documento']
        tipo_donante = data['tipo_donante']
        producto = data['producto']
        categoria_producto = data['categoria_producto']
        subcategoria_producto = data['subcategoria_producto']
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("UPDATE producto_has_donante SET donante= %s, tipo_documento= %s, tipo_donante= %s, producto= %s, categoria_producto= %s, subcategoria_producto= %s WHERE id= %s", 
                    (donante, tipo_documento, tipo_donante, producto, categoria_producto, subcategoria_producto, id))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


# Ruta para eliminar producto_has_donante
@app.route("/eliminar_producto_has_donante/<int:codigo>", methods=['DELETE'])
def eliminar_producto_has_donante(codigo):
    """
    Eliminar producto_has_donante por ID
    ---
    parameters:
      - name: codigo
        in: path
        required: true
        type: integer
    responses:
      200:
        description: producto_has_donante eliminado
    """
    try:
        conn = conectar('localhost', 'root', 'Es1084734914', 'proyecto')
        cur = conn.cursor()
        cur.execute("DELETE FROM producto_has_donante WHERE ID = %s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


if __name__ == '__main__':
    app.run(debug=True)