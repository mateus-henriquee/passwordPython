import subprocess
rede = "dualcore"

info = subprocess.run(
    ["netsh", "wlan", "show", "profile", rede, "key=clear"],
    stdout=subprocess.PIPE)
inf = info.stdout.decode('utf-8', errors='ignore')
print(inf)