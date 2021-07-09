from flask import Flask # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
#1
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

#2
@app.route('/dojo')
def hello_dojo():
    return "Dojo"


#3
@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name}!"


#4
@app.route('/repeat/<int:x>/<string>')
def repeat_word(x, string):
    word_repeat = ''
    for i in range(x):
        word_repeat += (string + ' ')
    return word_repeat


if __name__=="__main__":
    app.run(debug=True)

