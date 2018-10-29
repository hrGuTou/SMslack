import MySQLdb

# TODO RETURN THE INSERTION STATUS
# REDESIGN THE TABLES
# TODO ADD TABLE LINKERS

db = MySQLdb.connect(
    host="localhost",
    user="GuTou",
    db='on9db'
)
cur = db.cursor()


def makeTable():
    try:
        participant = "CREATE TABLE IF NOT EXISTS Participant(id INT PRIMARY KEY AUTO_INCREMENT," \
                      "Name TEXT NOT NULL," \
                      "Email VARCHAR(320) NOT NULL," \
                      "PhoneNumber VARCHAR(12) NOT NULL," \
                      "Sex CHAR(1) NOT NULL," \
                      "TeamID INT," \
                      "ProjectID INT," \
                      "UNIQUE (PhoneNumber));"

        team = "CREATE TABLE IF NOT EXISTS Team(TeamID INT PRIMARY KEY AUTO_INCREMENT," \
               "TeamName VARCHAR(320) NOT NULL," \
               "MeetTime DATETIME," \
               "UNIQUE (TeamName));"

        project = "CREATE TABLE IF NOT EXISTS Project(ProjectID INT PRIMARY KEY AUTO_INCREMENT," \
                  "ProjectName VARCHAR(320) NOT NULL," \
                  "ProjectStatus CHAR(1) NOT NULL," \
                  "ProjectDue DATETIME," \
                  "UNIQUE (ProjectName));"

        groupMsg = "CREATE TABLE IF NOT EXISTS GroupMsg(MsgID INT PRIMARY KEY AUTO_INCREMENT," \
                   "SentToTeam VARCHAR(320) NOT NULL," \
                   "SentTime TIMESTAMP NOT NULL," \
                   "Message TEXT NOT NULL," \
                   "FOREIGN KEY (SentToTeam) REFERENCES Team (TeamID))"

        privateMsg = "CREATE TABLE IF NOT EXISTS PrivateMsg(MsgID INT PRIMARY KEY AUTO_INCREMENT," \
                     "SentToPerson VARCHAR(320) NOT NULL," \
                     "SentTime TIMESTAMP NOT NULL," \
                     "Message TEXT NOT NULL," \
                     "FOREIGN KEY (SentToPerson) REFERENCES Participant (id))"

        announcement = "CREATE TABLE IF NOT EXISTS Announcement(MsgID INT PRIMARY KEY AUTO_INCREMENT," \
                       "SentTime TIMESTAMP NOT NULL," \
                       "Message TEXT NOT NULL)"

        cur.execute(participant)
        cur.execute(team)
        cur.execute(project)
        cur.execute(groupMsg)
        cur.execute(privateMsg)
        cur.execute(announcement)
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
        return None


def insINFO(data):
    try:
        cur.execute("INSERT INTO Team(TeamName) VALUES ('"+data['Team Name']+"')")
        db.commit()
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
        pass

    try:
        projectINFO = "INSERT INTO Project(ProjectName, ProjectStatus) VALUES (%s,%s);"
        projectVal = (data['Project Name'], data['Project Status'])
        cur.execute(projectINFO, projectVal)
        db.commit()
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
        pass

    try:
        personalINFO = "INSERT INTO Participant(Name, Email, PhoneNumber, Sex) VALUES (%s,%s,%s,%s);"
        personalVal = (data['Name'], data['Email'], data['PhoneNumber'], data['Sex'])
        cur.execute(personalINFO, personalVal)
        db.commit()

        cur.execute("SELECT TeamID FROM Team WHERE TeamName = '"+data['Team Name']+"';")
        row = cur.fetchone()
        teamid = row[0]

        cur.execute("SELECT ProjectID FROM Project WHERE ProjectName = '"+data['Project Name']+"';")
        row0 = cur.fetchone()
        projectid = row0[0]

        cur.execute("UPDATE Participant SET TeamID = '"+str(teamid)+"' WHERE Name = '"+data['Name']+"';")
        cur.execute("UPDATE Participant SET ProjectID = '"+str(projectid)+"' WHERE Name = '"+data['Name']+"';")
        db.commit()

    except(MySQLdb.Error,MySQLdb.Warning) as e:
        print(e)
        return None


