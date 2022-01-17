pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE:$BUILD_NUMBER .'
        sh 'docker login -u "michaelouan26" -p "LXC5kdes:_U+e_="'
        sh 'docker push $DOCKER_IMAGE:$BUILD_NUMBER'
        sh 'docker rmi $DOCKER_IMAGE:$BUILD_NUMBER'
      }
    }

    stage('deploy') {
      steps {
        sh 'envsubst < pod.yaml | kubectl apply --kubeconfig /pathToKubeConfig -f -n test -'
      }
    }

  }
  environment {
    DOCKER_IMAGE = 'michaelouan26/simpple-flask-app'
  }
}
