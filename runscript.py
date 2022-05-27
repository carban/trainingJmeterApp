import yaml
import sys
import subprocess
import json

# Making the docker command ---------------------------------------------------------------------------------

print("Catching specs.........")
url, port, threads, rampUp, iterations = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
numberEndpoints = 1
endpoints, methods = sys.argv[6], sys.argv[7]

print("Building the docker command with the following specs.........")
# print(json.dumps(specs, indent=4, sort_keys=True))

# Yes....windows
jmeter = "C:/Users/carlos.murillos/Downloads/apache-jmeter-5.4.3/bin/jmeter.bat"
# jmeter = "./../apache-jmeter-5.4.3/bin/jmeter"

for i in range(numberEndpoints):
    command = [jmeter]
    # command.extend(["-JURL", url, "-Jport", str(port), "-Jendpoint", endpoints, "-Jthreads", str(threads), "-JrampUp", str(rampUp)])
    # command.extend(["-Jiterations", str(iterations), "-Jmethod", methods, "-Jbody", json.dumps({"a": 10, "b": 5})])
    # command.extend(["-n", "-t", "script1.jmx", "-l", "out_"+endpoints.replace("/", "")+".jtl"])
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