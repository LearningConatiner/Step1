pipeline {
    agent { docker 'python:2.7.12' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                ocker build -t helloworld
                docker run -d -p 4000:4000 helloworld
            }
        }
    }
}
