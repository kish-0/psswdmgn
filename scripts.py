#Main
import csv
from tabulate import tabulate
import os
import sys
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

    d = {'service': service, 'uname': uname, 'psswd': None}

    with open(csv_path, newline='') as csvfile: # Check if username and service already exists
        reader = csv.DictReader(csvfile)
        for line in reader:
            if line['service'] == d['service'] and line['uname'] == d['uname']:
                raise ValueError(f"password for {line['uname']} already exists !")
    
    d['psswd'] = input("password: ")
    enterpassword()

    with open(csv_path, 'a', newline='') as datafile: # Write to csv file
        fields = ['service', 'uname', 'psswd']
        datawriter = csv.DictWriter(datafile, fieldnames=fields)
        datawriter.writerow(d)
    return "Password saved !"

def view(s):
    service = s
    enterpassword()
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        dictlist = [line for line in reader]
        if  dictlist is None: return "No data !" #Checking if any data in data.csv

        if service == 'all':
            headers = dictlist[0].keys()
            dictlist = [x.values() for x in dictlist]
            print("\n")
            return(tabulate(dictlist, headers=headers, showindex='always')) + "\n"

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
                    print("\n")
                    return tabulate({'uname': [l['uname']], 'psswd': [l['psswd']]}, headers='keys') + "\n"
                    
            else:
                return("username not found !")

def delete(s):
    if s == 'noservicegiven':
        raise ValueError("No service was given") #Checking if service given
    
    with open(csv_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        dictlist = [line for line in reader]
        if  dictlist is None: return "No data !" #Checking if any data in DATA.csv

    service = s

    service = service.lower()
    srvc = [d['service'] for d in dictlist]
    if service in srvc:
        service_index = srvc.index(service)
    else:
        return "service not found !"             #Check if service exists
    
    usname = input("username: ")
    usnames = [x['uname'] for x in dictlist]
    if usname in usnames:
        if not dictlist[service_index]['uname'] == usname:
            return(f"no {service} username '{usname}' was found !")      #Check if correct username exists
    else:
        return("username not found !")          #Check if uname exists
    
    while True:
        inp = input("Are you sure you want to delete? [yes/no]  ")
        if inp == 'yes' or inp == 'y':
            break
        else:
            sys.exit("Deletion cancelled")

    enterpassword()

    new_dict_list = []
    for l in dictlist:
        if not (l['service'] == service and l['uname'] == usname):
            new_dict_list.append(l)
    
    with open(csv_path, 'w', newline='') as datafile: # Write to csv file
        fields = ['service', 'uname', 'psswd']
        datawriter = csv.DictWriter(datafile, fieldnames=fields)
        datawriter.writeheader()
        for d in new_dict_list:
            datawriter.writerow(d)
    return "Password removed !"

def enterpassword():
    for i in range(3):
        n = input("security password: ")
        if n == password:
            break
        
        remaining = 2-i
        print(f'Wrong password! You have {remaining} more attempt(s) till all data is erased')
    else:
        os.remove(csv_path)
        sys.exit("Data erased !")



if __name__ == "__main__":        
    main()