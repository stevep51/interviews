terraform {
  required_version = ">= 1.0"
}

provider "aws" {
  region = us-east-1
}

resource "aws_instance" "web_server" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  
  tags = {
    Name = "Web Server"
    Environment = production
  }
}

resource "aws_s3_bucket" "data" {
  bucket = "my-data-bucket"
  
  tags {
    Name = "Data Bucket"
  }
}

resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Security group for web servers"
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = tcp
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

