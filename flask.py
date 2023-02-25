# pip insatll Flask

# from flask import Flask 
# or

from flask import Flask ,request,render_template

# render_template :>  searching template like .html file if not found showing 404 

# or
# import request


# requ handel all req like post get delete....


# API  application programming interfacing 

# IDE integrating developement invirnment (like vscode , pycharme)
app = Flask(__name__)
# __name__ private varialble alrady present in python


# Route
# route means url which rout we can run rode
@app.route("/")
def main_page():

    return "Hello Welcome"

@app.rout("/welcome_page")
def welcome():
    return "Welcome You in home Page"

# 

@app.rout('/demo', method=['POST'])
def math_operation():
    if(request.method=='POST'):
        operation = request.json['opration']
        num1= request.json['num1']
        num2 = request.jso['num2']
        if operation=="multiply":
            result = num1*num2
        elif operation=="add":
            result = num1+num2
        elif operation=="division":
            result = num1/num2
        else:
            result = num1-num2
        # r = render_template('index.html')
        return "The Ope is {} and the result is {}".formate(operation,result)



#Flask default port 5000

if __name__=="__main__":
	app.run(host="0.0.0.0", port=5000)
    
