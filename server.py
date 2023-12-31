from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"




@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"

list = ["Flask", "Michael", "John"]
@app.route("/say/<name>")
def say(name):
    return render_template("index.html", name = name, word = "", number = 0)


@app.route("/repeat/<int:number>/<word>")
def repeat(number, word):
    print('what is word --->', type(word))
    print('what is number --->', type(number))
    return render_template("index.html", number  = number,   word = str(word), name = "")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
