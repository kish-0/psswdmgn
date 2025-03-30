import argparse
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
from scripts import newpasswd, view, delete

def main():
    parser = argparse.ArgumentParser(description="Add/Generate and save passwords securely")

    action = parser.add_mutually_exclusive_group()
    action.add_argument("-n", "--newpsswd", help="Used to add and save psswd of new service", nargs="?", const="noservicegiven")
    action.add_argument("-v", "--view", help="Used to view saved credentials", nargs="?", const="all")
    action.add_argument("-d", "--delete", help="Delete existing instances", nargs="?", const="noservicegiven")

    args = vars(parser.parse_args())
    
    try:
        if args['view']:
            print(view(args["view"]))
        elif args['newpsswd']:
            print(newpasswd(args["newpsswd"]))
        elif args['delete']:
            print(delete(args['delete']))
    except IndexError:
        print("No data !")


if __name__ == "__main__":
    main()