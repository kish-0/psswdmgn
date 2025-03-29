#Main
import csv
from tabulate import tabulate
import os
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def loadcsv():
    checkpath = os.path.join(BASE_DIR, 'DATA.csv')
    if os.path.exists(checkpath):
        return checkpath
    else:
        with open(checkpath, 'w', newline='') as createcsvfile:
            fields = ['service', 'uname', 'psswd']
            writer = csv.DictWriter(createcsvfile, fieldnames=fields)
            writer.writeheader()   
        return checkpath
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Settig dirs for correct importing, file creation and usage
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = loadcsv()
password = 'hi'
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
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

    with open(csv_path, newline='') as csvfile: # Check if username and service already exists
        reader = csv.DictReader(csvfile)
        for line in reader:
            if line['service'] == d['service'] and line['uname'] == d['uname']:
                raise ValueError(f"password for {line['uname']} already exists !")

    with open(csv_path, 'a', newline='') as datafile: # Write to csv file
        fields = ['service', 'uname', 'psswd']
        datawriter = csv.DictWriter(datafile, fieldnames=fields)
        datawriter.writerow(d)
    return "Password saved !"

def view(s=None):
    service = s
    #print(s)
    with open(csv_path, newline='') as csvfile:
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

def enterpassword():
    for i in range(3):
        n = input("security password: ")
        if n == password:
            return None
        
        remaining = 2-i

        if remaining == 0:
            break

        print(f'Wrong password! You have {remaining} more attempts till all data is erased')

    print("Data erased !")
    os.remove(csv_path)
    return("Wrong password !")


if __name__ == "__main__":        
    main()