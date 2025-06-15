"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def calculate_totals(incomes):
    """Calculate running totals for a list of incomes."""
    totals = []
    total = 0
    for income in incomes:
        total += income
        totals.append(total)
    return totals

def print_income_report(incomes, num_months):
    """Print an income report with monthly incomes and running totals."""
    totals = calculate_totals(incomes)
    print("\nIncome Report\n-------------")
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total = totals[month - 1]
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes, num_months)

main()