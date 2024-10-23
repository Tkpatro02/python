Password="Pupun1232323"

Password_length=len(Password)

if Password_length <6:
    strength="weak"
elif Password_length <=10:
    strength="medium"
else:
    strength="strong"
print("your password is ", strength)