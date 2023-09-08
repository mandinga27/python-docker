@Library('pipeline-utils@feat-test') _

pipeline {
  agent any

  stages {
    stage('Cloning') {
        steps {
          git branch: 'main',
          credentialsId: 'jenkins-ec2',
          url: 'https://github.com/mandinga27/mandinga27/python-docker.git'

          script {
		        try {
              // send build started notifications
        		  slackSend (channel: "#jenkins-notifications", color: '#00FF00', message: "Ejecucion : ${env.BUILD_NUMBER} Comenzando! En el primer Stage. ${env.BUILD_URL}")
			        //sh "Stage exitoso: notificacion Slack"
		        }
	          catch(Exception e) {
		          bat 'echo "Job Failed"'
		          currentBuild.result = "FAILURE"
		          slackSend (channel: "#jenkins-notifications", color: '#FF0000', message: "Ejecucion : ${env.BUILD_NUMBER} FAILED! Hubo un error! ${env.BUILD_URL}")
              //sh "Stage con error: notificacion Slack"
            }
        }
      }
    }
    stage('prueba library') {
      steps{
        script{
         hola()
        }
        }
      }
    }
  }
}