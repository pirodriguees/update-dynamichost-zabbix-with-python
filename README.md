# Utilizando Python com Zabbix #
Criado para **atualizar host's registrado no zabbix que possuem ip publico dinâmico**, gerando um falso problema de inacessibilidade no Zabbix.

## Requerimentos
* Testado no Zabbix Server 4.2
```bash
$ pip freeze | grep --color "pyping\|zabbix\|request"
py-zabbix==1.1.5
pyping==0.0.6
requests==2.22.0
zabbix-api==0.5.
```
* Rodar com Python3.
* Possuir registro do ip no no-ip ou derivados.

A idéia de fazer com Python, foi com intuito de aprender um pouco mais da linguagem, além de trazer conhecimento sobre a API do Zabbix.
Para pessoas que como eu são iniciantes em Python, transferir tarefas repetitivas, ou até mesmo scripts Windows/Linux, sempre irá ajudar.