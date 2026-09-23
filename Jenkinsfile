pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/tanp4577-web/quee1.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Call python module explicitly using its complete default execution syntax
                bat '''
                python -m pip install --upgrade pip --quiet
                python -m pip install -r requirements.txt --quiet
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Invokes pytest directly as a python module to bypass system PATH variable limitations
                bat 'python -m pytest test_app.py'
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
