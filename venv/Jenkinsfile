pipeline {
agent any
    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/Arkady-Karasin/WOG.git'
            }
        }
        stage('docker start') {
            steps {
			   dir('venv'){
                   bat 'docker-compose start'
			   }
            }
        }
        stage('Start e2e') {
		    steps {
                dir('test')
                bat 'python e2e.py'
			}
		}
        stage('docker stop') {
            steps {
			   dir('venv'){
                   bat 'docker-compose stop'
			   }
            }
        }
	}
}