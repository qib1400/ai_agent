from functions.get_files_info import get_files_info

print("Result for .")
print(get_files_info("calculator", "."))
print("Result for pkg")
print(get_files_info("calculator", "pkg"))
print("Result for /bin")
print(get_files_info("calculator", "/bin"))
print("Result for ../")
print(get_files_info("calculator", "../"))