pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/Garvv09/scientific-calculator-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t calculator .'
            }
        }

    }
}

