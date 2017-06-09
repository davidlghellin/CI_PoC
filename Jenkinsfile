node(){
   
   stage('pre-reqs'){
      //prepare our slave container
      sh "apt-get -qq update && apt-get -qq -y install maven"
      sh "pip3 install requests bs4"
      
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
   
   stage('deploy app'){
      sh "python3 test.py master-1.node.paas.labs.stratio.com admin 1234"
   }

}
