import os
import subprocess
import winapps

# Constants for commands
POWERSHELL_COMMANDS = {
    'NUCMD': 'net user',
    'AdminCMD': 'net localgroup administrators',
    'RDPCMD': 'get-service "remote desktop services" | select Displayname,Status,ServiceName,Can*',
    'AVCMD': 'Get-MpComputerStatus',
    'SinfoCMD': 'systeminfo',
    'FWCMD': 'netsh advfirewall show Publicprofile',
    'FWCMD2': 'netsh advfirewall show privateprofile',
    'IPCMD': 'ipconfig /all',
    'BLCMD': 'manage-bde -status',
    'SRVCMD': """Get-Service | Select StartType, Status, Name, DisplayName | Where-Object {$_.Status -eq 'Running'} | Format-Table -AutoSize"""
}

# Output file
outputfile = 'output.txt'

# Labels and formats
LABEL_FORMAT = '===============================================================================\n               ############## {} ##############\n===============================================================================\n'
CMD_BREAK = '-------------------------------------------------------------------------------\n'

# Label variables
AV_NAME = 'AV Example'  # Change the variable to your AV name
VPN_NAME = 'VPN Example'  # Change the variable to your VPN name
SECTION_LABELS = {
    'Users': 'Users',
    'RDP': 'Remote Connections',
    'Anydesk': 'Anydesk',
    'TV': 'Team Viewer',
    'AV': 'Anti Virus Status',
    'FW': 'Firewall Status',
    'Sinfo': 'System Info',
    'IP': 'IP Config',
    'BL': 'Bit Locker',
    'SRV': 'Services',
    'SFT': 'Software'
}


def format_label(variable):
    return LABEL_FORMAT.format(variable)


def write_to_file(text):
    with open(outputfile, 'a') as f:
        f.write(text + '\n')


def run_powershell_command(command):
    try:
        result = subprocess.run(['powershell.exe', command], shell=True, capture_output=True, text=True, check=True)
        write_to_file(result.stdout)
    except subprocess.CalledProcessError as e:
        write_to_file(f"Error running command: {command}\n{e.stderr}")


def search_and_write(name):
    apps = list(winapps.search_installed(name))
    if apps:
        write_to_file(f"\n{name} is installed\n")
    else:
        write_to_file(f"\n-----------------------------------\n|!!!!! {name} not found !!!!!|\n-----------------------------------\n")


def installed_software():
    try:
        output = subprocess.run(["powershell.exe", "-Command", 'wmic product get name'], shell=True, capture_output=True, text=True, check=True)
        lines = output.stdout.split("\n")
        for line in lines:
            if line.strip():
                write_to_file(line + "\n")
    except subprocess.CalledProcessError as e:
        write_to_file(f"Error getting installed software:\n{e.stderr}")


def main():
    write_to_file(format_label("AV&VPN"))
    search_and_write(AV_NAME)
    search_and_write(VPN_NAME)

    for section, label in SECTION_LABELS.items():
        write_to_file(format_label(label))
        if section in POWERSHELL_COMMANDS:
            run_powershell_command(POWERSHELL_COMMANDS[section])
        elif section == 'SFT':
            installed_software()
        write_to_file(CMD_BREAK)


if __name__ == "__main__":
    main()
    os.startfile(outputfile)