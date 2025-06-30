from collections import defaultdict
from datetime import datetime
import pytz
import requests

class MTAFeed:
    FEED_URL = 'https://collector-otp-prod.camsys-apps.com/realtime/gtfsrt/ALL/alerts?type=json'

    EFFECT_CATEGORY_MAP = {
        'NO_SERVICE': 'No Scheduled Service',
        'REDUCED_SERVICE': 'Planned - Part Suspended',
        'SIGNIFICANT_DELAYS': 'Delays',
        'STOP_MOVED': 'Station Notice',
        'STATION_CLOSURE': 'Station Notice',
        'DETOUR': 'Planned - Trains Rerouted',
        'OTHER_EFFECT': 'Planned - Trains Rerouted',
    }

    # NYC Subway route IDs (excluding buses and commuter rails)
    SUBWAY_ROUTES = set([
        '1','2','3','4','5','6','7',
        'A','B','C','D','E','F','G','J','L','M','N','Q','R','S','W','Z',
        'GS', 'H', 'SI'
    ])

    def __init__(self):
        self.refresh()

    def refresh(self):
        self.refresh_time = datetime.now(pytz.timezone('US/Eastern'))
        self.data = defaultdict(set)

        try:
            response = requests.get(self.FEED_URL)
            alerts = response.json().get("entity", [])
        except Exception as e:
            print("Failed to fetch alerts:", e)
            alerts = []

        for entity in alerts:
            alert = entity.get("alert", {})
            informed_entities = alert.get("informed_entity", [])

            effect = alert.get("effect", "UNKNOWN").upper()
            category = self.EFFECT_CATEGORY_MAP.get(effect)

            if not category:
                mercury_alert = alert.get("transit_realtime.mercury_alert", {})
                category = mercury_alert.get("alert_type", "Miscellaneous")

            if not category:
                category = "Miscellaneous"

            found_subway = False
            for ie in informed_entities:
                route_id = ie.get("route_id")
                if route_id and route_id in self.SUBWAY_ROUTES:
                    self.data[category].add(route_id)
                    found_subway = True

            if not found_subway:
                continue  # skip bus/Q routes/etc

    def getRefreshTime(self):
        return self.refresh_time

    def items(self, include_empty=False):
        for alert_type, routes in self.data.items():
            if include_empty or routes:
                yield alert_type, routes

    def __getitem__(self, alert_type):
        return self.data.get(alert_type, set())

    def getLines(self):
        all_lines = set()
        for routes in self.data.values():
            all_lines.update(routes)
        return all_lines