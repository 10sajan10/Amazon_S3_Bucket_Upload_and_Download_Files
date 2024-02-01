# S3 File Upload and Download

This repository contains Python scripts for managing files in an Amazon S3 bucket. The provided scripts offer functionalities for uploading files to S3, listing files in an S3 bucket, and downloading files from S3.

## Usage

- **Upload Script:** `s3_upload_script.py` uploads local files to the specified S3 bucket.
  
  ```bash
  python s3_upload_script.py --bucket_name YOUR_BUCKET_NAME --directory_to_watch YOUR_LOCAL_DIRECTORY --aws_access_key YOUR_ACCESS_KEY --aws_secret_access_key YOUR_SECRET_ACCESS_KEY
  
- **Download Script:** `s3_download_script.py` download files from S3 bucket to the specified local directory.

  ```bash
  python s3_download_script.py --bucket_name YOUR_BUCKET_NAME --local_directory YOUR_LOCAL_DIRECTORY --aws_access_key YOUR_ACCESS_KEY --aws_secret_access_key YOUR_SECRET_ACCESS_KEY
