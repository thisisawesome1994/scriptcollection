# Import the necessary modules
import flask
from flask import request, render_template

# Define the function to calculate the annual increase in money and amount after inflation
def calculate_increase(initial_investment, monthly_investment, annual_increase, years, inflation):
    """
    This function calculates the annual increase in money and amount after inflation of an investment.

    Args:
        initial_investment: The initial investment.
        monthly_investment: The monthly investment.
        annual_increase: The annual increase (percentage).
        years: The number of years.
        inflation: The inflation rate (percentage).

    Returns:
        A tuple containing the annual increase in money and the amount after inflation.
    """

    # Calculate the total investment
    total_investment = initial_investment + (monthly_investment * 12 * years)

    # Calculate the final value after 'years' years
    final_value = total_investment * (1 + annual_increase / 100) ** years

    # Calculate the annual increase in money
    annual_increase_money = final_value - total_investment

    # Calculate the amount after inflation
    amount_after_inflation = final_value / (1 + inflation / 100) ** years

    return annual_increase_money, amount_after_inflation

# Define the Flask app
app = flask.Flask(__name__)

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
    inflation = 0.0

    # Check if form is submitted
    if request.method == 'POST':
        # Get the input variables
        initial_investment = float(request.form.get("initial_investment", 0.0))
        monthly_investment = float(request.form.get("monthly_investment", 0.0))
        annual_increase = float(request.form.get("annual_increase", 0.0))
        years = int(request.form.get("years", 0))
        inflation = float(request.form.get("inflation", 0.0))

    # Calculate the annual increase in money and amount after inflation
    annual_increase_money, amount_after_inflation = calculate_increase(initial_investment, monthly_investment, annual_increase, years, inflation)

    # Display the home page with calculated values
    return render_template("index.html", initial_investment=initial_investment, monthly_investment=monthly_investment, annual_increase=annual_increase, years=years, inflation=inflation, annual_increase_money=annual_increase_money, amount_after_inflation=amount_after_inflation)

# Start the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
