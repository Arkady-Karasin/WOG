pipeline {
agent any
    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/Arkady-Karasin/JenkinsTest.git'
            }
        }
		stage('Start e2e') {
		    steps {
			    build 'Check WoG score'
			}
		}
        stage('build') {
            steps {
			   dir('Build/venv'){
                   bat 'docker-compose up'
			   }
            }
        }
	}
}