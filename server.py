from flask import Flask

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
@app.route("/coupons", methods=["GET"])
def coupons():
    coupons_data = [
        {"_id": 1, "code": "WELCOME10", "discount": 10},
        {"_id": 2, "code": "SPOOKEY25", "discount": 25},
        {"_id": 3, "code": "VIP50", "discount": 50}
    ]
    return coupons_data
@app.route("/coupons/count", methods=["GET"])
def count():
    count = (len(coupons_data))
    return count

if __name__ == "__main__":
    app.run(debug=True)
# When this file is run directly: __name__ == "__main__"
# When this file is run directly: __name__ == "server.py" 
