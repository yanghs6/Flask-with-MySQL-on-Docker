from flask import Flask
from flask.templating import render_template

from mydao import MyEmpDao


app = Flask(__name__)
# empDao = MyEmpDao("db", "root2", "root2", "flask", 3306)
empDao = MyEmpDao("db", "customUser", "mysql", "flask", 3306)

# ####################
# # https://medium.com/analytics-vidhya/docker-docker-compose-flask-app-8527356aacd5
# # Flask app
# CORS(app)
# resources = {r"/api/*": {"origins": "*"}}
# app.config["CORS_HEADERS"] = "Content-Type"
# app.config['JSON_SORT_KEYS'] = False
# ####################

@app.route("/")
def hello_world():
    emp_list = empDao.getEmps()
    # emp_list = [{"empno":"123", "name":"kim", "department":"IT", "phone":"10-1234-5678"}]

    return render_template("emp01.html", emp_list=emp_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    