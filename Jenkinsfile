pipeline {
    agent any

    environment {
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
                    if not exist reports mkdir reports
                    behave --junit --junit-directory reports ^
                        -f behave_html_formatter:HTMLFormatter -o reports/html_report.html
                """
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML(target: [
                    reportDir: 'reports',
                    reportFiles: 'html_report.html',
                    reportName: 'BDD Test Report'
                ])
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
