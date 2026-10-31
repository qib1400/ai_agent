from functions.run_python_file import run_python_file

print('Results for "main.py"')
result = run_python_file("calculator", "main.py") #(should print the calculator's usage instructions)
print(result)

print('Results for "main.py", ["3 + 5"]')
result = run_python_file("calculator", "main.py", ["3 + 5"]) #(should run the calculator... which gives a kinda nasty rendered result)
print(result)

print('Results for "tests.py"')
result = run_python_file("calculator", "tests.py") #(should run the calculator's tests successfully)
print(result)

print('Results for "../main.py"')
result = run_python_file("calculator", "../main.py") #(this should return an error)
print(result)

print('Results for "nonexistent.py"')
result = run_python_file("calculator", "nonexistent.py") #(this should return an error)
print(result)

print('Results for "lorem.txt"')
result = run_python_file("calculator", "lorem.txt") #(this should return an error)
print(result)