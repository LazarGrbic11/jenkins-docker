import subprocess

cmd = "wget https://github.com/prometheus/node_exporter/releases/download/v1.5.0/node_exporter-1.5.0.linux-amd64.tar.gz"
subprocess.run(cmd, shell=True)

cmd = "tar xvfz node_exporter-*.tar.gz"
subprocess.run(cmd, shell=True)

cmd = "sudo mv node_exporter-1.5.0.linux-amd64/node_exporter /usr/local/bin"
subprocess.run(cmd, shell=True)

cmd = "rm -r node_exporter-1.5.0.linux-amd64"
subprocess.run(cmd, shell=True)

cmd = "sudo useradd -rs /bin/false node_exporter"
subprocess.run(cmd, shell=True)

cmd = "sudo nano /etc/systemd/system/node_exporter.service"
subprocess.run(cmd, shell=True)


