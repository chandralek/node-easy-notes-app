pipeline{
 agent any

 stages{
  stage('Build Package')
          {
           sh '''  npm install '''
          }
  stage('Start Application')
          {
           sh ''' node server.js '''
          }
 }

 }
