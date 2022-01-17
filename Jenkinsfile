pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE:$BUILD_NUMBER .'
        sh 'docker push $DOCKER_IMAGE:$BUILD_NUMBER'
        sh 'docker rmi $DOCKER_IMAGE:$BUILD_NUMBER'
      }
    }

    stage('deploy') {
      steps {
     docker.withRegistry('https://hub.docker.com/repository/', '') {

        def customImage = docker.build("my-image:${env.BUILD_ID}")

        /* Push the container to the custom Registry */
        customImage.push()
    }
        sh 'envsubst < pod.yaml | kubectl apply --kubeconfig /pathToKubeConfig -f -n test -'
      }
    }

  }
  environment {
    DOCKER_IMAGE = 'michaelouan26/simpple-flask-app'
  }
}
