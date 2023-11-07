[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/UxpU_KWG)
# Setup instructions

Step 1: Clone the repository

Step 2: Populate our project's Firestore Database with questions from LintCode 
```
cd assignment6

python3 main.py
```

# Modifying the serverless function
We are using Cloud Functions for Firebase. For security purposes, the only people who can modify the serverless function are those with the "Cloud Functions Developer" role for our Firebase project.

```
firebase init

#After firebase init, a selection menu will appear, choose the Firebase Functions feature, and associate the project directory with the CS3219 G56 project. Next, choose Overwrite the existing codebase to modify the serverless function in the index.js file under the functions folder.

#Currently the function adds a question in json format to our Firestore database. Make the appropriate changes to index.js.

firebase deploy

#A new link will be generated for the serverless function. Edit the main.py file and change the POST_URL link to make the script send questions from Lintcode to the new serverless function endpoint.

python3 main.py
```