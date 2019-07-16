import subprocess
subprocess.call("ifconfig")
aa = input("please input your interface:> ")
subprocess.call(["ifconfig", aa, "down"])
ww = input("please input your desired mac address> ")
subprocess.call(["ifconfig", aa, "hw", "ether", ww])
subprocess.call(["ifconfig", aa, "up"])
print(f"your {aa} mac address has been changed to {ww}")
