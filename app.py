from flask import Flask, jsonify, request

app = Flask(__name__)


purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido 1',
        'items': [
            {
                'id': 1,
                'description': 'Item de compra 1',
                'price': 20.99
            }        
        ],

    },

    {
        'id': 2,
        'description': 'Pedido 27',
        'items': [
            {
                'id': 2,
                'description': 'Item de compra 10',
                'price': 50.99
            }  
        ],

    },

    {
        'id': 3,
        'description': 'Pedido 17',
        'items': [
            {
                'id': 3,
                'description': 'Item de compra 12',
                'price': 10.99
            }  
        ]
    }
]


@app.route('/')
def home():
    return 'Hello World'


@app.route('/purchase_orders')
def get_purchase_orders():
    return jsonify(purchase_orders)


@app.route('/purchase_orders/<int:id>')
def get_purchase_orders_by_id(id):
    for order in purchase_orders:
        if id == order['id']:
            return jsonify(order)
    return f'ERRO 404! Pedido não encontrado. ---'


@app.route('/purchase_orders',methods=['POST'])
def create_purchase_order():
    request_data = request.get_json()

    purchase_order = {
        'id': request_data['id'],
        'description': request_data['description'],
        'items': []
    }

    purchase_orders.append(purchase_order)

    return jsonify(purchase_order)


@app.route('/purchase_orders/<int:id>/items')
def get_purchase_items_by_id(id):
    for order in purchase_orders:
        if id == order['id']:
            return jsonify(order['items'])
    return f'ERRO 404! Pedido não encontrado. ---'


@app.route('/purchase_orders/<int:id>/items', methods=['POST'])
def create_purchase_items_by_id(id):
    req_data = request.get_json()
    for order in purchase_orders:
        if id == order['id']:
            order['items'].append({
                'id': req_data['id'],
                'description': req_data['description'],
                'price': req_data['price']
            })
            return jsonify(order)
    return f'ERRO 404! Pedido não encontrado. ---'


app.run(port=5000)