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
    conn = pymysql.Connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset='utf8mb4')
    return conn

# ruta consultar tipo_usuario generales
@app.route("/", methods=['GET'])
def consulta_general():
    """
    consulta general del banco de alimento
    ---
    responses:
      200:
        description: lista de registro
    """
    try:
        conn = conectar('localhost','root','Es1084734914','proyecto') # se conecta a la base de datos
        cur = conn.cursor() # cursor para ejecutar consultas
        cur.execute("SELECT * FROM usuario") 
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {'id_usuario':row[0], 'nombre_completo':row[1], 'numero_documento':row[2], 'gmail':row[3], 'contrasena':row[4], 'tipo_usuario':row[5], 'tipo_documento':row[6], 'estado':row[7]}
            data.append(dato) # se agrega a la lista
        cur.close()
        conn.close()
        return jsonify({'usuario': data, 'mesaje': 'Lista De Usuario'})
    except Exception as ex:
        print(ex) # imprime el error
        return jsonify ({'mesaje': 'Error'})
        
        
@app.route("/consultar_tipo_usuario/<int:codigo>", methods=['GET'])
def consultar_tipo_usuario(codigo):
    """
    consulta general por id
    ---
    parameters:
      codigo:
        description: ID del tipo de usuario
        in: query
        type: integer
    responses:
      200:
        description: Consulta realizada con éxito
    """
    try:
        conn = conectar('localhost','root','Es1084734914','proyecto') 
        cur = conn.cursor()
        cur.execute(f"select * from tipo_usuario where id_tipo_usuario = '{codigo}'") # consulta a la tabla tipo_usuario
        datos = cur.fetchone() # obtiene todos los datos
        cur.close() # cierra el cursor
        conn.close() # cierra la conexion
        if datos:
            datos = {'id_tipo_usuario':datos[0], 'descripcion':datos[1]}
            return jsonify(datos)
        else:
            return jsonify({'mensaje':'No se encontraron resultados'}),
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error en la consulta'}),
    
@app.route("/tipo_donante", methods=['GET'])
def donante():
    """
    consulta de tipo_donante
    ---
    responses:
      200:
        description: lista de registro
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM tipo_donante")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {'ID':row[0], 'descripcion':row[1]}
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'tipo_donante': data, 'mensaje': 'Lista De tipo_Donante'})
    except Exception as ex:
        print(ex)
        return jsonify ({'Mensaje': 'Error'})
    


@app.route("/donante", methods=['GET'])
def donante():
    """
    consulta de donante
    ---
    responses:
      200:
        description: lista de registro
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM donante")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {'id_donante':row[0], 'nombre':row[1], 'telefono':row[2], 'gmail':row[3], 'direccion':row[4], 'estado':row[5], 'tipo_documento':row[6] , 'tipo_documento':row[7]}
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'donante': data, 'mensaje': 'Lista De Donante'})
    except Exception as ex:
        print(ex)
        return jsonify ({'Mensaje': 'Error'})
    
    
@app.route("/donacion", methods=['GET'])
def donacion():
    """
    consulta de donacion
    ---
    responses:
      200:
        description: lista de registro
    """
    try:
        conn= conectar('localhost','root','Es1084734914','proyecto')
        cur= conn.cursor()
        cur.execute("SELECT * FROM donacion")
        datos= cur.fetchall()
        data = []
        for row in datos:
            dato = {'id_donante':row[0], 'cantidad_donada':row[1], 'fecha_donacion':row[2], 'forma_donacion':row[3], 'observaciones':row[4]}
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify ({'donacion': data, 'mensaje': 'Lista De donacion'})
    except Exception as ex:
        print(ex)
        return jsonify ({'Mensaje': 'Error'})
if __name__ == '__main__':
    app.run(debug=True)