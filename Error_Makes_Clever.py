s_username="emc"
s_password="123"
def validate():
    if(s_username==username and s_password==password):
        return "True"
    else:
        return "false"


username=input("username:")
password=input("password:")
print(validate())