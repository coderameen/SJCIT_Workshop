from flask import Flask,render_template,request,redirect

#initiallize the app
app = Flask(__name__)

#default route
@app.route("/")
def home():
    # return "THIS IS HTML"
    return render_template('index.html')

#/Service
@app.route("/service")
def service():
    return render_template('service.html')

#/contact
@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__=='__main__':
    app.run(debug=True)