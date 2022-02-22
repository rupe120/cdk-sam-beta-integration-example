$samBuildPath="./.aws-sam/build"
if (Test-Path -Path $samBuildPath) {
    Remove-Item -Recurse -Force $samBuildPath
}

cdk synth

sam build -t ./cdk.out/SampleStack.template.json --use-container