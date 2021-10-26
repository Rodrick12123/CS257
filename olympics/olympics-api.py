
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


@app.route('/games')
#sends list of dictionaries with Olympics games information from 1896-2016
def game():
    game_dict = {}
    glist =[]
    years = []
    with open('event.csv', mode='r') as infile:
        reader = csv.reader(infile)
        # for row in reader:  
        #     index = int(row[0])
        #     year = int(row[7])
        #     
    #         game_dict = {'id': index, 'year': row[7], 'season': row[8] ,'city': row[9]}
    #         years.append(year)
    #         glist.append(game_dict)
        #     glist.sort(key=operator.itemgetter('year'))

        for row in reader:  
            index = int(row[0])
            year = int(row[7])
            if year not in years:
                game_dict = {'id': index, 'year': row[7], 'season': row[8] ,'city': row[9]}
                years.append(year)
                glist.append(game_dict)
        glist.sort(key=operator.itemgetter('year'))
        cnt = 1
        for g in glist:
            g['id'] = cnt
            cnt = cnt + 1
    return json.dumps(glist)

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

#fix this does not work with the git parameter
@app.route('/medalists/games/<games_id>?[noc=noc_abbreviation]')
def medalists(games_id):
    ''' Sends a list of dictonaries the requested games according to the id given 
    and associated Olympic years. If get parameter is inputed the list of dictonaries 
    will be filtered to only have the games with the specified noc's and game id. 
    '''
    noc = request.args.get('noc')
    medalist_dict = {}
    mlist =[]
    check = False
    if noc is not None: #check if a noc is given
        check = True
        noc.lower()
    with open('event.csv', mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:  
            if row[0] == games_id:
                game = int(row[7]) #saves the year of the inputed games id
                break
    try:
        connection = psycopg2.connect(database="olympics", user="rodrick", password="Lankford1")
    except Exception as e:
        print(e)
        exit()
    query = '''SELECT athletes.firstname, athletes.lastname, athletes.id, athletes.sex, events.sport, events.event, events.medal
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
        if check == True:
            if row[6] != 'NA' and row[5].lower() == noc: #checks to see if the row has a medal and if it has the correct noc
                medalist_dict = {'athlete_id': row[2], 'athlete_name': row[0] + ' ' + row[1], 'athlete_sex': row[3], 'sport': row[4], 'event': row[5], 'medal': row[6]}
                mlist.append(medalist_dict)
        else:
            if row[6] != 'NA': 
                medalist_dict = {'athlete_id': row[2], 'athlete_name': row[0] + ' ' + row[1], 'athlete_sex': row[3], 'sport': row[4], 'event': row[5], 'medal': row[6]}
                mlist.append(medalist_dict)
    return json.dumps(mlist)


# @app.route('/help')
# def get_help():
#     return flask.render_template('help.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
