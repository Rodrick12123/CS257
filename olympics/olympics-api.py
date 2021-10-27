
'''
    olympics.py
    19 October 2021

    Functions implemented by Rodrick Lankford
'''

import operator
import sys
import argparse
import flask
from flask import request
import json
import csv
import psycopg2
app = flask.Flask(__name__)
#creates the list of game dictionaries using a query
def game_gen():
    game_dict = {}
    glist =[]
    years = []
    try:
        connection = psycopg2.connect(database="olympics", user="rodrick", password="Lankford1")
    except Exception as e:
        print(e)
        exit()
    query = '''SELECT events.year, events.season, events.city
            FROM events'''

    try:
        cursor = connection.cursor()
        cursor.execute(query,) #query for the Olympic game year with athletes name, id, sex, event, sport, and meadal
    except Exception as e:
        print(e)
        exit()
    cnt =1
    for row in cursor:
        year = row[0]
        if year not in years:
                game_dict = {'id': cnt, 'year': row[0], 'season': row[1] ,'city': row[2]}
                years.append(year)
                glist.append(game_dict)
                cnt = cnt + 1
    glist.sort(key=operator.itemgetter('year'))
    connection.close()
    return glist

@app.route('/games')
#sends list of dictionaries with Olympics games information from 1896-2016
def game():
    return json.dumps(game_gen())

@app.route('/nocs')
def noc():
    ''' Returns list of nocs with their abbreviation and fullname '''
    noc_dict = {}
    nlist =[]
    nocs = []

    
    with open('event.csv', mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:  
            noc = row[4]
            if noc not in nocs:
                noc_dict = {'abbreviation': row[5], 'name': noc}
                nocs.append(noc)
                nlist.append(noc_dict)
        nlist.sort(key=operator.itemgetter('name'))
    return json.dumps(nlist)


@app.route('/medalists/games/<games_id>')
def medalists(games_id):
    ''' Sends a list of dictonaries the requested games according to the id given 
    and associated Olympic years. If get parameter is inputed the list of dictonaries 
    will be filtered to only have the games with the specified noc's and game id. 
    '''
    noc = request.args.get('noc', default= '', type=str)
    medalist_dict = {}
    mlist =[]
    check = False
    if noc != '': #check if a noc is given
        check = True
    glist = game_gen()
    for item in glist: # checks for games_id based on the list of games in game_gen()
        if item['id'] == int(games_id):
            game = item['year']
            break

    try:
        connection = psycopg2.connect(database="olympics", user="rodrick", password="Lankford1")
    except Exception as e:
        print(e)
        exit()
    query = '''SELECT athletes.firstname, athletes.lastname, athletes.id, athletes.sex, events.sport, events.event, events.medal, events.NOC
            FROM athletes, events
            WHERE athletes.id = events.athleteid
            AND events.year = %s'''

    try:
        cursor = connection.cursor()
        cursor.execute(query, (game,)) #query for the Olympic game year with athletes name, id, sex, event, sport, and meadal
    except Exception as e:
        print(e)
        exit()

    for row in cursor:
        if (row[6] != 'NA'):
            if check == True:
                if row[-1] == noc:#checks to see if the row has a medal and if it has the correct noc
                    medalist_dict = {'athlete_id': row[2], 'athlete_name': row[0] + ' ' + row[1], 'athlete_sex': row[3], 'sport': row[4], 'event': row[5], 'medal': row[6]}
                    mlist.append(medalist_dict)
            else:
                medalist_dict = {'athlete_id': row[2], 'athlete_name': row[0] + ' ' + row[1], 'athlete_sex': row[3], 'sport': row[4], 'event': row[5], 'medal': row[6]}
                mlist.append(medalist_dict)
    connection.close()
    return json.dumps(mlist)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
