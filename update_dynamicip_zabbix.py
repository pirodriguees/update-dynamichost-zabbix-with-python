#!/usr/bin/python3

#   Autor: Vinicius Oliveira
#   Data:  06/04/2020


from pyzabbix import ZabbixAPI
from requests import get
import pyping


zabbix_url      = 'http://yoururl/zabbix'
zabbix_username = 'youruser'
zabbix_password = 'yourpassword'


'''tratando exceção de conexão na api do zabbix'''
try:
    zapi = ZabbixAPI(zabbix_url, timeout=4)
    zapi.login(zabbix_username, zabbix_password)
except Exception as err:
     print ('Falha ao conectar na API do Zabbix')   
     print('Erro: {}'.format(err))


'''nome do hostname configurado na interface web do zabbix'''
host_name = "" #host with dynamic ip


"""
zabbuix API Requisições
More information: https://github.com/lukecyca/pyzabbix
"""


"""Coletando o id do HOST"""
req_host_get = zapi.host.get(filter={"host": host_name})
host_id = (req_host_get[0]['hostid'])

req_interface_get = zapi.hostinterface.get(filter={"hostid": host_id})
ip_hostzabbix_srv = (req_interface_get[0]['ip'])


"""coletando o id da interface
"""
req_interface_id = zapi.hostinterface.get(filter={"hostid": host_id})
interfaceid = (req_interface_id[0]['interfaceid'])




"""
pingando ddns para sabermos o ip
"""
ddns_host = "metapf.ddns.net"
host_ping = pyping.ping(ddns_host)
ip_public = host_ping.destination_ip #retornará exatamente o ip destino, não precisando filtrar com regex por exemplo


"""Comparando IP's"""
if ip_hostzabbix_srv != ip_public:
    req_interfaceid_upd = zapi.hostinterface.update({"interfaceid": interfaceid, "ip": ip_public})
    print("O ip estava desatualizado, neste momento foi atualizado com sucesso! :D")
else:
    print("Ip já está equivalente")