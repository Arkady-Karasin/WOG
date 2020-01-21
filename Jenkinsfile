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
			   dir('Build'){
                   bat 'docker build .'
			   }
            }
        }
    }
}
