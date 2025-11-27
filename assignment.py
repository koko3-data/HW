# ------------------------------------------------------------
# EXPENSE TRACKER
# ------------------------------------------------------------
#
# INSTRUCTIONS:
# - Read all tasks below.
# - Then implement your full solution directly in this file.
# - You may structure your code however you want.
# - Do everything in this single file.
#
# ------------------------------------------------------------
# 1. DATA MODEL & SETUP
# ------------------------------------------------------------
#
# Create the following GLOBAL variables:
#
#   currency = "PLN"
#   expenses = []
#   next_expense_id = 1
#
# Each expense must be a dictionary:
#   {
#       "id": ...,
#       "amount": ...,
#       "category": ...,
#       "description": ...
#   }
currency = "PLN"
expenses = []
next_expense_id = 1
current_id = 0
# expense= {
#     "id": int,
#     "amount": float,
#     "category": ...,
#     "description": ...
#     }
# ------------------------------------------------------------
# 2. FUNCTION add_expense – Parameters vs Arguments
# ------------------------------------------------------------
#
# Create a function:
#
#   def add_expense(expenses_list, expense_id, amount, category, description):
def add_expense(expenses_list, expense_id, amount, category, description):
      expense = {
      "id": expense_id,
      "amount": amount,
      "category": category,
     "description":description
    }
      expenses_list.append(expense)
      return expenses_list

# Inside the function:
#   - Create an expense dictionary using the parameters
#   - Append it to expenses_list
#   - Return expenses_list
#
# In global code:
#   - Call add_expense() at least 5 times with different arguments

#   - Assign the returned list back into the global expenses variable
expenses = add_expense(expenses,next_expense_id,100,"Food","Bread and Eggs for Breakfast")
next_expense_id+=1
expenses = add_expense(expenses,next_expense_id,200,"Shopping","Santa PJS for Christmas")
next_expense_id+=1
expenses = add_expense(expenses,next_expense_id,300,"Fruits","Fruit varieties for healthy dieting")
next_expense_id+=1
expenses = add_expense(expenses,next_expense_id,400,"Shopping","Christmas Groceries")
next_expense_id+=1
expenses = add_expense(expenses,next_expense_id,500,"Skincare","Skincare varieties for the month")

print(expenses)
# ------------------------------------------------------------
# 3. FUNCTION calculate_total – Local variables & scope
# ------------------------------------------------------------
#
# Create:
#
#   def calculate_total(expenses_list):
#
# Inside the function:
#   - Create a local variable total = 0
#   - Loop through expenses_list and sum all amounts into total
#   - Print the total from inside the function
#   - Return total
def calculate_total(expenses_list):
    total = 0
    for expense in expenses_list:
         total+=expense["amount"]
    print(f"Total: {total}")
    return total
    
      
calculate = calculate_total(expenses)
#
# In global code:
#   - Call: overall_total = calculate_total(expenses)
#   - Print overall_total from outside the function
overall_total = calculate_total(expenses)
print(overall_total)
#
# Then deliberately try:
#   print(total)
# print(total)
# This should fail because total is local.
#
# ------------------------------------------------------------
# 4. FUNCTION calculate_category_total – Shadowing
# ------------------------------------------------------------
#
# Create:
#
#   def calculate_category_total(expenses_list, category, currency):
def calculate_category_total(expenses_list, category, currency):
    category_total = 0
    for expense in expenses_list:
        if expense["category"] == category:
            category_total+=expense["amount"]
    print(f"Category_Total:{category_total} {currency}")
    return category_total


calculate_category =calculate_category_total(expenses,"Shopping",currency)
calculate_category =calculate_category_total(expenses,"Food",currency)


# Inside:
#   - Create category_total = 0
#   - Sum amounts where expense["category"] matches the category
#   - Print the total and the currency parameter
#   - Return category_total
#
# In global code:
#   - Call the function for at least two categories
#   - Print the global currency afterwards to show it did not change
#
# ------------------------------------------------------------
# 5. BUGGY ID GENERATOR – Demonstrating scope errors
# ------------------------------------------------------------
#
# Create a BUGGY version:
#
#   def generate_id():
#       next_expense_id = next_expense_id + 1
#       return next_expense_id
#
# Call it twice:
#   generate_id()
#   generate_id()
#
# This should raise an error because next_expense_id becomes a local
# variable inside the function before being defined.
# def generate_id():
#     next_expense_id = next_expense_id + 1
#     return next_expense_id

# generate_id()
# generate_id()

# ------------------------------------------------------------
# 6. FIXING generate_id – Two Versions
# ------------------------------------------------------------
#
# 6A. Version using global:
#
#   def generate_id_global():
#       global next_expense_id
#       next_expense_id = next_expense_id + 1
#       return next_expense_id

def generate_id_global():
    global next_expense_id
    next_expense_id = next_expense_id + 1
    return next_expense_id

generate_id_global()
generate_id_global()
generate_id_global()
# Call this at least three times.
#
# 6B. Pure version (preferred):
#
#   def generate_id_pure(current_id):
#       new_id = current_id + 1
#       return new_id

def generate_id_pure(current_id):
    new_id = current_id + 1
    print(f"ID:{new_id}")
    return new_id
    
generate_id_pure(current_id)

generate_id_pure(current_id)


# Reset next_expense_id = 0 and call generate_id_pure() twice,
# updating next_expense_id each time.
#
# ------------------------------------------------------------
# 7. INTEGRATE generate_id_pure INTO add_expense
# ------------------------------------------------------------
#
# Refactor your global add_expense calls:
#   - Do not hard-code IDs.
#   - Every time before adding an expense:
#
#         next_expense_id = generate_id_pure(next_expense_id)
#
#   - Then call add_expense with that ID.
#   - Add at least 5 expenses this way.
#
# ------------------------------------------------------------
# 8. FINAL PROGRAM OUTPUT
# ------------------------------------------------------------
#
# Your final program should print:
#
#   1. All expenses (loop and print each)
#   2. The overall total using calculate_total(expenses)
#   3. At least two category totals using calculate_category_total(...)
#   4. The final value of next_expense_id
#
# When executed, the file should produce visible output demonstrating
# correct function behavior and correct understanding of:
#   - parameters vs arguments
#   - local vs global scope
#   - variable shadowing

