import os

# get system details
system_name = os.uname().sysname
node_name = os.uname().nodename
release = os.uname().release
version = os.uname().version

print(f"System Name: {system_name}")
print(f"Node Name: {node_name}")
print(f"Release: {release}")
print(f"Version: {version}")