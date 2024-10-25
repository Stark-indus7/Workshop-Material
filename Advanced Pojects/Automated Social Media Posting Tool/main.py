# This project automates social media posts based on a schedule.
# Implement the code here

import schedule
import time

def post_to_social_media():
    print("Posting to social media...")

# Schedule posting
schedule.every().day.at("09:00").do(post_to_social_media)

# Keep script running
while True:
    schedule.run_pending()
    time.sleep(60)
