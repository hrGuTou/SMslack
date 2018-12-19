# SMslack
This project used MYSQL database and Twilio sms API to build a platform mainly for event organizers to send out notifications and announcements via SMS.

# Database Setup
### Master branch ###
Using Firebase Database<br />
Sign up then download your certificate json file from Firebase and place it in `/Firebase_cred` folder.<br />
Modify `Firebase_cred.py` to include your json path and database url.<br />

### MySQL_database branch ###
Install MYSQL for database management.<br />

# Environment Setup
Have Twilio account ready.<br />
Install ngrok or alternative services to expose localhost.<br />
<br />
For ngrok, use the following command in terminal to start:<br />
`$ ngrok http FLASK_RUNNING_PORT -host-header="localhost:FLASK_RUNNING_PORT"`<br />
Copy generated http link and paste it into your Twilio SMS webhook.<br />

# Usage
Enter Twilio api (account_sid and token) information and Twilio phone number in `control.py`<br />
Fill in database information.<br />
Start app at `/gui/main.py`<br />

All control functions located in `control.py`. Modify if needed.<br />

# Database Tables
1.Announcement<br />
2.GroupMsg<br />
3.Participant<br />
4.PrivateMsg<br />
5.Project<br />
6.Team<br />

# TODO
1.Fix possible bugs and check inputs<br />
2.Rewrite in Express.js and React<br />

# Group Members
Haoran He<br />
Qizhi Zhao<br />
YanFeng Lin<br />
