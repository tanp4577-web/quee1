pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/tanp4577-web/quee1.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                bat 'pytest'
            }
        }
    }
    post {
        success {
            echo 'Build succeeded: all tests passed.'
        }
        failure {
            echo 'Build failed: check the test output above.'
        }
    }
}
