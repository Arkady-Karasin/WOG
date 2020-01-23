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
//	post {
    // Always runs. And it runs before any of the other post conditions.
//        always {
      // Let's wipe out the workspace before we finish!
//           deleteDir()
//        }
//	}
}