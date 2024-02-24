# Import the necessary modules
import flask
from flask import request, render_template

# Define the function to calculate the percentage increase
def calculate_increase(initial_investment, monthly_investment, annual_increase, years):
    """
    This function calculates the percentage increase of an investment.

    Args:
        initial_investment: The initial investment.
        monthly_investment: The monthly investment.
        annual_increase: The annual increase.
        years: The number of years.

    Returns:
        The percentage increase.
    """

    # Calculate the total investment
    total_investment = initial_investment + (monthly_investment * 12 * years)

    # Check if the total investment is zero to avoid division by zero
    if total_investment == 0:
        return 0

    # Calculate the final value
    final_value = total_investment * (1 + annual_increase) ** years

    # Calculate the percentage increase
    percentage_increase = (final_value - total_investment) / total_investment * 100

    return percentage_increase

# Define the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Define the route for the home page
@app.route("/", methods=['GET', 'POST'])
def home():
    """
    This function displays the home page.

    Args:
        None.

    Returns:
        The home page.
    """

    # Set default values if form is not submitted yet
    initial_investment = 0.0
    monthly_investment = 0.0
    annual_increase = 0.0
    years = 0

    # Check if form is submitted
    if request.method == 'POST':
        # Get the input variables
        initial_investment = float(request.form.get("initial_investment", 0.0))
        monthly_investment = float(request.form.get("monthly_investment", 0.0))
        annual_increase = float(request.form.get("annual_increase", 0.0))
        years = int(request.form.get("years", 0))

    # Calculate the percentage increase
    percentage_increase = calculate_increase(initial_investment, monthly_investment, annual_increase, years)

    # Display the home page
    return render_template("home.html", initial_investment=initial_investment, monthly_investment=monthly_investment, annual_increase=annual_increase, years=years, percentage_increase=percentage_increase)

# Start the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
