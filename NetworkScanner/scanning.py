import subprocess
import platform


class Systems:
    os_name = platform.system()
    def Linux():
        result = subprocess.run(
            ["arp-scan", "--localnet"],
            capture_output=True,
            text=True
        )

        print(result)

        if result.returncode != 0 or "permission denied" in result.stderr.lower():
            print("Standard scan needs root. Trying with sudo...")
            subprocess.run(["sudo", "arp-scan", "--localnet"])
        elif "command not found" in result.stderr.lower():
            not_installed = input("You haven't installed apr-scan\nEnter ok to install it").lower()
            if not_installed == "ok":
                subprocess.run(["sudo", "apt-get", "install", "arp-scan"])
                subprocess.run(["sudo", "arp-scan", "--localnet"])
        else:
            print(result.stdout)


    def Windows():
        result = subprocess.run(
            ["arp", "-a"],
            capture_output=True,
            text=True
        )

        print(result.stdout)



    def Mac():
        result = subprocess.run(
            ["arp-scan", "--localnet"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0 or "permission denied" in result.stderr.lower():
            print("Standard scan needs root. Trying with sudo...")
            subprocess.run(["sudo", "arp-scan", "--localnet"])
        elif "command not found" in result.stderr.lower():
            not_installed = input("You haven't installed apr-scan\nEnter ok to install it").lower()
            if not_installed == "ok":
                subprocess.run(["brew", "install", "arp-scan"])
                subprocess.run(["sudo", "arp-scan", "--localnet"])
        else:
            print(result.stdout)


if Systems.os_name == "Linux":
    Systems.Linux()

elif Systems.os_name == "Windows":
    Systems.Windows()

elif Systems.os_name == "Darwin":
    Systems.Mac()

















        
# else:
#     print("_"*30+"\n|Sorry you are not on Windows|\n"+"‾"*30)
