# SMslack
This project used MYSQL database and Twilio sms API to build a platform mainly for event organizers to send out notifications and announcements via SMS.

# Environment Setup
Install MYSQL for database management.
Have Twilio account ready
Install ngrok or alternative services to expose localhost

# Usage
Enter Twilio api (account_sid and token) infomation in control.py
Start app at /gui/main.py
All control functions located in control.py

# Database tables
1.Announcement
2.GroupMsg
3.Participant
4.PrivateMsg
5.Project
6.Team

# TODO
1.Fix possible bugs and check inputs
2.Rewrite in Express.js and React
