starting_age = 22
retirement_age = 65
years_of_work = retirement_age - starting_age

starting_salary = 26000
yearly_raise = 300

monthly_mortgage_payment = 900
mortgage_duration = 480  
other_expenses = 750
bank_balance = 0

annual_interest_rate = 0.02
monthly_interest_rate = annual_interest_rate / 12

current_salary = starting_salary
remaining_mortgage = mortgage_duration

for year in range(years_of_work):
    for month in range(12):
        if bank_balance > 0:
            bank_balance *= (1 + monthly_interest_rate)

        monthly_income = current_salary / 12
        monthly_tax_free_limit = 35000 / 12

        if monthly_income > monthly_tax_free_limit:
            after_tax_income = ((monthly_income - monthly_tax_free_limit) * 0.6) + (monthly_tax_free_limit * 0.8)
        else:
            after_tax_income = monthly_income * 0.8

        bank_balance += after_tax_income
        bank_balance -= other_expenses

        if remaining_mortgage > 0:
            bank_balance -= monthly_mortgage_payment
            remaining_mortgage -= 1

    current_salary += yearly_raise

print(f"Bob's bank balance at age {retirement_age} (with tax + 2% interest): £{bank_balance:,.2f}")
