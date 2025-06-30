# 🗽 MTA Live Subway Alert Feed – PyQt6 GUI

A modern desktop application that displays **real-time MTA subway service alerts** using the GTFS-RT API, built with **Python** and **PyQt6**. Designed for clarity, accuracy, and responsiveness — this GUI shows the latest status of all NYC subway lines, with live icons and a refresh mechanism.

![Screenshot](mta.png)

---

## 🚀 Features

- ✅ Live subway service status using MTA’s GTFS Realtime feed
- ✅ Clean, scrollable PyQt6 interface
- ✅ Color-coded SVG icons for all subway lines
- ✅ Categories like: Delays, Part Suspensions, Station Notices, and more
- ✅ One-click **Refresh** button to pull new alerts
- ✅ Filters out buses, railroads, and non-subway data

---

## 🛠️ Built With

- [Python 3.9+](https://www.python.org/)
- [PyQt6](https://pypi.org/project/PyQt6/)
- [Requests](https://pypi.org/project/requests/)
- [GTFS-RT JSON](https://developers.google.com/transit/gtfs-realtime)

---

## 📁 Project Structure

.
├── main.py # Launches the GUI
├── task1.py # MTAFeed: handles live API fetching and parsing
├── task2.py # Legacy GUI components (for testing)
├── subway_signs/ # SVG icons for subway lines
├── test.py # Test runner / experiments
├── screenshots/ # Screenshots for README
└── README.md # This file


---

## ▶️ How to Run

1. **Clone this repository:**

   ```bash
   git clone https://github.com/yourusername/mta-subway-alerts.git
   cd mta-subway-alerts
2. **Install dependencies:**

  pip install PyQt6 requests pytz

3. **Run the app:**

   python main.py

