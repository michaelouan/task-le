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
        kubeconfig(serverUrl: 'https://127.0.0.1:63440', credentialsId: 'root', caCertificate: '-----BEGIN CERTIFICATE----- MIIDBjCCAe6gAwIBAgIBATANBgkqhkiG9w0BAQsFADAVMRMwEQYDVQQDEwptaW5p a3ViZUNBMB4XDTIxMTEwMTE3MjMyNloXDTMxMTAzMTE3MjMyNlowFTETMBEGA1UE AxMKbWluaWt1YmVDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAL/z yL0GVknHDBxj+RYNGvabchBFOfsolfV3/YpGEb4Ti7iwibl1RMnLAcjhK0dTynDH ZrNRDkqxdELIwsznPNDhRLGl8qvId02MSZtNI3MZQK8L1hHXGO7dufWqTrOBVa7s okdFqpnTkJGe8wnLOHb8EdDClZpS+ft9SfBzkhU3Q+CsJSjJ+bs+5y/01s0MZlgz M5pjroVUk8LJzVw+2zUccmSZXNfXDrAG0egf6W9GT7JG65ZtbU6pIss7ft+L2QHR ocfxgsal9PfBkYSWiFXjdebcEB312O0iLEVpc6Ou7IHTELPbpLfPNRUQWjtiLG7j 4ovt+6sw3EHnGTyg8XMCAwEAAaNhMF8wDgYDVR0PAQH/BAQDAgKkMB0GA1UdJQQW MBQGCCsGAQUFBwMCBggrBgEFBQcDATAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQW BBSIpR1Hk+99Q7cZneHeT8XFRRS9kDANBgkqhkiG9w0BAQsFAAOCAQEAjqq7i4ii k3WfqUpe9vnCsV7c/LCOuyUt3AO/anYAKFI8rkXFLyH5milByh/LuBEiz/1+y7ot Qp8fm52SKVbJ8tkTan2xAp2jTXe0i6A8mBFQp5e/2a1vAlaeojIiSRrEOOLxpQfV cm+kj0zZAG2s35p+jsElfGU2G95mQBdvhf4idDJWPBZCaQRz4r/T4maCT5+K5+vF FvyGfY/7RroS2Bmg6PeNRD76aiCGFrBQmmDj51A9vVRTBRLkDF0EV6DBOxKXmAc5 PlpHa59FomIvsCJvDLyCsl727OpknTrlXc1/9CivOZenYvdsOlm/ra4+OR3+oSlr upk1M9n+qzRTNA== -----END CERTIFICATE-----') {
          sh 'kubectl get pods -n test'
        }

        sh 'envsubst < pod.yaml | kubectl apply --kubeconfig /pathToKubeConfig -f -n test -'
      }
    }

  }
  environment {
    DOCKER_IMAGE = 'michaelouan26/simpple-flask-app'
  }
}
