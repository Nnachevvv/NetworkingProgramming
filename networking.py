import socket



def reverse_ip(ip):
    addr = list(reversed(ip.split('.')))
    ip = ".".join(addr)
    return ip


def make_DNS_request(ip):
    ip = ip + '.zen.spamhaus.org'
    arr=(list( map( lambda x: x[4][0], socket.getaddrinfo( \
     ip,80,type=socket.SOCK_STREAM))))
    print(arr[0])
    return arr

def get_dscpr(ip):
    ip = ip.split('.')
    octet = ip[-1]
    if octet == "2" :
        return "SBL-Spamhaus SBL Data"
    elif octet == "3":
        return "SBL-Spamhaus SBL CSS Data"
    elif octet == "4":
        return "XBL-CBL Data"
    elif octet =="9":
         return "SBL-Spamhaus DROP/EDROP Data" 
    elif octet == "10":
        return "PBL-ISP Maintained"
    elif octet == "11":
        return "PBL-Spamhaus Maintained"
    
    return "is NOT found in the Spamhaus blacklists."



def main():
    
    adresses = input("Enter ip adress: ")
    adresses = adresses.split()
    
    for i in range(0,len(adresses)):
        reversed_ip = reverse_ip(adresses[i])
        requested_arr = make_DNS_request(reversed_ip)
        print(f"The IP address: {adresses[i]} is found in the following Spamhaus public IP zone: ")

        for j in range(0,len(requested_arr)):
            print(f"{requested_arr[j]} - {get_dscpr(requested_arr[j])}")

    


main()