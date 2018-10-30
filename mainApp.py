from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from parser import *
from database import *
import threading


def infoParser(info, num):
    result = dataParser(info)
    dataRec = {'Name': result[0],
               'Email': result[1],
               'Sex': result[2],
               'Team Name': result[3],
               'Project Name': result[4],
               'Project Status': result[5],
               'PhoneNumber': num}
    print(dataRec)  # for debug
    insINFO(dataRec)


def greeting(res, eventName):
    res.message("Welcome to " + eventName + "! Please copy&paste the following message to fill in and reply. "
                                            "(Keep exact format)")
    res.message("[INFO]\n"
                "Name(first last):\n"
                "Email:\n"
                "Sex(M/F):\n"
                "Team Name:\n"
                "Project Name:\n"
                "Project status(C for complete,I for incomplete):")
    return str(res)


def startApp():
    app = Flask(__name__)

    @app.route('/sms', methods=['POST'])
    def sms():
        num = request.form['From']

        msg = request.form['Body']
        response = MessagingResponse()

        if num not in listofNum:
            res = greeting(response, 'CS336')
            listofNum.append(num)
            return res
        else:
            if msg.rfind("[INFO]") != -1:
                infoParser(msg, num)
            return "OK"

    app_thread = threading.Thread(target=app.run)
    app_thread.daemon = True
    app_thread.start()


listofNum = []


#if __name__ == '__main__':
#    listofNum = []
#    eventName = input("Event Name: ")
#    app = startApp(eventName)
#    makeTable()
#    app.run()
