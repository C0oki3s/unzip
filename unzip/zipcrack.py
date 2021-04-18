import zipfile
import optparse
from threading import Thread

def File(file,password):
    try:
        file.extractall(pwd=password)
        print(f"Found password {password}")
    except:
        print("Not Yet")
        pass
def main():
        Rules = optparse.OptionParser("Usage Of the Script "+ "-f <UrZipFile> -d <Payload>")
        try:
            Rules.add_option('-f', dest="filename", type='string', help="Please place Ur zip File")
            Rules.add_option('-d', dest="Payload", type='string', help="Please Place Ur Payload.txt Here")
        except:
            pass
        (options, args) = Rules.parse_args()
        if (options.filename == None) or (options.Payload == None):
            print(Rules.usage)
            exit(0)
        else:
            filename = options.filename
            Payload = options.Payload
        file = zipfile.ZipFile(filename)
        passFile = open(Payload)
        for line in passFile.readlines():
            password = line.strip('\n')
            t = Thread(target=File, args=(file, password))
            t.start()
if __name__ =='__main__':
    main()
