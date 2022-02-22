
# Welcome to your CDK Python project with beta SAM integration!


## Prerequisites
CDK
https://aws.amazon.com/getting-started/guides/setup-cdk/

AWS SAM 
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html


## Overview
This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies to the CDK app, for example other CDK libraries, just add
them to your `requirements.txt` file and rerun the `pip install -r requirements.txt`
command.

Now the lambda can be build with it's dependencies. The `sam-build.ps1` script runs the following commands.

```powershell
$samBuildPath="./.aws-sam/build"
if (Test-Path -Path $samBuildPath) {
    Remove-Item -Recurse -Force $samBuildPath
}

cdk synth

sam build -t ./cdk.out/SampleStack.template.json --use-container
``` 

The SAM build folder is cleared to support the `sample\stack\sam_helper.py` logic. 

The helper is used both during `cdk synth` and `cdk deploy`. During synth we want the `sample\function` content used for the the lambda. During deploy we want the `.aws-sam\build\<my-function>` content used. The helper looks for the existence of the `.aws-sam\build\<my-function>` folder, and if it doesn't exists it uses the lambda's default content.

After SAM build has been run a standard CDK deploy can be used.

```
cdk deploy
```


## Useful CDK commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
