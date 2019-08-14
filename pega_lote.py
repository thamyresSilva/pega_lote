from datetime import datetime
import requests
import json
import time


url_dealer = ''

dealers = {'Geru':''}
dateTimeObj = datetime.now()
today = dateTimeObj.strftime("%d-%m-%Y-%H-%p")
today_request = dateTimeObj.strftime("%d-%m-%Y" +  " ás " "%H:%M:%Sh")

for dealer in dealers:
    print("Lote requisitado em: " +  today_request)
    headers={'Authorization':(dealers[dealer]), 'Content-Type': 'application/json'}
    response = requests.get(url_dealer + '/deal_packages_batch', headers=headers)
    print ("Nome do Dealer: " + dealer)
    print (response.status_code)
    assert response.status_code == 200
    
    #salva_arquivo
    arquivo = open(dealer + '-' + today + '.json', "w")
    json.dump(response.json(), arquivo)
    arquivo.close()
    
    #pega_uuid_do_lote
    uuid_lote_de_acordos = (response.json()['uuid'])
    print("UUID Do Lote de acordos: " + uuid_lote_de_acordos)
    
    #confirma_lote_de_acordos
    time.sleep(120)
    payload = {"__all__": "string"}
    headers={'Authorization': (dealers[dealer])}
    
    confirmaRecebimento = requests.post(url_dealer + '/deal_packages_batch/' + uuid_lote_de_acordos + '/confirm_receipt',  json=payload, headers=headers)
    print(confirmaRecebimento.status_code)
    assert confirmaRecebimento.status_code == 200
