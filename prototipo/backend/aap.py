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

@app.route("/consultar_tipo_usuario", methods=['GET'])
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
        conn = conectar('localhost','root','Es1084734914','proyecto') # se conecta a la base de datos
        cur = conn.cursor() # cursor para ejecutar consultas
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
    
    

if __name__ == '__main__':
    app.run(debug=True)