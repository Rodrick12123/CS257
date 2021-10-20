import psycopg2
import argparse

'''
    olympics.py
    19 October 2021

    Functions implemented by Rodrick Lankford
'''

def main():
    #all of the parser arguments available
    parser = argparse.ArgumentParser()
    parser.add_argument('--password', '-p', type = str)
    parser.add_argument('--database', '-d', type = str)
    parser.add_argument('--user', '-u', type = str)
    parser.add_argument('-?', '--usage', action='store_true')
    parser.add_argument('--NOC', '-n', type = str)
    parser.add_argument('--gold', '-g', action='store_true')
    parser.add_argument('--sport', '-s', type = str)
    #why cant I do --help or -h here?


    args = parser.parse_args()
    if args.password:
        password = args.password
    else:
        password = "Lankford1"
    if args.database:
        database = args.database
    else:
        database = "olympics"
    if args.user:
        user = args.user
    else:
        user = "rodrick"
    if args.usage:
        file = open('ussage.txt', 'r')
        lines = file.readlines()
        for line in lines:
            print(line)
    #try to connect to psycopg2 with given parameters
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()


    #list all athletes from specified NOC
    if args.NOC:
        query = '''SELECT firstname, lastname, NOC
                FROM athletes
                WHERE athletes.NOC like %s'''
        try:
            cursor = connection.cursor()
            cursor.execute(query, (args.NOC,))
        except Exception as e:
            print(e)
            exit()

        for row in cursor:
            print(row[0], row[1], row[2])
        print()
    #prints list of NOC regions with their gold medal count in decreasing order
    if args.gold:
        query = '''SELECT noc_regions.NOC, noc_regions.gold_medal
                FROM noc_regions
                ORDER BY gold_medal DESC'''
        try:
            cursor = connection.cursor()
            cursor.execute(query)
        except Exception as e:
            print(e)
            exit()

        for row in cursor:
            print(row[0], row[1])
        print()
    #prints a list of athletes with the sport they played that is the desired search result of the user
    if args.sport:
        query = '''SELECT athletes.firstname, athletes.lastname, events.sport
                FROM athletes, events
                WHERE athletes.id = events.athleteid
                AND events.sport like %s'''
        cap = (args.sport).capitalize()
        try:
            cursor = connection.cursor()
            cursor.execute(query, (cap,))
        except Exception as e:
            print(e)
            exit()

        for row in cursor:
            print(row[0], row[1], row[2])
        print()

    connection.close()

if __name__=='__main__':
    main()