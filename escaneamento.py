import scapy.all as scapy

class Escaneamento:
    def __init__(self):
        self.ip_local = "192.168.0.11"
        self.ip_dest = "192.168.0.17"
        self.ttl = 77
        self.source_port = 12346
        self.dest_port = 12000
        self.envia_e_recebe_pacote()

    def envia_e_recebe_pacote(self):
        pacote = self.cria_pacote_udp()
        pacote.show()
        for _ in range(5):
            respondido = scapy.sr1(pacote, timeout = 10)
            if respondido:
                break
        if respondido:
            if respondido[0].haslayer(scapy.UDP):
                print("Mensagem retornada pelo servidor:", respondido[0].getlayer(scapy.Raw).load.decode())
                print("A porta está aberta")
            elif respondido[0].haslayer(scapy.ICMP):
                if respondido[0].getlayer(scapy.ICMP).code == 3 and respondido[0].getlayer(scapy.ICMP).type == 3:
                    print("Mensagem retornada pelo servidor:", respondido[0].getlayer(scapy.Raw).load.decode())
                    print("A porta está fechada")
                elif respondido[0].getlayer(scapy.ICMP).code in [1,2,9,10,13] and respondido[0].getlayer(scapy.ICMP).type == 3:
                    print("Mensagem retornada pelo servidor:", respondido[0].getlayer(scapy.Raw).load.decode())
                    print("A porta está filtrada")
        else:
            print("A porta está aberta ou filtrada")

    def cria_pacote_udp(self):
        datagrama = scapy.IP()
        datagrama.src = self.ip_local
        datagrama.dst = self.ip_dest
        datagrama.ttl = self.ttl

        segmento = scapy.UDP()
        segmento.sport = self.source_port
        segmento.dport = self.dest_port

        load = scapy.Raw()
        load.load = "Mensagem enviada para o servidor".encode()

        pacote = datagrama / segmento / load
        return pacote

scan = Escaneamento()
