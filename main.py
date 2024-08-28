import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
import warnings, os, time, requests
from random import randint
from colorama import Fore
import asyncio
import random
api = "https://127.0.0.1:6327"
mailapi = "https://api.mail.tm"
warnings.filterwarnings('ignore')


def newTry():
    waitedOnPage = 0
    mailapi = "https://api.mail.tm"
    password =   ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=14))
    email = password + "@starmail.net"
    body = {
        
        "address" : email,
        "password": password
    }
    headers = {
    "Content-Type": "application/json"
    }
    r = requests.post(mailapi + "/accounts", json=body, headers=headers)
    time.sleep(1.5)
    r = requests.post(mailapi + "/token", json=body, headers=headers)
    token = r.json()['token']
  
    payload = {
        "acceptedPrivacyPolicy" : True,
        "email" : email,
        "password1" : password,
        "password2" : password,
        "subscribeToNewsletter" : True
    }
    print("Generating [" + email + "]")
    uwu = requests.post(api + "/user", verify=False, json=payload)
    uwuw = str(uwu.json())
    if uwuw == "{'error': '429'}":
        print(Fore.RED + "Rate limited. Change IP or wait 1 minute")
        exit()
    time.sleep(5)
    # Send a request to /messages endpoint
    messages_url = mailapi + "/messages"
    source_url = mailapi + "/sources/"
    headers = {
        "Content-Type": "application/json",

        "Authorization":"Bearer " + token
    }
    response = requests.get(messages_url, headers=headers)
    
    # Find the link containing "link.steelseries.com/ls/click"
    link = None
    messages = response.json()
    if 'hydra:member' in messages:
        message_id = messages['hydra:member'][0]['id']
    
    else:
        print("No messages found")
    
    sourceresp = requests.get(source_url + message_id, headers=headers)
    source = sourceresp.json()
    sourceData = source['data']
    start_index = sourceData.find('Verify My Account')
    end_index = sourceData.find('Questions?', start_index)
    link = sourceData[start_index:end_index].strip()
    link = link.replace("=", "")
    link = link.replace("?token3D", "?token=")
    print(link)
    
    input("Press Enter to continue...")
    time.sleep(3)
    def getcode():
        payload = {
            "name" : "giveaway_discord_jul01"
        }
        reques = requests.post(api + "/promos/code", verify=False, json=payload)
        req = reques.json()
        
        print(Fore.GREEN + f"Code: {req['promocode']:30} | Email: {email} | Pass: {password}")
        with open("account.txt", "a", encoding="utf-8") as myfile:
            myfile.write(f"{email}:{password} | {req['promocode']}\n")
        with open("codes.txt", "a", encoding="utf-8") as myfile:
            myfile.write(f"{req['promocode']}\n")
        
        print(Fore.RESET)
    while True:
        try:
            getcode()
            break
        except Exception as e:
            print(f"An error occurred: (This probably means ratelimit) {str(e)}")
            print("Waiting 10 seconds and trying again...")
            time.sleep(10)


gene = 0
while True:
    if gene == 4:
        time.sleep(40)
        gene = 0
    os.system('taskkill /f /IM SteelSeriesGGClient.exe>temp')
    os.system('start cmd /c "C:\Program Files\SteelSeries\GG\SteelSeriesGGClient.exe"')
    time.sleep(1)
    newTry()
    time.sleep(1)
    gene += 1
