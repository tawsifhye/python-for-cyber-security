string_var = "Hello World"

print(type(string_var))

string_var = str.encode(string_var)

print(type(string_var))

string_var = string_var.decode()
print(type(string_var))