# escaneamento-de-porta

Script escaneamento.py envia mensagem para um servidor que está implementado em servidor.py, ao receber uma resposta UDP imprime que a porta está aberta, caso a resposta seja ICMP com código 3 imprime que a porta está aberta, caso a resposta seja ICMP com códigos 1, 2, 9, 10 ou 13 imprime que a porta está filtrada e caso não receba resposta imprime que a porta está aberta ou filtrada
