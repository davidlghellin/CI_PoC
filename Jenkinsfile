node {
   // Mark the code checkout 'stage'....
   stage 'checkout'

   // Get some code from a GitHub repository
   git url: 'https://github.com/mpenate/CI_PoC'
   sh 'git clean -fdx; sleep 4;'


   stage 'build image'
   // set the version of the build artifact to the Jenkins BUILD_NUMBER so you can
   // map artifacts to Jenkins builds
   sh "docker build . -t qa.stratio.com/stratio/ci_poc:test"

   stage 'push image'

   sh "docker push qa.stratio.com/stratio/ci_poc:test"

}