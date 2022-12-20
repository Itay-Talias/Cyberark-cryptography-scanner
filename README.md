# Cyberark-cryptography-scanner
## Frontend in react
cd to frontend folder and than run the command npm start

## Technologies
<img align="left" alt="react" width="70px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/react/react.png" />

<img align="left" alt="python" width="70px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />

<img align="left" alt="mongodb" width="70px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/mongodb/mongodb.png" />

<br />
<br />
## About The Project

WolfsonBuddy is a web application designed to support the patient from after calling the appointment until the end of the treatment. This application includes applications for navigating to the hospital, getting information about the doctor who treats the patient, activities for the waiting time, and eventually answering a survey to measure patient's satisfaction.
The application support two kinds of users: The patients, which the above application is aiming for, and the hospital staff, which have the option to edit and add information to the users' screens, regarding information about the staff, surveys, news, and updates.


## Getting Started

### Prerequisites

1) Install node.js   https://nodejs.org/en/download/  <br>
2) Make sure that npm is well installed   https://www.npmjs.com/get-npm  <br>


### Download

Options to download the app: <br>

- Clone the repository https://github.com/Adi-Shuker/WolfsonBuddy.
- Download the zip.


### Create the database

Go to the file https://github.com/Adi-Shuker/WolfsonBuddy/blob/2f131de8886863d903cca292afe94c534b01041a/server/config/db.config.js, you can change there the configuration to your user in mysql

1) Create schema called "wolfson_db" in your mysql
2) Run "npm run migrate" on the terminal (for download flyway)
3) Run "npm run migrate" on the terminal again (for create all the tables)


### Usage

1) Enter in the command line of the cloned repository <br>
2) Run the following commands on one terminal<br>

```bash
cd server
npm install
npm start
```

 3) Run the following commands on another terminal<br>

```bash
cd client
npm install
npm start
```

4) Open the browser. The application will run on a new tab.


## DataBase UML:

<br>   

![image](https://user-images.githubusercontent.com/71780251/189334526-ba22ba07-d9ad-4f71-90be-3fcda53ae59c.png)

<br>

 
 # Swagger App

The swagger app can help the developers to understand how the app is designed and work, from the side of the REST API and the database

## How to use it
To run this app you need to go to the swagger app folder and run npm install, and then run npm start.
The app will open in the browser after that.
Now you can see the different API requests, add parameters if need and test the different requests. Note that the 'post' and 'delete' requests can change your local database!
 

# Contributors
This program was developed by Adi-Shuker, naamaU, omer-zivoni

