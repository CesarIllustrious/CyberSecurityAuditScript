# SecurityAuditScript
My security audit script with a user friendly GUI, decreases time wasted on obtaining audit information and returns it into a textfile. It then opens the text file ready to be analysed.
It was written and compiled in Python 3.10.5. 
Some features require admin priviledges.
Some features added as a bonus that dont need to be there.
Remember to change the names of AV and VPN.

What it does:
Checks for installed AV&VPN,
User accounts for the device,
Users with admin privileges, 
Remote connection apps,
status of AV, sysinfo, running services, firewall settings for public profile, bitlocker status,
Installed software list,
AV scan (optional)


You can use Nuitka to convert this into a portable .exe. I have this saved on my USB stick, ready for auditing. Remember to make a copy of the output for multiple
devices, as the output.txt file will be overwritten everytime.
Heres a guide I used to convert https://www.youtube.com/watch?v=YdZd7LolWm0

