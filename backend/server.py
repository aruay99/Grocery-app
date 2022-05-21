from flask import Flask
from flask import request
from flask import jsonify
import products_dao
from sql_connection import get_sql_connection
import uom_dao
import json

connection =get_sql_connection()

app = Flask(__name__)
@app.route('/getProducts', methods =['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products) #converts into json
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUOM', methods =['GET'])
def get_uoms():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods = ['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response= jsonify({
        'product_id':return_id

    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/insertProduct', methods = ['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.inser_new_product(connection,request_payload)
    response = jsonify({
        'product_id': product_id

    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ =="__main__" :
    print("Starting Python Flask server for grocery store management system")
    app.run()

