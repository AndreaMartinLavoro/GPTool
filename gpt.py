import openai
import json


def saveFile(text):
    with open('gpt.md', 'w') as file:
        file.write(text)
    
    
def infoAPI_Key():
    print("Per ottenere l'API key di OpenAI devi andare sulla pagina del sito web di OpenAI dedicata all'API,")
    print("creare un account e seguire le istruzioni per ottenere la tua chiave API.")
    print("Ti consiglio di consultare la documentazione dell'API per comprendere come utilizzarla al meglio.\n")
    
    
# legge l'API Key presente nel file JSON
def getAPI_Key(path):
    result = ""
    
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        result = data['api-key']
        
    except:
        print("Si è verificato un errore in getAPI_Key()\n")
        
    return result


# legge le informazioni relative all'account che ha effettuato il login
def getInfo(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        
        print("modello: " + data['model'])
        print("account: " + data['user'])
        print("data log-in: " + data['data'] + "\n")
        
    except:
        print("Si è verificato un errore in getInfo()\n")


# effettua le request all'API di OpenAI
def gpt3(API_Key, PROMPT, debug = False):
    result = ""
  
    try:
        openai.api_key = API_Key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": PROMPT},
            ]
        )

        for choice in response.choices:
            result += choice.message.content
    except Exception as err:
        result = "Mi dispiace ma si è verificato un errore."
        if debug:
            result = "ERRORE - " + err
      
    return result


# main
json_path = "gpt.json"
html_path = "gpt.html"
getInfo(json_path)

API_Key = getAPI_Key(json_path)

if(API_Key != ""):
    while(True):
        PROMPT = input("Chiedi a GPT: ")
        result = gpt3(API_Key, PROMPT)
        print(result)
        saveFile(result)
        print("\n")
else:
    infoAPI_Key()
    print("API Key NON presente! Premi INVIO per chiudere...")
    exit = input()