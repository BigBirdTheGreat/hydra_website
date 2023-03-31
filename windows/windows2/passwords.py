import bcrypt

# store your password</strong>:
password = str(input("input password: ")) 

# Encode the stored password</strong>:
password = password.encode('utf-8')

# Encrypt the stored pasword</strong>:
hashed = bcrypt.hashpw(password, bcrypt.gensalt(4)) 

print(hashed)

hashed = "$2b$04$9zgpx5ufz1okU06dyvBIf.Y48BAH8XxnjuefxFlSfAVDVxwh4GlDe"
hashed = hashed.encode('utf-8')

# Create an authenticating password input field to check if a user enters the correct password</strong> 
check = str(input("check password: ")) 

# Encode the authenticating password as well</strong> 
check = check.encode('utf-8') 

# Use conditions to compare the authenticating password with the stored one</strong>:
if bcrypt.checkpw(check, hashed):
    print("login success")
else:
    print("incorrect password")