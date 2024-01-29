# Overview
This project aims to improve a Python script for system information gathering and reporting. The script collects various system details, such as user information, installed software, antivirus status, firewall status, etc., and outputs them to a text file.

# Features
Consolidation of PowerShell commands into a dictionary for better manageability.
Adoption of consistent snake_case naming convention for variables.
Use of F-strings for cleaner string formatting.
Addition of error handling mechanisms for subprocess and file operations, enhancing script robustness.
Modularization of the code into reusable functions for improved readability and maintainability.
Inclusion of docstrings for function clarity and usage explanation.
Ensuring consistent code formatting, including indentation, for improved readability.

# How to Use
Fork the repository.
Clone the forked repository to your local machine.
Make necessary changes or improvements to the script.
Commit your changes and push them to your fork.
Create a pull request to merge your changes into the original repository.
Once approved, your changes will be merged.

# Contributors
Michael J. Rodriguez github.com/mjrodri
and
https://github.com/CesarIllustrious

License
This project is licensed under the MIT License.

# SecurityAuditScript
My security audit script that decreases time wasted on obtaining audit information and returns it into a textfile. It then opens the text file ready to be analysed.
It was written and compiled in Python 3.10.5. 
The print statements are a GUI for the output.txt file.
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

