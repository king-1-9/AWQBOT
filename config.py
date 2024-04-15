import json
import os

import requests
from database import get_db_general_rtb
from utils import get_restarted

super_sudoers = [5145609515]


####################################################################################

# start

wr = get_restarted()
if wr is None:
    if os.path.exists('info.json'):
        fileSize = os.path.getsize("info.json")
        if fileSize == 0:
            
            tokenBot = '6204532438:AAEcr5ro1AQE8LC7vNUPaFEpQDpPZKoJZTk' 
            
            idSudo = 5145609515

            aDict = {"Token": tokenBot, "idSudo": int(idSudo)}
            jsonString = json.dumps(aDict)
            jsonFile = open("info.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
    else:
        
        tokenBot = '7075593585:AAH-idyUQtMT7hJbnP1IpCzrFA9YG5oMltE'
        
        idSudo = 5145609515

        aDict = {"Token": tokenBot, "idSudo": int(idSudo)}
        jsonString = json.dumps(aDict)
        jsonFile = open("info.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

####################################################################################

# Bot token from Bot Father

# TOKEN = "5664558596:6185311761:AAF1960-FhRxYpmU_qYvADz_AlQy5zI93hU"
f = open('info.json', )
data = json.load(f)
TOKEN = data['Token']


# Your API ID and Hash from https://my.telegram.org/apps
API_ID = 20036317
API_HASH = "986cb4ba434870a62fe96da3b5f6d411"

# Chat used for logs
log_chat = 5145609515
# Sudoers and super sudoers
sudoers = [data['idSudo']]
sudoers += super_sudoers
developer = []
developer += sudoers
f.close()


####################################################################################

def dev():
    lang = get_db_general_rtb("developer")
    lang2 = get_db_general_rtb("secdeveloper")
    if lang is None:
        print("No Developer")
    else:
        for row in lang:
            t = row[0]
            developer.append(t)
    if lang2 is None:
        print("No Second Devoloper")
    else:
        for row in lang2:
            t = row[0]
            developer.append(t)
    print(developer)


def get_bot_information():
    bot_inf = requests.get(
        "https://api.telegram.org/bot" + TOKEN + "/getme")
    bot_info = bot_inf.json()
    result = bot_info["result"]
    bot_id = result["id"]
    bot_username = result["username"]
    return bot_id, bot_username


#####################################################################################


# Prefixes for commands, e.g: /command and !command
prefix = ["/", "!"]

# List of disabled plugins
disabled_plugins = []

# API keys
TENOR_API_KEY = "2MAL8NKBOO01"

# Bot version, do not touch this
with open("version.txt") as f:
    version = f.read().strip()


# Run function
dev()
