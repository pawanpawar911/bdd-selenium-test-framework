pipeline {
    agent any

    environment {
        // Escape backslashes for Windows path
        PYTHON = "C:\\Users\\Pawan.Pawar\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat """
                    %PYTHON% --version
                    %PYTHON% -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    call venv\\Scripts\\activate
                    behave -f pretty -f junit -o reports
                """
            }
        }

        stage('Archive Reports') {
            steps {
                junit 'reports/*.xml'
                archiveArtifacts artifacts: 'reports/**', fingerprint: true
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            bat 'rmdir /s /q venv'
        }
        success {
            echo "✅ Tests Passed!"
        }
        failure {
            echo "❌ Tests Failed!"
        }
    }
}
