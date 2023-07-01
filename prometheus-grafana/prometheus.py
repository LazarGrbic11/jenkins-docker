import subprocess

cmd = "wget https://github.com/prometheus/prometheus/releases/download/v2.37.6/prometheus-2.37.6.linux-amd64.tar.gz"
subprocess.run(cmd, shell=True)

cmd = "tar xvfz prometheus-*.tar.gz"
subprocess.run(cmd, shell=True)

cmd = "rm prometheus-*.tar.gz"
subprocess.run(cmd, shell=True)

cmd = "sudo mkdir /etc/prometheus /var/lib/prometheus"
subprocess.run(cmd, shell=True)

cmd = "cd prometheus-2.37.6.linux-amd64"
subprocess.run(cmd, shell=True)

cmd = "sudo mv prometheus promtool /usr/local/bin/"
subprocess.run(cmd, shell=True)

cmd = "sudo mv prometheus.yml /etc/prometheus/prometheus.yml"
subprocess.run(cmd, shell=True)

cmd = "sudo mv consoles/ console_libraries/ /etc/prometheus/"
subprocess.run(cmd, shell=True)

cmd = "sudo useradd -rs /bin/false prometheus"
subprocess.run(cmd, shell=True)

cmd = "sudo chown -R prometheus: /etc/prometheus /var/lib/prometheus"
subprocess.run(cmd, shell=True)

cmd = "sudo nano /etc/systemd/system/prometheus.service"
subprocess.run(cmd, shell=True)

