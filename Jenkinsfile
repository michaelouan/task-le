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
        sh 'echo \'$BUILD_NUMBER\''
        sh 'cat pod.yaml | sed "s/{{BUILD_NUMBER}}/$BUILD_NUMBER/g" | kubectl apply --kubeconfig /pathToKubeConfig -f -n test -'
        sh 'echo \'envsubst < pod.yaml\''
      }
    }

  }
  environment {
    DOCKER_IMAGE = 'michaelouan26/simpple-flask-app'
  }
}
