import yaml
import sys
import subprocess
import json

# Loading file and parameters ---------------------------------------------------------

with open("applications.yml", 'r') as stream:
    data = yaml.safe_load(stream)

app, env = sys.argv[1], sys.argv[2]

# Searching for the app and the environment ---------------------------------------------------------

apps = data["applications"]
appFound = False
specs = {}

for a in apps:
    if (a["name"] == app):
        appFound = True
        try:
            specs = a["environments"][env]
            break
        except:
            print("No environment found")
            sys.exit() 

if not appFound:
    print("No app found")
    sys.exit()

# Making the docker command ---------------------------------------------------------------------------------

print("Catching specs.........")
url, port, threads, rampUp, iterations = specs["URL"], specs["port"], specs["threads"], specs["rampUp"], specs["iterations"]
numberEndpoints = specs["numberEndpoints"]
endpoints, methods, bodies = specs["endpoints"], specs["methods"], specs["bodies"]

print("Building the docker command with the following specs.........")
# print(json.dumps(specs, indent=4, sort_keys=True))

# Yes....windows
jmeter = "C:/Users/carlos.murillos/Downloads/apache-jmeter-5.4.3/bin/jmeter.bat"

for i in range(numberEndpoints):
    command = [jmeter]
    command.extend(["-JURL", url, "-Jport", str(port), "-Jendpoint", endpoints[i], "-Jthreads", str(threads), "-JrampUp", str(rampUp)])
    command.extend(["-Jiterations", str(iterations), "-Jmethod", methods[i], "-Jbody", json.dumps(bodies[i])])
    command.extend(["-n", "-t", "script1.jmx", "-l", "out_"+endpoints[i].replace("/", "")+".jtl"])
    print(command)
    print("Running.....", i+1)
    process = subprocess.call(command)


"""
URL=ec2-3-17-140-131.us-east-2.compute.amazonaws.com
port=8080
endpoint=/add
threads=1
rampUp=1
iterations=10
method=POST
body={"a": 10, "b": 5}
"""

# Executing sitespeed.io ---------------------------------------------------------------------------------

# print("Running.........")
# process = subprocess.Popen(command, stdout=subprocess.PIPE)
# output, error = process.communicate()
# output = output.decode("utf-8").split("\n")

# print(output)