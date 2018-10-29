from twilio.rest import Client
from time import strftime, localtime
from main import *

account_sid = ""#HIDDEN
token = ""#HIDDEN
client = Client(account_sid,token)
f = '%Y-%m-%d %H:%M:%S'

"""
    GUI for event organizers will be based on these functions
    Future updates possible
    You need to create the table header corresponding to the format
    
    #ALL FUNCTIONS CHECKED EXCEPT Announcement()
    #WILL BE TESTED
    #CORRECTIONS MADE
    
    TODO: add msg history
    
    Set up MYSQL on localhost
    Don't use root user, create your own
    Create database named on9db using CREATE DATABASE on9db;
"""

db = MySQLdb.connect(
    host="localhost",
    user="GuTou", #change it to your username
    #passwd="" if needed
    db='on9db'
)
cur = db.cursor()

def start(eventName):
    """
        Call this function to start app
        Input: event name in string
        No return
    """
    app = startApp(eventName)
    makeTable()
    app.run()


def listAllParticipant():
    """
        ALL DATA UNSORTED
        This function return the list of lists of all participants
        Format will be [Name, Email, PhoneNumber, Sex, TeamName, ProjectName]
    """
    cur.execute("Select Name,Email,PhoneNumber,Sex,TeamName,ProjectName from Participant natural join Team "
                "natural join Project;")
    result = []
    for row in cur.fetchall():
        result.append(list(row))

    return result

def names():
    """
        Return all participants' name
    """
    cur.execute("SELECT Name FROM Participant")
    return [item[0] for item in cur.fetchall()]

def listAllTeam():
    """
        ALL DATA UNSORTED
        Return a list of all teams information
        Format will be {TeamName, MeetTime}
        MeetTime contains time format YYYY-MM-DD HH:MM:SS that indicates when team will have a meeting
    """
    cur.execute("SELECT TeamName,MeetTime FROM Team")
    return [item[0] for item in cur.fetchall()]

def teams():
    """
        Return all the team name
    """
    cur.execute("SELECT TeamName FROM Team")
    return [item[0] for item in cur.fetchall()]

def listAllProject():
    """
        ALL DATA UNSORTED
        Return a list of all projects information
        Format will be {ProjectName, ProjectStatus, ProjectDue}

        For ProjectStatus, C for completed, I for Incomplete
        ProjectDue contains time format YYYY-MM-DD HH:MM:SS that indicate when project is due. To be assign by event organizer.
    """
    cur.execute("SELECT ProjectName,ProjectStatus,ProjectDue FROM Project")
    return [item[0] for item in cur.fetchall()]

def assignProjectDue(time, projectname):
    """
        To be used by event organizers.

        Input: Project Name and Due date/time
        Format has to be "YYYY-MM-DD HH:MM:SS" ex: 2018-10-8 15:30:00

        No return

        #TODO: check input
    """


    cur.execute("UPDATE Project SET ProjectDue = '"+time+"' WHERE ProjectName = '"+projectname+"'; ")
    db.commit()


def sendPM(message,participantList):
    """
        Send message to one or multiple participants

        Input:message, participant name(s)[HAS TO BE A LIST OF STRING]

            *You can use names() to get all the participant names, then use checkbox to choose send target
            *Checkbox has to return the name(s) in the STRING LIST data type

        Store sent messages into database for record
        No return

        #TODO: list data type check
    """
    numberTO = []
    for name in participantList:
        cur.execute("SELECT PhoneNumber FROM Participant WHERE Name='"+name+"';")
        phoneNum = str(cur.fetchone()[0])
        numberTO.append(phoneNum)

    for number in numberTO:
        client.messages.create(
            body=message,
            from_='+12017209126',
            to=number
        )

    sentTime = strftime("%Y-%m-%d %H:%M:%S", localtime())

    for name in participantList:
        sql = "INSERT INTO PrivateMsg(SentToPerson, SentTime, Message) VALUES (%s,%s,%s);"
        val = (name, sentTime, message)
        cur.execute(sql, val)
        db.commit()



def sendGM(message,teamName):
    """
        Send message to one team's all members

        Input:message, a team name in string

            *You can use teams() to get all the team names, then use drop down list to choose send target

        Store sent messages into database for record
        No return
    """

    cur.execute("SELECT PhoneNumber FROM Team NATURAL JOIN Participant WHERE TeamName = '"+teamName+"';")
    allPhoneNumber = [item[0] for item in cur.fetchall()]

    for number in allPhoneNumber:
        client.messages.create(
            body = message,
            from_= '+12017209126',
            to = number
        )

    sentTime = strftime("%Y-%m-%d %H:%M:%S", localtime())

    sql = "INSERT INTO GroupMsg(SentToTeam, SentTime, Message) VALUES (%s,%s,%s);"
    val = (teamName,sentTime, message)
    cur.execute(sql, val)
    db.commit()


def sendAnnouncement(message):
    """
        Make announcement to all participants in the database

        Input:message

        Store sent messages into database for record
        No return
    """
    cur.execute("SELECT PhoneNumber FROM Participant")
    allPhoneNumber = [item[0] for item in cur.fetchall()]

    for number in allPhoneNumber:
        client.messages.create(
            body = message,
            from_= '+12017209126',
            to = number
        )

    sentTime = strftime("%Y-%m-%d %H:%M:%S", localtime())

    sql = "INSERT INTO Announcement(SentTime, Message) VALUES (%s,%s);"
    val = (sentTime, message)
    cur.execute(sql,val)
    db.commit()

def pmHistory():
    """
        No input

        :return: A list of lists of all private messages.
                Format will be [Name, Sent Time, Message]

    """

    cur.execute("select SentToPerson, SentTime, Message from PrivateMsg;")
    result = []
    for row in cur.fetchall():
        result.append(list(row))

    for data in result:
        date = data[1]
        data[1]=date.strftime(f)

    return result

def gmHistory():
    """
    No input

    :return: A list of lists of all group messages.
            Format will be [Team Name, Sent Time, Message]

    """
    cur.execute("select SentToTeam, SentTime, Message from GroupMsg;")
    result = []
    for row in cur.fetchall():
        result.append(list(row))

    for data in result:
        date = data[1]
        data[1] = date.strftime(f)

    return result

def amHistory():
    """
        No input

        :return: A list of lists of all announcement messages.
                Format will be [Sent Time, Message]

    """
    cur.execute("SELECT SentTime, Message FROM Announcement;")
    result = []
    for row in cur.fetchall():
        result.append(list(row))

    for data in result:
        date = data[0]
        data[0]=date.strftime(f)

    return result

def explode():
    """
        After event ends, event organizer can completely delete all the personal information
        CAUTION: Display warning before calling this function
                 Deletion can't be undone.

    """

    cur.execute("DROP DATABASE on9db")
    db.commit()


