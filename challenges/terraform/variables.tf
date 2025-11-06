variable "instance_count" {
  type        = number
  description = "Number of instances to create"
  default     = 1
}

variable "environment" {
  type        = string
  description = "Environment name"
  # Missing default value
}

variable "region" {
  type = string
  default = "us-east-1"
}

variable "allowed_cidrs" {
  type    = list
  default = ["10.0.0.0/8"]
}

