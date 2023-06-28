# About the project

A small project I created, in order to learn some basics in Jenkins, Ansible and Docker, Point was, to create a pipeline between my repo and the instance hosting a simple HTML page with Nginx 

## Contents

It contains the following

- `ansible` folder, which contains 2 playbooks to install docker and jenkins
- `docker` folder, which contains a docker-compose file with a Nginx image
- `Jenkins` folder, which contains a XML file, since I was using a job to trigger the builds
- `Nginx` folder, which contains a nginx.conf
- index.html, a page hosted by the Nginx

## Result

The HTML page is currently hosted at [http://167.99.242.146:90](http://167.99.242.146:90)

