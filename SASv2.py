import os
import winapps
import subprocess

outputfile = 'output.txt'  #output file

#Labels and formats
Start_label = '=== is new section,\n--- is new command in the section\n### is info type\n\n===============================================================================\n               ############## AV&VPN ##############\n==============================================================================='
Label_format = '===============================================================================\n               ############## {} ##############\n===============================================================================\n'
CMD_Break = '-------------------------------------------------------------------------------\n'

#Label Variables
Users = 'Users'
RDP = 'Remote Connections'
anydesk = 'Anydesk'
TV = 'Team Viewer'
AV = 'Anti Virus Status'
FW = 'Firewall Status'
Sinfo = 'System Info'
IP = 'IP Config'
BL = 'Bit Locker'
SRV = 'Services'
SFT = 'Software'
AVname = 'AV Example'  #Change the variable to your AV name
VPN_NAME = 'VPN Example' #Change the variable to your VPN name


#PowerShell Commands Variables
NUCMD = 'net user'
AdminCMD = 'net localgroup administrators'
RDPCMD = 'get-service "remote desktop services" | select Displayname,Status,ServiceName,Can*'
AVCMD = 'Get-MpComputerStatus'
SinfoCMD = 'systeminfo'
FWCMD = 'netsh advfirewall show Publicprofile'
FWCMD2 = 'netsh advfirewall show privateprofile'
IPCMD = 'ipconfig /all'
BLCMD = 'manage-bde -status'
SRVCMD = """Get-Service | Select StartType, Status, Name, DisplayName | Where-Object {$_.Status -eq 'Running'} | Format-Table -AutoSize"""



#Label Format Function
def formatlabel(variable):
     
        return Label_format.format(variable)



#Write Function
def write(text):
    with open(outputfile, 'a') as f:
        f.write(text)
        f.flush()

#Software Search Function
def search (name):
    search1 =  list(winapps.search_installed(name))
    if search1:
        write(f"\n {name} is installed\n")
    else:
        write(f"\n-----------------------------------\n|!!!!! {name} not found !!!!!|\n-----------------------------------\n") 







#Run PowerShellCMD Function
def run_PSCMD(input):
    
        test = subprocess.run(['powershell.exe',input], shell=True, stdout=subprocess.PIPE, text=True)
        
        write(test.stdout)

#Installed Software Format Function
def installed_software():
    output = subprocess.run(
    ["powershell.exe", "-Command", 'wmic product get name'],
    shell = True,
    stdout = subprocess.PIPE,
    encoding = "UTF-8")
    # Split the output into lines
    lines = output.stdout.split("\n")
    # Write only the non-empty lines to the file
    for line in lines:
        if line.strip():
            write(line + "\n")               

#The Script Main 
def main():
    
    write(Start_label)

    search(AVname)
    search(VPN_NAME)

    write(formatlabel(Users))

    run_PSCMD(NUCMD)

    write(CMD_Break)

    run_PSCMD(AdminCMD)
    

    write(formatlabel(RDP))
    run_PSCMD(RDPCMD)
    write(CMD_Break)
    search(anydesk)
    write(CMD_Break)
    search(TV)

    write(formatlabel(AV))
    run_PSCMD(AVCMD)

    write(formatlabel(Sinfo))
    run_PSCMD(SinfoCMD)

    write(formatlabel(FW))
    run_PSCMD(FWCMD)
    write(CMD_Break)
    run_PSCMD(FWCMD2)

    write(formatlabel(IP))
    run_PSCMD(IPCMD)
    
    write(formatlabel(BL))
    run_PSCMD(BLCMD)

    write(formatlabel(SRV))
    run_PSCMD(SRVCMD)

    write(formatlabel(SFT))
    installed_software()



if __name__ == "__main__":
     main()


# Star the file automatically
os.startfile(outputfile)


#FEATURE ENABLED BY DELETING '#' before the px, requires admin
    #p6 = subprocess.run('sfc /scannow', stdout=f, text=True)  # System File Checker in case new drives needed   
    #p7 = subprocess.call('powershell.exe Start-MpScan', shell=True, stdout=f, text=True)    # start AV scan
