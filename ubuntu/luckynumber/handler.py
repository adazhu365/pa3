import random
import pymysql

con = pymysql.connect('uvaclasses.martyhumphrey.info', 'JoeJackson', 
    'HitSingle1991', 'uvaclasses')

def parseInt(value):
    try:
        return int(valu)
    except ValueError:
        return 100

def lucky_number(event, context):
    intent = event['request']['intent']['name']
    coursenum = event['request']['intent']['slots']['coursenum']['value']
    print(coursenum)
    cur = con.cursor()

    if intent == "GetClass":
        cur.execute("SELECT `Title` FROM `CompSci1192Data` WHERE `Number` = %s LIMIT 1", coursenum)
        input_name = cur.fetchone()
        print(input_name[0])

        response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'The class is '+str(input_name[0]) ,
            }
            }
        }
        
    elif intent == "GetInstructor":
        cur.execute("SELECT `Instructor` FROM `CompSci1192Data` WHERE `Number` = %s LIMIT 1", coursenum)
        input_name = cur.fetchone()
        print(input_name[0])

        response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'The instructor is ' + str(input_name[0]),
            }
            }
        }

    elif intent == "GetSeats":
        cur.execute("SELECT `EnrollmentLimit`-`Enrollment` FROM `CompSci1192Data` WHERE `Number` = %s LIMIT 1", coursenum)
        input_name = cur.fetchone()
        print(input_name[0])

        response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'Number of available seats is: ' + str(input_name[0]),
            }
            }
        }
    return response
