#! /usr/bin/env python3
# coding: utf-8

import argparse

from controller.dbcreation import CreateDatabase
from controller.dbupdate import UpdateDatabase
from controller.application import Application

def parse_arguments():
    """ This function creates the needed arguments to create and updates
    the database manually """

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--database', help="""Action on Database. Type
    create to create and feed the database. Type update to force the update of
    the database""")
    return parser.parse_args()

def main():
    """ This is the main function """

    args = parse_arguments()

    if args.database == 'create':
        database = CreateDatabase()
        database.prepare()
    elif args.database == 'update':
        database = UpdateDatabase()
        database.update_database(True)

    application = Application()
    application.start()

if __name__ == "__main__":
    main()
