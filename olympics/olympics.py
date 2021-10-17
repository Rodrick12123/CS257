import psycopg2
import argparse

# from config import password
# from config import database
# from config import user


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--password', '-p', type = str)
    parser.add_argument('--database', '-d', type = str)
    parser.add_argument('--user', '-u', type = str)
    parser.add_argument('--usage', '-?', type = str)
    parser.add_argument('--NOC', '-n', type = str)
    #why cant I do --help or -h here?
    #parser.add_argument('--year', '-y', type = int, nargs='+')
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

    connection.close()

if __name__=='__main__':
    main()