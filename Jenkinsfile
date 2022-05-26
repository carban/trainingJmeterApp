pipeline {
    agent { dockerfile true }
    parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
    }
    stages {
        stage ("Compile Stage") {
            steps {
                echo 'Compiling'
            }
        }
        stage ("Run Stage") {
            steps {
                echo "Running.... Hello ${params.PERSON}"
            }
        }
        stage ("Report Stage") {
            steps {
                echo 'Reporting'
            }
        }
        stage ("Dockering...."){
            // agent {
            //     docker {image: 'carbanx/jmeter'}
            // }
            steps {
                sh "python -c 'print(2+2)'"
            }
        }
        // stage ("Building docker image"){
        //     steps {
        //         sh """
        //             docker build -t carbanx/jmeter .
        //         """
        //     }
        // }
        // stage ("Running Docker container"){
        //     steps {
        //         sh """
        //             docker run --rm carbanx/jmeter
        //         """
        //     }
        // }

    }
}