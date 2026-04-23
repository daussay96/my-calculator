# Import Flask and the tools we need from it
# Flask - creates our web application
# render_template - loads our HTML page
# request - reads what the user typed in the form
from flask import Flask, render_template, request

# Create the Flask web application
# __name__ tells Flask where this file is located
app = Flask(__name__)

# This is a "route" - it tells Flask what to do when someone visits our homepage "/"
# methods=["GET", "POST"] means this page can both show content (GET) and receive form data (POST)
@app.route("/", methods=["GET", "POST"])
def calculator():

    # Set default values to None (empty) when the page first loads
    result = None  # This will store the answer
    error = None   # This will store any error messages

    # Check if the user clicked the Calculate button (POST request)
    # If they just visited the page, this will be a GET request and we skip the math
    if request.method == "POST":

        # try/except is a safety net - if anything goes wrong, we catch the error
        # instead of crashing the whole app
        try:
            # Read the numbers the user typed in the form
            # request.form["num1"] gets the raw text from the input field
            # float() converts the text "10" into an actual number 10.0
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])

            # Read which operation the user selected (add, subtract, multiply, divide)
            operation = request.form["operation"]

            # Check which operation was selected and do the math
            if operation == "add":
                result = num1 + num2          # Addition

            elif operation == "subtract":
                result = num1 - num2          # Subtraction

            elif operation == "multiply":
                result = num1 * num2          # Multiplication

            elif operation == "divide":
                # Special check for division - dividing by zero is impossible!
                if num2 == 0:
                    error = "Cannot divide by zero!"
                else:
                    result = num1 / num2      # Division

        # If the user typed letters instead of numbers, float() will fail
        # We catch that mistake here and show a friendly message
        except ValueError:
            error = "Please enter valid numbers."

    # Send the result back to the HTML page
    # render_template loads index.html and passes in the result and error values
    # index.html will display them to the user
    return render_template("index.html", result=result, error=error)

# This block only runs when you execute this file directly (python app.py)
# host="0.0.0.0" means accept connections from anywhere - important for Docker!
# port=5000 is the door number our app listens on
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)