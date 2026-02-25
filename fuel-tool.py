import requests
import json
from datetime import datetime

class NavixyFuelManager:
    def __init__(self, username, password):
        self.api_url = ""
        self.dwh_url = ""
        self.username = username
        self.password = password
        self.session_hash = None

    def authenticate(self):
        response = requests.post(f"{self.api_url}/user/auth", json={
            "login": self.username,
            "password": self.password
        })
        result = response.json()

        if result.get("success"):
            self.session_hash = result["hash"]
            print("✓ Logged in successfully\n")
            return True
        else:
            print("✗ Login failed")
            return False

    # ==============================
    # RAW FUEL DATA (CALIBRATION)
    # ==============================
    def get_raw_fuel_data(self, tracker_id, from_time, to_time):
        """Get raw analog fuel sensor data (CALIBRATION USE ONLY)"""

        payload = {
            "hash": self.session_hash,
            "tracker_id": str(tracker_id),
            "from": from_time,
            "to": to_time,
            "columns": [
                "speed",
                "inputs.avl_io_66", # Tank 
                "inputs.avl_io_68",
                "inputs.hw_mileage"
            ]
        }

        response = requests.post(
            f"{self.dwh_url}/tracker/raw_data/read",
            headers={
                "accept": "text/csv",
                "Content-Type": "application/json"
            },
            json=payload
        )

        print("=" * 60)
        print("🛢️ RAW FUEL SENSOR DATA (FOR CALIBRATION)")
        print("=" * 60)

        if response.status_code == 200:
            print(response.text)
        else:
            print("✗ Failed to retrieve raw data")
            print(response.text)

        print("=" * 60)

    # ==============================
    # EXISTING FUNCTIONS (UNCHANGED)
    # ==============================
    def get_all_trackers(self):
        response = requests.post(f"{self.api_url}/tracker/list", json={
            "hash": self.session_hash
        })
        result = response.json()

        if result.get("success"):
            for t in result.get("list", []):
                print(f"ID: {t['id']} | Name: {t['label']}")
        return result.get("list", [])

    def get_all_sensors(self, tracker_id):
        response = requests.post(f"{self.api_url}/tracker/sensor/list", json={
            "hash": self.session_hash,
            "tracker_id": tracker_id
        })
        print(json.dumps(response.json(), indent=2))

    def get_fuel_level(self, tracker_id):
        response = requests.get(f"{self.api_url}/tracker/get_fuel", params={
            "hash": self.session_hash,
            "tracker_id": tracker_id
        })
        print(json.dumps(response.json(), indent=2))

    def logout(self):
        requests.post(f"{self.api_url}/user/logout", json={
            "hash": self.session_hash
        })
        print("\n✓ Logged out")


# ==============================
# MAIN
# ==============================
def main():
    print("NAVIXY FUEL SENSOR CALIBRATION TOOL\n")

    username = input("Navixy Username: ")
    password = input("Navixy Password: ")

    navixy = NavixyFuelManager(username, password)

    if not navixy.authenticate():
        return

    while True:
        print("\nMENU")
        print("1. Get all trackers")
        print("2. Get all sensors")
        print("3. Get fuel level (processed)")
        print("4. Get RAW fuel sensor data (CALIBRATION)")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            navixy.get_all_trackers()

        elif choice == "2":
            tracker_id = input("Tracker ID: ")
            navixy.get_all_sensors(tracker_id)

        elif choice == "3":
            tracker_id = input("Tracker ID: ")
            navixy.get_fuel_level(tracker_id)

        elif choice == "4":
            tracker_id = input("Tracker ID: ")
            from_time = input("From (ISO, e.g. 2023-11-29T08:31:00Z): ")
            to_time = input("To   (ISO, e.g. 2023-11-29T08:32:00Z): ")
            navixy.get_raw_fuel_data(tracker_id, from_time, to_time)

        elif choice == "5":
            navixy.logout()
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
