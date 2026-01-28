from flask import Flask, jsonify, request

app = Flask(__name__) # Instance of Flask
# http://127.0.0.1:5000/
@app.route("/", methods=["GET"])
def index():
    return "Welcome to Flask Framework"

# http://127.0.0.1:5000/hello
@app.route("/hello", methods=["GET"])
def hello():
    return "Hello world from Flask"

# http://127.0.0.1:5000/cohort-63

@app.route("/cohort-63", methods=["GET"])
def cohort63():
    student_list = ["Robert", "Barney", "lous", "Lemuel", "Reece", "John", "Angel"]
    return student_list 

# http://127.0.0.1:5000/cohort-99
@app.route("/cohort-99", methods=["GET"])
def cohort99():
    student_list = ["Pam", "Dwight", "Micheal", "Angela"]
    return student_list

@app.route("/contact", methods=["GET"])
def contact():
    information = {
        "email": "rrpieces86@gmail.com",
        "phone": "610 1268654"
    }
    return information

@app.route("/course-information", methods=["GET"])
def course_information():
    course_data = {
        "title": "Introduction Web API with Flask",
        "duration": "4 sessions",
        "level": "Beginner"
    }
    return course_data

# path paramater
#is a dynamic part of the url used to identify a specific item or resource within a api

@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
    print(f"this is the name {name}")
    return jsonify({"message": "hello"})


products = [
    {"_id": 1,
     "title": "Nintendo Switch",
      "price": 999.99,
       "category": "electronics",
        "image": "https://picsum.photos/seed/1/300/300"
    },
    {
        "_id": 2,
        "title": "smart refrigerator",
        "price": 999.99,
        "category": "kitchen",
        "image": "https://picsum.photos/seed/2/300/300"
    },
    {
        "_id": 3,
        "title": "bluetooth speaker",
        "price": 79.99,
        "category": "electronics",
        "image": "https://picsum.photos/seed/3/300/300"
    },
]


@app.route("/api/products", methods=["GET"])
def product_list():
    return jsonify({
        "success": True,
        "message": "Products retrieved successfully",
        "products": products
    })

# GET api/products/3
@app.route("/api/products/<int:product_id>")
def get_product_by_id(product_id):
    for product in products:
        if product["_id"] == product_id:
            return jsonify({
               "success": True,
               "message": "Product retrieved successfully",
               "data": product 
            }), 200 # ok
    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404

# POST api/products
@app.route("/api/products", methods=["POST"])
def create_products():
    new_product = request.get_json()
    print(new_product)
    products.append(new_product)
    return jsonify({
        "success": True,
        "message": "product sucessfully created",
        "data": new_product

    })
    return "working on it/POST"


coupons_data = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKEY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]
@app.route("/coupons", methods=["GET"])
def coupons():
    return coupons_data


@app.route("/coupons/count", methods=["GET"])
def count():
 
    count = (len(coupons_data))
    return {"coupons-count": count}

@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()
    print(new_coupon)
    coupons_data.append(new_coupon)
    return jsonify({
        "success": True,
        "message": "coupon created!",
        "data": new_coupon

    })
app.route("/api/coupons/<int:coupon_id>")
def get_coupon_by_id(coupon_id):
    for coupon in coupons_data:
        if coupon["_id"] == coupon_id:
            return jsonify({
                "success": True,
                "message": "coupon retrieved",
                "data": coupon
            }), 200
        return jsonify({
            "success": False,
            "message": "product not found"
        }), 404


if __name__ == "__main__":
    app.run(debug=True)
# When this file is run directly: __name__ == "__main__"
# When this file is run directly: __name__ == "server.py" 
