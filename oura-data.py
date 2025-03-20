
file_path = 'APItoken.txt'
with open(file_path, 'r') as file:
    APIToken = file.read()
print(APIToken)