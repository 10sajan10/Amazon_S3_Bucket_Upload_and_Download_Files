import os
import argparse
import boto3
from s3_utils import list_all_files

def main():
    """
    Main function to run S3 Download script.

    Parses command line arguments, initializes the S3 client, lists existing files in the S3 bucket,
    downloads them to the local directory, and prints a message for each downloaded file.
    """
    # Default values if not provided via command line or modified here
    bucket_name = "your_default_bucket_name"
    local_directory = "your_default_local_directory_path"
    aws_access_key_id = "your_default_access_key_id"
    aws_secret_access_key = "your_default_secret_access_key"

    # Parse command line arguments if available
    parser = argparse.ArgumentParser(description='Download files from S3')
    parser.add_argument('--bucket_name', required=False, help='S3 bucket name')
    parser.add_argument('--local_directory', required=False, help='Local directory to save downloaded files')
    parser.add_argument('--aws_access_key', required=False, help='AWS Access Key ID')
    parser.add_argument('--aws_secret_access_key', required=False, help='AWS Secret Access Key')

    args = parser.parse_args()

    # Update values if provided via command line
    if args.bucket_name:
        bucket_name = args.bucket_name
    if args.local_directory:
        local_directory = args.local_directory
    if args.aws_access_key:
        aws_access_key_id = args.aws_access_key
    if args.aws_secret_access_key:
        aws_secret_access_key = args.aws_secret_access_key

    # Initialize S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    
    # Download each file from the S3 bucket to the local directory
    for file in list_all_files(bucket_name, s3):
        local_file_path = os.path.join(local_directory, os.path.basename(file))
        s3.download_file(bucket_name, file, local_file_path)
        print(f"Downloaded: {file} to {local_file_path}")

if __name__ == "__main__":
    main()
