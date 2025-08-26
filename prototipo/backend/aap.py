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
    consulta general tipo de usuario
    ---
    responses:
      200:
        description: lista de registro
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


# ruta de tipo_documento
@app.route("/tipo_documento", methods=['GET'])
def tipo_documento():
    """
    consulta general tipo de documento
    ---
    responses:
      200:
        description: lista de registro
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

# ruta tipo_gasto
@app.route("/tipo_gasto", methods=['GET'])
def tipo_gasto():
    """
    consulta general tipo de gasto
    ---
    responses:
      200:
        description: lista de registro
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


# ruta para estado
@app.route("/estado", methods=['GET'])
def estado():
    """
    consulta general estado
    ---
    responses:
      200:
        description: lista de registro
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

# ruta de gasto
@app.route("/gasto", methods=['GET'])
def gasto():
    """
    consulta general tipo de gasto
    ---
    responses:
      200:
        description: lista de registro
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


# ruta consultar usuario generales
@app.route("/usuario", methods=['GET'])
def usuario():
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
        cur.execute("SELECT * FROM tipo_usuario WHERE id_tipo_usuario = %s", (codigo,)) # consulta a la tabla tipo_usuario
        datos = cur.fetchone() # obtiene todos los datos
        cur.close() # cierra el cursor
        conn.close() # cierra la conexion
        if datos:
            datos = {
                'id_tipo_usuario':datos[0],
                'descripcion':datos[1]
            }
            return jsonify(datos)
        else:
            return jsonify({'mensaje':'No se encontraron resultados'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error en la consulta'})

@app.route("/tipo_donante", methods=['GET'])
def tipo_donante():
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
    
    
# ruta de tipo_donacion
@app.route("/tipo_donacion", methods=['GET'])
def tipo_donacion():
    """
    consulta general tipo de donacion
    ---
    responses:
      200:
        description: lista de registro
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


# ruta de donacion_has_tipo_donacion
@app.route("/donacion_has_tipo_donacion", methods=['GET'])
def donacion_has_tipo_donacion():
    """
    consulta general donacion_has_tipo_donacion
    ---
    responses:
      200:
        description: lista de registro
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

# ruta de certificado_donante
@app.route("/certificado_donante", methods=['GET'])
def certificado_donante():
    """
    consulta general certificado_donante
    ---
    responses:
      200:
        description: lista de registro
    """
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


# ruta para categoria_producto
@app.route("/categoria_producto", methods=['GET'])
def categoria_producto():
    """
    consulta de categoria_producto
    ---
    responses:
      200:
        description: lista de registro
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

    # ruta para subcategoria_producto
@app.route("/subcategoria_producto", methods=['GET'])
def subcategoria_producto():
    """
    consulta de subcategoria_producto
    ---
    responses:
      200:
        description: lista de registro
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


# ruta para fecha_vencimiento
@app.route("/fecha_vencimiento", methods=['GET'])
def fecha_vencimiento():
    """
    consulta de fecha_vencimiento
    ---
    responses:
      200:
        description: lista de registro
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

# ruta para acta_vencimiento
@app.route("/acta_vencimiento", methods=['GET'])
def acta_vencimiento():
    """
    consulta de acta_vencimiento
    ---
    responses:
      200:
        description: lista de registro
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
    


# ruta para bodega
@app.route("/bodega", methods=['GET'])
def bodega():
    """
    consulta de bodega
    ---
    responses:
      200:
        description: lista de registro
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
    
# ruta unidad_de_medida

@app.route("/unidad_de_medida", methods=['GET'])
def unidad_de_medida():
    """
    consulta de unidad_de_medida
    ---
    responses:
      200:
        description: lista de registro
    """
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

# ruta para tipo_organizacion
@app.route("/tipo_organizacion", methods=['GET'])
def tipo_organizacion():
    """
    consulta de tipo_organizacion
    ---
    responses:
      200:
        description: lista de registro
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
    
# ruta para tipo_entrega
@app.route("/tipo_entrega", methods=['GET'])
def tipo_entrega():
    """
    consulta de tipo_entrega
    ---
    responses:
      200:
        description: lista de registro
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


# ruta para organizacion
@app.route("/organizacion", methods=['GET'])
def organizacion():
    """
    consulta de organizacion
    ---
    responses:
      200:
        description: lista de registro
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
    
# ruta para movimiento_producto
@app.route("/movimiento_producto", methods=['GET'])
def movimiento_producto():
    """
    consulta de movimiento_producto
    ---
    responses:
      200:
        description: lista de registro
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
    
# ruta para producto
@app.route("/producto", methods=['GET'])
def producto():
    """
    consulta de producto
    ---
    responses:
      200:
        description: lista de registro
    """
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

# ruta para producto_has_donante

@app.route("/producto_has_donante", methods=['GET'])
def producto_has_donante():
    """
    consulta de producto_has_donante
    ---
    responses:
      200:
        description: lista de registro
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
    









if __name__ == '__main__':
    app.run(debug=True)