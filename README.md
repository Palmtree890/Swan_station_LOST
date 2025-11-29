# Swan Station *LOST*
This is a replica of the familiar countdown timer from the TV show LOST. It is written in python and is avalible for 
linux, mac, and windows.
I made this to get better at python so if you have any recomendations please fork this and add them, then submit a pull request.
## How to install
first clone the repo
```bash
https://github.com/Palmtree890/Swan_station_LOST
```
Then cd into the repo
```bash
cd Swan_station_LOST
ls
```
Then you will make the venv (this will very from OS but I will include intructions for both)

#FOR WINDOWS
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
#for Linux
```bash
python3 -m venv venv
source venv/bin/acivate
```
#For Mac
same as linux, just change python3 to python

after you have made the venv its time to install the requrements but forst I reqemend updating setuptools wheel.
```powershell
py -m pip install --upgrade setuptools wheel
```
Now you are ready to install the requirments. to install run this command
```bash/powershell
python -m pip install -r requirements.txt
```
Now you are ready to run your LOST project
```powershell
python run.py
```
```bash
python3 run.py
```
