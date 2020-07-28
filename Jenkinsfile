pipeline{
 agent any

 stages{
  stage('Build Package')
          {
           steps{

           sh '''npm install'''
           }

          }
  stage('Start Application')
          {
           steps{

            sh '''node server.js'''
           }
          }
 }

 }
