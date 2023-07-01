import subprocess

cmd = "sudo apt-get install -y apt-transport-https software-properties-common"
subprocess.run(cmd, shell=True)

cmd = "sudo wget -q -O /usr/share/keyrings/grafana.key https://apt.grafana.com/gpg.key"
subprocess.run(cmd, shell=True)

cmd = 'echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list'
subprocess.run(cmd, shell=True)

cmd = "sudo apt-get update"
subprocess.run(cmd, shell=True)

cmd = "sudo apt-get install grafana"
subprocess.run(cmd, shell=True)

cmd = "sudo systemctl daemon-reload"
subprocess.run(cmd, shell=True)

cmd = "sudo systemctl enable grafana-server.service"
subprocess.run(cmd, shell=True)

cmd = "sudo systemctl start grafana-server"
subprocess.run(cmd, shell=True)


