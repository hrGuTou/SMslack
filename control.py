from twilio.rest import Client
from time import strftime, localtime
from mainApp import *
import database


account_sid = ""#HIDDEN
token = ""#HIDDEN
client = Client(account_sid,token)
twilioPhoneNumber = "" #insert your twilio phone number here
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


def start():
    """
        Call this function to start app
        No return
    """
    startApp()

def listAllParticipant():
    """
        ALL DATA UNSORTED
        This function return the list of lists of all participants
        Format will be [Name, Email, PhoneNumber, Sex, TeamName, ProjectName]
    """
    ref = user.get()
    result = []
    for key in ref:
        result.append([ref[key]["Name"],ref[key]["Email"],ref[key]["Phone Number"],ref[key]["Sex"],ref[key]["Team Name"],ref[key]["Project Name"]])
    print(result)
    return result


def names():
    """
        Return all participants' name
    """

    try:
        ref = user.get()
        result = []
        for key in ref:
            result.append(ref[key]["Name"])
        return result

    except Exception as e:
        print(e)



def teams():
    """
        Return all the team name
    """
    try:
        ref = user.get()
        result = []
        for key in ref:
            result.append(ref[key]["Team Name"])
        return set(result)
    except Exception as e:
        print(e)

def listAllProject():
    """
        ALL DATA UNSORTED
        Return a list of all projects information
        Format will be {ProjectName, ProjectStatus, ProjectDue}

        For ProjectStatus, C for completed, I for Incomplete
        ProjectDue contains time format YYYY-MM-DD HH:MM:SS that indicate when project is due. To be assign by event organizer.
    """

    try:
        ref = user.get()
        result = []
        for key in ref:
            result.append([ref[key]["Project Name"],ref[key]["Project Status"]])

        return result

    except Exception as e:
        print(e)

def assignProjectDue(time, projectname):
    """
        To be used by event organizers.

        Input: Project Name and Due date/time
        Format has to be "YYYY-MM-DD HH:MM:SS" ex: 2018-10-8 15:30:00

        No return

        #TODO: check input
    """
    pass

    #cur.execute("UPDATE Project SET ProjectDue = '"+time+"' WHERE ProjectName = '"+projectname+"'; ")
    #db.commit()


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
    try:
        numberTO = []
        for name in participantList:
            ref = user.order_by_child("Name").equal_to(name).get()
            for key in ref:
                numberTO.append(ref[key]["Phone Number"])

        for number in numberTO:
            client.messages.create(
                body=message,
                from_= twilioPhoneNumber,
                to=number
            )

        sentTime = strftime("%Y-%m-%d %H:%M:%S", localtime())

        for number in numberTO:
            user.child(number).child("Message History/Personal").update({
                sentTime:message
            })
    except Exception as e:
        print(e)

def sendGM(message,teamName):

    """
        Send message to one team's all members

        Input:message, a team name in string

            *You can use teams() to get all the team names, then use drop down list to choose send target

        Store sent messages into database for record
        No return
    """
    try:
        numberTO = []
        ref = user.order_by_child("Team Name").equal_to(teamName).get()
        for key in ref:
            numberTO.append(ref[key]["Phone Number"])


        for number in numberTO:
            client.messages.create(
                body = message,
                from_= twilioPhoneNumber,
                to = number
            )

        sentTime = strftime("%Y-%m-%d %H:%M:%S", localtime())

        database.message.child("Group Message").child(teamName).update({
            sentTime:message
        })

    except Exception as e:
        print(e)


def sendAnnouncement(message):
    """
        Make announcement to all participants in the database

        Input:message

        Store sent messages into database for record
        No return
    """
    numberTO = []
    ref = user.get()
    for key in ref:
        numberTO.append(ref[key]["Phone Number"])


    for number in numberTO:
        client.messages.create(
            body = message,
            from_= twilioPhoneNumber,
            to = number
        )

    sentTime = strftime("%Y-%m-%d %H:%M:%S", localtime())

    database.message.child("Announcement").update({
        sentTime:message
    })

def pmHistory():
    """
        No input

        :return: A list of lists of all private messages.
                Format will be [Name, Sent Time, Message]

    """
    try:
        result = []

        ref = user.get()
        for key in ref:
            if "Message History" in ref[key]:
                if "Personal" in ref[key]["Message History"]:
                    for senttime in ref[key]["Message History"]["Personal"]:
                        result.append([ref[key]["Name"], senttime, ref[key]["Message History"]["Personal"][senttime]])

        return result

    except Exception as e:
        print(e)

def gmHistory():
    """
    No input

    :return: A list of lists of all group messages.
            Format will be [Team Name, Sent Time, Message]

    """
    try:
        result = []
        ref = database.message.child("Group Message").get()
        #print(ref)
        for key in ref:
            for time in ref[key]:
                result.append([key, time, ref[key][time]])

        return (result)
    except Exception as e:
        print(e)

def amHistory():
    """
        No input

        :return: A list of lists of all announcement messages.
                Format will be [Sent Time, Message]

    """
    try:
        ref = database.message.child("Announcement").get()
        result = []
        for key in ref:
            result.append([key,ref[key]])
        return result
    except Exception as e:
        print(e)

def explode():
    """
        After event ends, event organizer can completely delete all the personal information
        CAUTION: Display warning before calling this function
                 Deletion can't be undone.

    """
    user.delete()
    message.delete()


    print("DB reset")

if __name__ == "__main__":
    pass
