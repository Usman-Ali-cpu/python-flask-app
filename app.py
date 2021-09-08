from random_Art import makeImage
from flask import Flask, render_template,  request
import os


app = Flask(__name__)  # creating flask app
picfolder = os.path.join('static', 'images')  # to get path to folder for image
app.config['UPLOAD_FOLDER'] = picfolder


@app.route('/')  # defining default route for app
@app.route('/home')  # define a defualt home route for app
def home():  # define a home function
    # rendering a home page which is index.html page
    return render_template('index.html')


# defining a route for a result page, accessing data by post method
@app.route('/result', methods=['POST', "GET"])
def result():  # a result function to render result page
    output = makeImage(20)  # calling a script which produce a image
    # getting path for image
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], output)
    # redering a hmtl page index with result on it, img path is passed as an argument
    return render_template("index.html", img_produce=pic1)


if __name__ == '__main__':  # defining main
    app.run(debug=True, port=5001)  # run app on port 5001
