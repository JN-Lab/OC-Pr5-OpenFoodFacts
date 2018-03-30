#! /usr/bin/env python3
# coding: utf-8

import argparse

from controller.dbcreation import CreateDatabase
from controller.dbupdate import UpdateDatabase

def parse_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--database', help="""Action on Database. Type
    create to create and feed the database. Type update to force the update of
    the database""")
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.database == 'create':
        database = CreateDatabase()
        database.prepare()
    elif args.database == 'update':
        database = UpdateDatabase()
        database.update_database()

if __name__ == "__main__":
    main()
