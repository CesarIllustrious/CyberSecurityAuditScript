import os, sys, winapps, subprocess, wmi
from unittest import result
 


with open('output.txt', 'w') as f:
#### AV & VPN Check
    print('=== is new section,\n--- is new command in the section\n### is info type\n\n===============================================================================\n               ############## AV&VPN ##############\n===============================================================================', end='\n\n', file=f)    
    BD = list(winapps.search_installed('NAME OF ANTIVIRUS'))   #change the name to your company's AV
    if BD: print(*BD,sep='\n\n', end='\n\n', file=f)
    else: f.write("-----------------------------------\n|!!!!! NAME OF AV not found !!!!!|\n-----------------------------------\n"), f.flush   #change the output name
    
    cisco = list(winapps.search_installed('NAME OF VPN'))  #change to company VPN name
    if cisco: print(*cisco, sep='\n\n', end='\n\n', file=f)
    else: f.write("----------------------------------------\n|!!!!! NAME OF VPN not found !!!!!|\n----------------------------------------\n===============================================================================\n               ############## User Accounts ##############\n==============================================================================="), f.flush()
    
#### Users check   
    p8 = subprocess.run(["powershell.exe", """net user"""], shell=True, stdout=f, text=True)   #show all users    
    print("-------------------------------------------------------------------------------\n               ############## Admin accounts ##############\n-------------------------------------------------------------------------------", end='\n\n', file=f), f.flush()     
    
    p9 = subprocess.run(["powershell.exe", """net localgroup administrators"""], shell=True, stdout=f, text=True)    #show admin users
    print('===============================================================================\n               ############## Remote Connections ##############\n===============================================================================', file=f), f.flush()    
 #####  Remote connections check
    p12 = subprocess.run(["powershell.exe", "-Command", 'get-service "remote desktop services" | select Displayname,Status,ServiceName,Can*'], shell=True, stdout=f, text=True),  f.flush
   
    AD = list(winapps.search_installed('Anydesk'))
    if AD: print(*AD, sep='\n\n', end='\n\n', file=f)
    else: f.write("---------------------\n| Anydesk not found |\n---------------------\n"), f.flush()               

    TV = list(winapps.search_installed('TeamViewer'))
    if TV: print(*TV, sep='\n\n', end='\n\n', file=f)
    else: f.write("-------------------------\n| TeamViewer not found  |\n-------------------------\n")
    print('===============================================================================\n               ############## AntiVirus Status ##############\n===============================================================================', file=f), f.flush()            
#### Status of antimalware, sysinfo, services, sfc scan firewall settings, bitlocker status
    p1 = subprocess.call('powershell.exe Get-MpComputerStatus', shell=True, stdout=f, text=True)    #AV Detail status
    print("===============================================================================\n               ############## SYSTEMINFO ##############\n===============================================================================", file=f), f.flush() 
     
    p2 = subprocess.run('systeminfo', stdout=f, text=True)            #sysinfo    
    print("\n===============================================================================\n               ############## FIREWALL-STATUS ##############\n===============================================================================", file=f), f.flush() 
    
    p3 = subprocess.check_call('netsh advfirewall show Publicprofile', stdout=f, text=True)  # FWINFO                         
    print("===============================================================================\n               ############## IPCONFIG ##############\n===============================================================================", file=f), f.flush() 
   
    p4 = subprocess.run('ipconfig /all', stdout=f, text=True)  # IPINFO            
    print('\n\n===============================================================================\n               ############## BITLOCKER-STATUS ##############\n===============================================================================', end='\n\n', file=f), f.flush() 

    p5 = subprocess.run(["powershell.exe", """manage-bde -status"""], shell=True, stdout=f, text=True)
    print("\n\n===============================================================================\n                  ############## SERVICES ##############\n===============================================================================", file=f), f.flush() 

    p10 = subprocess.run(["powershell.exe", """Get-Service | Select StartType, Status, Name, DisplayName | Where-Object {$_.Status -eq 'Running'} | Format-Table -AutoSize"""], shell=True, stdout=f, text=True)  # running services
    print("===============================================================================\n               ############## INSTALLED-SOFTWARE ##############\n===============================================================================", file=f), f.flush() 
##### Installed software check  & extra scans feature
    for item in winapps.list_installed(): print(item, file=f)                      
    f.flush()
    #FEATURE ENABLED BY DELETING '#' before the pX, requires admin
    #p6 = subprocess.run('sfc /scannow', stdout=f, text=True)  # System File Checker in case new drives needed   
    #p7 = subprocess.call('powershell.exe Start-MpScan', shell=True, stdout=f, text=True)    # start AV scan
   
os.startfile('output.txt')   # Open the output text file


    
    
        















