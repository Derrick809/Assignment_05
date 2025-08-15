# BMI Calculator with functions

def calculate_bmi(weight, height):
    """Calculate and return the BMI."""
    return weight / (height ** 2)

def interpret_bmi(bmi):
    """Return the weight category based on BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Get user input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Output results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {interpret_bmi(bmi)}")

# Run the program
main()