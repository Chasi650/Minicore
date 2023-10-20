from flask import Flask, render_template, request
import mysql.connector 

app = Flask(__name__, template_folder='template')

# Configura los parámetros de la base de datos
db_config = {
    'host': '139.144.19.100:3306',
    'user': 'pablo',
    'password': '12345adcvayne',
    'database': 'minicore'
}

# Función para conectarse a la base de datos
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error en la conexión a la base de datos: {err}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/comisiones', methods=['POST'])
def mostrar_comisiones():
    fecha_inicio = request.form.get('fecha_inicio')
    fecha_fin = request.form.get('fecha_fin')

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT usuarios.nombre, usuarios.apellido, SUM(ventas.monto) AS total_ventas FROM ventas JOIN usuarios ON ventas.idusuario = usuarios.idusuarios WHERE ventas.fecha BETWEEN %s AND %s GROUP BY usuarios.nombre, usuarios.apellido", (fecha_inicio, fecha_fin))
        comision = cursor.fetchall()
        cursor.close()
        connection.close()
        print(comision)
        return render_template('comision.html', comision=comision)
    else:
        return "Error en la conexión a la base de datos."

@app.route('/buscar_comisiones', methods=['GET'])
def mostrar_formulario_busqueda():
    return render_template('formulario_busqueda.html')

if __name__ == '__main__':
    app.secret_key = "pinchellave"
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
