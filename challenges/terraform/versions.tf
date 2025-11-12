terraform {
  required_version = ">= 1.5.0"

  required_provider {
    aws = {
      source  = "hashicorp/awss"
      version = "~> 5.0"
    }
  }
}
