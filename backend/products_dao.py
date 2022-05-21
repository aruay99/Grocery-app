#Data Access Object
from sql_connection import get_sql_connection

def get_all_products(connection):


    cursor = connection.cursor() #allows to execute the queries
    query = "(select products.product_id, products.name_p, products.uom_id, products.price_per_unit, uom.uom_name  from  products inner join uom  on products.uom_id = uom.uom_id)"


    cursor.execute(query)

    response = []

    for (product_id, name_p, uom_id, price_per_unit, uom_name) in cursor:

        response.append({
            'product_id':product_id,
            'name':name_p,
            'uom_id':uom_id,
            'price_per_unit':price_per_unit,
            'uom_name':uom_name}
        )


    return response

def inser_new_product(connection, product):
    cursor = connection.cursor()
    query = "insert into products (name_p, uom_id, price_per_unit) values (%s, %s , %s)"
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid #shows us the id of last thing inserted

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("delete from products where product_id =" + str(product_id))
    cursor.execute(query)
    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    # print(inser_new_product(connection, {
    #     'product_name': 'cabbage',
    #     'uom_id' : '1',
    #     'price_per_unit': '1.90'
    #
    # }))

    print(delete_product(connection, 13))

