node ('docker') {
   // Mark the code checkout 'stage'....
   stage 'checkout'

   // Get some code from a GitHub repository
   git url: 'https://github.com/mpenate/CI_PoC'
   sh 'git clean -fdx; sleep 4;'


   stage 'build image'
   // set the version of the build artifact to the Jenkins BUILD_NUMBER so you can
   // map artifacts to Jenkins builds
   sh "docker build . -t bootstrap-sec.labs.stratio.com:5000/microservice-ci-poc:v1"

   stage 'push image'

   sh "docker push bootstrap-sec.labs.stratio.com:5000/microservice-ci-poc:v1"

}
