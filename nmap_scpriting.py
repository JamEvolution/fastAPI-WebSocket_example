import nmap

# nmap tarama nesnesi oluşturma
nm = nmap.PortScanner()

# hedef IP adresi veya adres aralığını belirleme
target = '192.168.1.0/24'

# ağ tarama işlemi gerçekleştirme
nm.scan(hosts=target, arguments='-n -sP')

# tarama sonucunda bulunan IP adreslerini listeleme
for host in nm.all_hosts():
    print('Host : %s (%s)' % (host, nm[host].hostname()))

    # bulunan host'un açık olan portlarını tarama
    nm.scan(host, arguments='-sS')

    # port sonuçlarını listeleme
    for proto in nm[host].all_protocols():
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()
        for port in lport:
            print('port : %s' % port)

