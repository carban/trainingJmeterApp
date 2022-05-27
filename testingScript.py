
import sys
import subprocess

# Making the docker command ---------------------------------------------------------------------------------

print("Catching specs.........")

testType, time, host, port = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
testFile = "trainingApp.jmx"

if (testType == "normal"):
    testFile = "TrainingNormal.jmx"
elif (testType == "stress"):
    testFile = "trainingStress.jmx"
elif (testType == "load"):
    testFile = "trainingLoad.jmx"
elif (testType == "peaks"):
    testFile = "trainingPeaks.jmx"
elif (testType == "wordLoad"):
    testFile = "trainingWordLoad.jmx"

print("Building the docker command with the following specs.........")
# print(json.dumps(specs, indent=4, sort_keys=True))

# Yes....windows
# jmeter = "C:/Users/carlos.murillos/Downloads/apache-jmeter-5.4.3/bin/jmeter.bat"
jmeter = "./../apache-jmeter-5.4.3/bin/jmeter"

command = [jmeter, "-Jhost", host, "-Jport", port, "-Jtime", time, "-n", "-t", testFile, "-l", "out_"+testType.replace("/", "")+".jtl"]


print(command)
print("Running.....")
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