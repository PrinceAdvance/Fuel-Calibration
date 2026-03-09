## FUEL CALIBRATION TOOL 
This is a fuel calibration tool for calibrating fuel sensors + Ruptella GPS Tracker on Navixy fleet management platform.
The tool uses Navixy API for data transmission and makes calibration seamless. 
I implemented this for one of the biggest mining companies in Africa, across their multi-national sites



## Requirements
1. Python 3.0+
2. Navixy account
3. Internet connectivity to reach the Navixy API


 ## HOW TO USE THE TOOL
 1. Open your Command Line Interface
 2. Run the program


##  Features

- Authenticate with a Navixy account
- List all trackers in the account
- Fetch processed fuel level data
- Download **raw analog fuel sensor readings** for calibration purposes


---


## 🚀 Installation

Clone or copy the repository to your local machine and install dependencies (only `requests` is required):

```powershell
git clone <repository-url> "Fuel Calibration"
cd "Fuel Calibration"
python -m pip install --upgrade pip
python -m pip install requests
```

> If you prefer, you can also just download `fuel-tool.py` since the project is standalone.

---

## ▶️ Usage

Run the script from a command prompt or terminal:

```powershell
python fuel-tool.py
```

The program will prompt you for your Navixy credentials and then present a simple menu:

```
NAVIXY FUEL SENSOR CALIBRATION TOOL

MENU
1. Get all trackers
2. Get all sensors
3. Get fuel level (processed)
4. Get RAW fuel sensor data (CALIBRATION)
5. Exit
```

### Menu options

1. **Get all trackers** – Displays the ID and label for every tracker in your account.
2. **Get all sensors** – After entering a tracker ID, prints the JSON response returned by Navixy.
3. **Get fuel level (processed)** – Retrieves the standard processed fuel-level reading for a tracker.
4. **Get RAW fuel sensor data (CALIBRATION)** – Prompts for tracker ID and time range (ISO format) and prints a CSV of raw analog sensor values.  Use this when performing sensor calibration.
5. **Exit** – Logs out and terminates the program.


##  Notes

- The script stores the session hash only in memory; it does not persist credentials.
- If authentication fails, the program will exit without further prompts.
- The payloads printed by the script are not logged to disk; redirect output if you wish to save results.

---

## ⚖️ License

This project is provided "as is" under the MIT License. Feel free to modify and redistribute.

---

## 📬 Feedback

Feel free to open an issue or send feedback to the author if you need additional features or run into problems.