#! /usr/bin/env python3
# coding: utf-8

import argparse

from dbcreation import DatabaseCreation
from interface import Interface

def parse_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--database', help="""Action on Database. Type
    create to create and feed the database. Type update to force the update of
    the database""")
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.database == 'create':
        database = DatabaseCreation()
        database.prepare()
    elif args.database == 'update':
        pass
        
    interface = Interface()
    interface.start()

if __name__ == "__main__":
    main()
