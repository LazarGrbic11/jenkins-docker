import subprocess

cmd = "cp /var/lib/jenkins/workspace/job1/index.html ~/nginx/html"
subprocess.run(cmd, shell=True)