import socket
import optparse


def connect(host):
    try:
        f = open(host, 'r')
        data = f.read().splitlines()
        for x in data:
            try:
                hostname = x
                ipAddr = socket.gethostbyname(hostname)
                vp = ipAddr
                ad = socket.gethostbyaddr(vp)
                print(f'{ad} and {ipAddr}')
            except:
                print("Its not vul for reverse lookup")
    except:
        try:
            hostname = host
            ipAddr = socket.gethostbyname(hostname)
            vp = ipAddr
            ad = socket.gethostbyaddr(vp)
            print(f'{ad} and {ipAddr}')
        except:
            print("Its not vul for reverse lookup")


def main():
    parser = optparse.OptionParser("usage -H"+'<Enter Host>')
    try:
        parser.add_option('-H', dest='host', type='string',
                          help='this check if its reslove or not will reslove')
    except:
        pass
    (options, args) = parser.parse_args()
    host = options.host
    if (host == None):
        print(parser.usage)
        exit(0)
    connect(host)


if __name__ == '__main__':
    main()
