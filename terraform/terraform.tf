terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
    }
  }
}
variable "do_token" {
  type = string
}
provider "digitalocean" {
  token = var.do_token
}

resource "digitalocean_volume" "testvolume" {
  name      = "testvolume"
  region    = "fra1"
  size      = 25
  filesystem_type = "ext4"
}

resource "digitalocean_droplet" "testprojekat" {
  name           = "jenkins-droplet"
  region         = "fra1"
  size           = "s-2vcpu-2gb"
  image          = "ubuntu-18-04-x64"
  volume_ids     = [digitalocean_volume.testvolume.id]
}
output "droplet_ip" {
  value = digitalocean_droplet.testprojekat.ipv4_address
}
