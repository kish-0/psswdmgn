#Main
import csv
import argparse

def run():
    #write(data)
    print(find())

def write():
    service = input("service: ")
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

def find():
    service = input("service: ")
    usname = input("username: ")

    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for line in reader:
            if line['service'] == service and line['uname'] == usname:
                return line['psswd']
        else:
            return "Service not found !"
        
run()