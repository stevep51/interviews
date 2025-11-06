output "instance_id" {
  value = aws_instance.web_server.id
  description = "ID of the EC2 instance"
}

output "bucket_name" {
  value       = aws_s3_bucket.data.bucket
  description = "Name of the S3 bucket"
}

output "security_group_id" {
  value = aws_security_group.web.id
}

