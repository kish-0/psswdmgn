#Main
import csv
from tabulate import tabulate
def main():
    newpasswd()
    print(view())
    

def newpasswd(s):
    if s == 'noservicegiven':
        raise ValueError("No service was given")
    
    service = s.lower()
    uname = input("username: ")
    psswd = input("password: ")

    d = {'service': service, 'uname': uname, 'psswd': psswd}

    with open('data.csv', newline='') as csvfile: # Check if username and service already exists
        reader = csv.DictReader(csvfile)
        for line in reader:
            if line['service'] == d['service'] and line['uname'] == d['uname']:
                raise ValueError(f"password for {line['uname']} already exists !")

    with open('data.csv', 'a', newline='') as datafile: # Write to csv file
        fields = ['service', 'uname', 'psswd']
        datawriter = csv.DictWriter(datafile, fieldnames=fields)
        datawriter.writerow(d)
    return "Password saved !"

def view(s=None):
    service = s
    #print(s)
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        dictlist = [line for line in reader]
        if  dictlist is None: return "No data !" #Checking if any data in data.csv

        if service == 'all':
            headers = dictlist[0].keys()
            dictlist = [x.values() for x in dictlist]
            return(tabulate(dictlist, headers=headers))

        else:
            #Check if service exists:
            service = service.lower()
            srvc = [d['service'] for d in dictlist]
            if not service in srvc:
                return "service not found !"
            #Now that service present, continue

            usname = input("username: ")
            for l in dictlist:
                if l['service'] == service and l['uname'] == usname:
                    return(l['psswd'])
            else:
                return("username not found !")
        

if __name__ == "__main__":        
    main()