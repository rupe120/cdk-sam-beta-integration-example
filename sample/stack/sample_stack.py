from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_
)
from constructs import Construct
from .sam_helper import get_lambda_src_path

class SampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambdaId = "MyFunction"

        # Find the folder in .aws-sam/build/data-lake-S3DmsTriggerStack????? that represents the current Lambda, or just return the standard path
        lambdaSourcePath = get_lambda_src_path(construct_id, lambdaId, "sample/function")
        
        # The code that defines your stack goes here
        my_function = lambda_.Function(self, lambdaId,
            function_name=f"{lambdaId}-lambda",
            code=lambda_.Code.from_asset(lambdaSourcePath),
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="app.lambda_handler"
        )

        # example resource
        # queue = sqs.Queue(
        #     self, "SampleQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
