import boto3

def list_all_files(bucket_name, s3):
    """
    List all files in the specified S3 bucket.

    Parameters:
        bucket_name (str): The name of the S3 bucket.
        s3 (boto3.client): The S3 client.

    Returns:
        set: A set containing the names of all files in the S3 bucket.
    """
    continuation_token = None
    uploaded_files = set()

    while True:
        list_objects_params = {'Bucket': bucket_name}
        if continuation_token:
            list_objects_params['ContinuationToken'] = continuation_token

        response = s3.list_objects_v2(**list_objects_params)

        objects = response.get('Contents', [])

        if len(objects) > 0:
            for obj in objects:
                key = obj['Key']
                uploaded_files.add(key)

            if response.get('IsTruncated', False):
                continuation_token = response['NextContinuationToken']
            else:
                break
        else:
            break

    return uploaded_files

def upload_to_s3(local_file_path, s3_file_name, bucket_name, s3):
    """
    Upload a local file to the specified S3 bucket.

    Parameters:
        local_file_path (str): The path to the local file.
        s3_file_name (str): The name to be used for the file in S3.
        bucket_name (str): The name of the S3 bucket.
        s3 (boto3.client): The S3 client.
    """
    try:
        s3.upload_file(local_file_path, bucket_name, s3_file_name)
        print(f'Uploaded {local_file_path} to {bucket_name}/{s3_file_name}')
    except Exception as e:
        print(f'Error uploading {local_file_path} to S3: {e}')