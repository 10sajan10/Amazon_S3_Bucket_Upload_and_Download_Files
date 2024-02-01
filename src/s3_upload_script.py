# s3_upload_script.py
import os
import argparse
import time
import boto3
from s3_utils import list_all_files, upload_to_s3

def main():
    """
    Main function to run the S3 file upload script.

    Parses command line arguments, initializes the S3 client, lists existing files in the S3 bucket,
    watches the local directory for new files, and uploads them to the S3 bucket.
    """
    # Default values if not provided via command line or modified here
    bucket_name = "your_default_bucket_name"
    directory_to_watch = "your_default_local_directory_path"
    aws_access_key_id = "your_default_access_key_id"
    aws_secret_access_key = "your_default_secret_access_key"

    # Parse command line arguments if available
    parser = argparse.ArgumentParser(description='Upload files to S3')
    parser.add_argument('--bucket_name', required=False, help='S3 bucket name')
    parser.add_argument('--directory_to_watch', required=False, help='Local directory to watch for new files')
    parser.add_argument('--aws_access_key', required=False, help='AWS Access Key ID')
    parser.add_argument('--aws_secret_access_key', required=False, help='AWS Secret Access Key')

    args = parser.parse_args()

    # Update values if provided via command line
    if args.bucket_name:
        bucket_name = args.bucket_name
    if args.directory_to_watch:
        directory_to_watch = args.directory_to_watch
    if args.aws_access_key:
        aws_access_key_id = args.aws_access_key
    if args.aws_secret_access_key:
        aws_secret_access_key = args.aws_secret_access_key

    # Initialize S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    while True:
        # List all files in the S3 bucket
        uploaded_files = list_all_files(bucket_name, s3)

        # Check for new files in the local directory
        files = os.listdir(directory_to_watch)
        new_files = [file_name for file_name in files if os.path.isfile(os.path.join(directory_to_watch, file_name)) and file_name not in uploaded_files]

        if new_files:
            print(f'New files detected: {new_files}')

            for file_name in new_files:
                local_file_path = os.path.join(directory_to_watch, file_name)
                s3_file_name = file_name

                # Upload the new file to S3
                upload_to_s3(local_file_path=local_file_path, s3_file_name=s3_file_name, bucket_name=bucket_name, s3=s3)

                # Update the set of uploaded files
                uploaded_files.add(s3_file_name)

        # Pause for a specified duration before checking again
        time.sleep(60)  # Adjust the duration as needed

if __name__ == "__main__":
    main()
