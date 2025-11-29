[![GitHub stars](https://img.shields.io/github/stars/palmtree890/Swan_station_LOST?style=social)](https://github.com/palmtree890/Swan_station_LOST/stargazers) ![Repo Views](https://komarev.com/ghpvc/?username=palmtree890&repo=Swan_station_LOST&style=social&label=Repo+Views) ![GitHub Repo size](https://img.shields.io/github/repo-size/palmtree890/Swan_station_LOST?style=social&label=Repo%20size) ![GitHub top language](https://img.shields.io/github/languages/top/palmtree890/Swan_station_LOST?style=social) !

# Swan Station *LOST*

This is a replica of the familiar countdown timer from the TV show LOST. It is written in Python and is available for Linux, Mac, and Windows.

I made this to get better at Python, so if you have any recommendations, please fork this and add them, then submit a pull request!

## How to Install and Run

### 1. Clone the Repository

You can clone the repo using Git:

```bash
git clone https://github.com/Palmtree890/Swan_station_LOST/
```
### 2.Enter the directory
```
cd Swan_station_LOST
# Use 'ls' or 'dir' to view the files and confirm you are in the correct location
```
### 3. Create and Activate a Virtual Environment (venv)
## for windows
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
For Linux or macOS (Bash/Zsh)
```Bash/Zsh
python3 -m venv venv
source venv/bin/activate
```
(Note: On some systems, the command might be just python -m venv venv if python is already aliased to python3.)

### 4. Install Requirements
First, ensure your package management tools are up to date:
```bash
python -m pip install --upgrade setuptools wheel
```
Now, install the project-specific dependencies listed in requirements.txt:
```bash
python -m pip install -r requirements.txt
```
### 5. Run the Project
You are now ready to run the application!
```bash
python run.py
```
replace python with python3 for linux
