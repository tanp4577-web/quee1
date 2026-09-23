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
                bat 'python -m pip install -r requirements.txt --quiet'
            }
        }
        stage('Run Unit Tests') {
            steps {
                bat 'python -m pytest -v test_app.py'
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
