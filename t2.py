from flask import Flask, jsonify, abort
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return 'Server is running!'

@app.route('/kenttä/<kodi>', methods=['GET'])
def lentokenta(kodi):
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='mimmasum',
            password='Mitoina33',
            autocommit=True
        )
        with connection.cursor() as cursor:
            query = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
            cursor.execute(query, (kodi.upper(),))
            result = cursor.fetchone()

        connection.close()

        if result:
            return jsonify({
                "ICAO": result[0],
                "Name": result[1],
                "Municipality": result[2]
            })
        else:
            abort(404, description=f"Airport with ICAO code {kodi} not found.")

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)
