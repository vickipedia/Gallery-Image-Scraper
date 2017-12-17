from urllib import request
import os

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

path = "E:\Photos\\" # Enter the path to save folders (each containing one gallery)

url = "" # Enter the common URL here
name = "" # Enter the name of the folder
start = 1 # Enter the start sequence number
end = 100 # Enter the end sequence number

try:
    os.makedirs(path + "%s" % name)
except:
    print ("Folder already exists!")

for i in range(start,end+1):
    try:
        link = "%s%d.jpg" % (url,i)
        folder = path + "%s\%s%d.jpg" % (name,name,i)

        opener = request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        request.install_opener(opener)

        f = open(folder, 'wb')
        f.write(request.urlopen(link).read()) #, headers=hdr)
        f.close()

        print ("%s %d" % (name,i),"done.")
    except:
        f.close()
        os.remove(path + "%s\%s%d.jpg" % (name,name,i))
        print ("%s %d" % (name,i),"not found.")

print ("Completed..")