pipeline {
agent any
    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/Arkady-Karasin/JenkinsTest.git'
            }
        }
        stage('build') {
            steps {
			   dir('Build/venv'){
                   bat 'docker-compose up'
			   }
            }
        }
		stage('Start browser') {
		    steps {
			    bat 'python e2e.py'
			}
		}
	}
}
