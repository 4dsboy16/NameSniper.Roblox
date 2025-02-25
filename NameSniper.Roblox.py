import requests
import time
from colorama import Fore, Style, init

init()

def check(user):
  url = f"https://auth.roblox.com/v1/usernames/validate?Username={user}&Birthday=2006-01-01"
  try:
    response = requests.get(url)
    response_data = response.json()

    code = response_data.get("code")

    if code == 0:
      print(Fore.GREEN + f"VALID: {user}" + Style.RESET_ALL)
    elif code == 1:
      print(Fore.LIGHTBLACK_EX + f"TAKEN: {user}" + Style.RESET_ALL)
    elif code == 2:
      print(Fore.RED + f"CENSORED: {user}" + Style.RESET_ALL)
    else:
      print(Fore.YELLOW + f"OOF: ({code}): {user}" + Style.RESET_ALL)
  
  except requests.exceptions.RequestException as ex:
    print(Fore.YELLOW + f"FAIL: {user}: {ex}" + Style.RESET_ALL)

def app():
  with open("users.txt", "r") as content:
    users = content.read().splitlines()

  for user in users:
    check(user)
    time.sleep(0.05)

if __name__ == "__main__":
  app()
