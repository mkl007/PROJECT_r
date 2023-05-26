# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route('/api/data', methods=['GET'])
# def get_data():
#     data = {'message': 'Hola desde Flask',
#             'name': 'Maikel'}
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, request
from DB.db import conn, cursor

app = Flask(__name__)

# Ruta para obtener todos los registros
@app.route('/api/data', methods=['GET'])
def get_data():

    cursor.execute('SELECT * FROM Usuarios')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

# Ruta para crear un nuevo registro
@app.route('/api/data', methods=['POST'])
def create_data():
    data = request.get_json()
    cursor.execute('INSERT INTO Usuarios (name, email, password) VALUES (?, ?, ?)', (data['maiekl'], data['maikel@maikel.com', data['password']]))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Registro creado'})

# # Ruta para actualizar un registro existente
# @app.route('/api/data/<int:id>', methods=['PUT'])
# def update_data(id):
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     data = request.get_json()
#     cursor.execute('UPDATE tablename SET column1 = ?, column2 = ? WHERE id = ?', (data['column1'], data['column2'], id))
#     conn.commit()
#     conn.close()
#     return jsonify({'message': 'Registro actualizado'})

# # Ruta para eliminar un registro existente
# @app.route('/api/data/<int:id>', methods=['DELETE'])
# def delete_data(id):
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM tablename WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()
#     return jsonify({'message': 'Registro eliminado'})

if __name__ == '__main__':
    app.run(debug=True)
