pipeline {
    agent { label 'standard-slave' }
    parameters {
        choice(name: 'TEST', choices: ['normal', 'stress', 'load', 'peaks', 'wordLoad'], description: 'Select a test')
        string(name: 'TIME', defaultValue: '60', description: 'Test time')
        string(name: 'HOST', defaultValue: '', description: 'Host address')
        string(name: 'PORT', defaultValue: '8080', description: 'Port number')
    }
    stages {
        stage ("Building docker image"){
            steps {
                sh """
                    docker build -t carbanx/jmeter .
                """
            }
        }
        stage ("Checking Container"){
            steps {
                sh """
                    docker run --rm carbanx/jmeter
                """
            }
        }
        stage ("Running Docker container"){
            steps {
                sh """
                    docker run -it --rm carbanx/jmeter python testingScript.py ${params.TEST}" ${params.TIME}" ${params.HOST}" ${params.PORT}"
                """
            }
        }

    }
}