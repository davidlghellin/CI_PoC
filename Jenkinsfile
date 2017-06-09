node('docker'){
   
   stage('pre-reqs'){
      //prepare our slave container
      sh "apt-get -qq update && apt-get -qq -y install maven python-dev libxml2-dev libxslt1-dev zlib1g-dev"
      sh "pip3 install requests bs4 lxml" 
   }
   
   stage('checkout'){      
      // Get some code from a GitHub repository
      git url: 'https://github.com/mpenate/CI_PoC'
      sh 'git clean -fdx; sleep 4;'    
   }
   
   stage('package'){
      sh "mvn -q clean package"    
   }

   stage('build image'){
   // set the version of the build artifact to the Jenkins BUILD_NUMBER so you can
   // map artifacts to Jenkins builds
      sh "docker build . -t bootstrap-sec.labs.stratio.com:5000/microservice-ci-poc:v1"
   }

   stage('push image'){
      sh "docker push bootstrap-sec.labs.stratio.com:5000/microservice-ci-poc:v1"
   }
   
   stage('test'){
      withCredentials([string(credentialsId: 'admin', variable: 'PW1')]) {
         sh "python3 test.py master-1.node.paas.labs.stratio.com admin '$PW1'"
      }
   }
   
   stage('deploy'){
       withCredentials([string(credentialsId: 'admin', variable: 'PW1')]) {
         sh "python3 deploy.py master-1.node.paas.labs.stratio.com admin '$PW1'"
      }
   }

}
