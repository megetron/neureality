provider "aws" {
  region = var.region
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.medium"
  key_name      = var.key_pair_name

  vpc_security_group_ids = [aws_security_group.example.id]

  tags = {
    Name = "example-instance"
  }
}

resource "aws_security_group" "example" {
  name        = "example-security-group"
  description = "Allow incoming traffic on port 5000"

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


provisioner "remote-exec" {
  inline = [
    "cd api",
    "docker-compose up -d"
  ]
}
