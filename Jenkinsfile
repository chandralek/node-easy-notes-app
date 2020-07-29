pipeline{
 agent any

 stages{
  stage('Build Image')
          {
           steps{

           sh '''sudo docker-compose build'''
           }

          }
  stage('Start Application')
          {
           steps{

            sh '''sudo docker-compose up'''
           }
          }
   stage('Run Api Tests')
           {
             steps{
               sh '''python3 apiTest.py'''
             }
           }
 }

 }
