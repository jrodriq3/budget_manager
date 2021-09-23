# imports from Budget.py file
import Budget
# creates instance of the BudgetManager class
outgoings = Budget.BudgetManager(2500)
# calls add_budget function/method and gives value 500
outgoings.add_budget('Groceries', 500)
outgoings.print_summary()

