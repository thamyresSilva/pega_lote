import requests
import json
from datetime import datetime

url_dealer = ''

dealers = {'geru':''}

dateTimeObj = datetime.now()
today = dateTimeObj.strftime("%d-%m-%Y-%H-%p")

for dealer in dealers:
    headers={'Authorization':(dealers[dealer]), 'Content-Type': 'application/json'}
    response = requests.get(url_dealer + '/deal_packages_batch', headers=headers)
    print ("Nome do Dealer: " + dealer)
    
    assert response.status_code == 200

    #salva_arquivo
    arquivo = open(dealer + '-' + today + '.text', "w")
    json.dump(response.json(), arquivo)
    arquivo.close()
    
    #pega_uuid_do_lote
    uuid_lote_de_acordos = (response.json()['uuid'])
    print("UUID Do Lote de acordos: " + uuid_lote_de_acordos)
    
    #confirma_lote_de_acordos
    payload = {"__all__": "string"}
    headers={'Authorization': (dealers[dealer])}

    confirmaRecebimento = requests.post(url_dealer + '/deal_packages_batch/' + uuid_lote_de_acordos + '/confirm_receipt',  json=payload, headers=headers)

    assert confirmaRecebimento.status_code == 200
