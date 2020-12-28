import requests
import time

#will call other funcations
def main():
    message = input('Please enter a message to be relayed: ')
    while (1 > 0):
        for char in message:
            updateStatus(char)
            time.sleep(5)
        updateStatus('*static*')
        time.sleep(10)
        


#sends text to discord servers with a hardcoded auth key
def updateStatus(text):
    session = requests.Session()
    headers = {
        'authorization': 'MjA0MDkwNzE0MjkwNzgyMjA5.XvaZug.e1YTudy5b9mZ0471R141nyGuCAI',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
        'content-type': 'application/json'
    }
    data = '{"custom_status":{"text":"' + text + '"}}'
    r = session.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, data=data)
    if '"custom_status": {"text": "' in r.text:
        print('[SUCCESS] Status changed: ' + str(text))

main()
