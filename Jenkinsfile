pipeline {
    agent any // Runs on the first available agent, fixing the "doesn't have label" error

    stages {
        stage('Checkout') {
            steps {
                // Clones your specific GitHub repository automatically
                git url: 'https://github.com', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Uses Windows batch commands to safely install requirements without prompting
                bat '''
                python -m pip install --upgrade pip --quiet
                pip install -r requirements.txt --quiet
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Executes the test suite via pytest
                bat 'pytest test_app.py'
            }
        }
    }

    post {
        success {
            echo '===================================='
            echo 'SUCCESS: All stages passed perfectly!'
            echo '===================================='
        }
        failure {
            echo '===================================='
            echo 'FAILURE: The build or tests failed!'
            echo '===================================='
        }
    }
}
