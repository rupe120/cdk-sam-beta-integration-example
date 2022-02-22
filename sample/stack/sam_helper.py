from os import listdir, path
from os.path import isdir, join

def get_lambda_src_path(construct_id, lambda_id, lambda_source_path):
    lambda_folder_starts_with = lambda_id.replace("-", "")
    stack_build_path = "./.aws-sam/build"
    lambda_final_source_path = lambda_source_path 

    print(f"Testing for paths starting with {lambda_folder_starts_with} in {stack_build_path}")

    if(path.exists(stack_build_path)):
        built_functions = [diritem for diritem in listdir(stack_build_path) if isdir(join(stack_build_path, diritem)) and diritem.startswith(lambda_folder_starts_with)]

        if len(built_functions) > 0:
            lambda_final_source_path = join(stack_build_path, built_functions[0])

    print(f"{lambda_id} Source Path")
    print(lambda_final_source_path)

    return lambda_final_source_path