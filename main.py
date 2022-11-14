#!/bin/python3

import requests
import argparse

BASE_URL = "https://www.strava.com"
FEED_ACTIVITY = "/feed/activity/"
ACTIVITY = "/activities/"

headers = {}

class StravaClient:
    def __init__(self):
        print("Initializing client")

    def kudos(self, activity):
        url = BASE_URL + FEED_ACTIVITY + str(activity) + "/kudo"

        response = requests.request("POST", url, headers=headers, data={})

        if response.status_code == 200:
            print("Successfully gave kudos to " + str(activity))
            print(BASE_URL + ACTIVITY + str(activity))
            return True
        else:
            print("Failed to give kudos to " + str(activity))
            return False


def main():
    client = StravaClient()

    parser = argparse.ArgumentParser(description='Give kudos to random strangers')
    parser.add_argument('--start', dest='start', help='The activity to begin with')
    parser.add_argument('--count', dest='count', help='Number of activities to do')

    args = parser.parse_args()
    start = int(args.start)
    count = int(args.count)

    i = 0
    successes = 0
    fails = 0
    fails_in_a_row = 0
    while i < count:
        success = client.kudos(start + i)
        if success:
            successes += 1
            fails_in_a_row = 0
        else:
            fails += 1
            fails_in_a_row += 1

        if fails_in_a_row > 5:
            print("Failed too much in a row, stopping")
            break

        i += 1

    print("Gave kudos to " + str(successes) + " people!")

if __name__ == "__main__":
    main()
