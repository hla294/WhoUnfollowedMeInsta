import instaloader
import json
from sys import argv

# followers : People -> I
# followings : I -> people
# What I want to know : followings - followers

USERNAME = argv[1]
PASSWORD = argv[2]

try:
    with open("data.json") as data_file:
        # Reading from the json file that I saved followers and followings on
        data = json.load(data_file)
        followers_data = data["followers"]
        followings_data = data["followings"]
        print(f"Total number of followers: {len(followers_data)}")
        print(f"Total number of followings: {len(followings_data)}")

        diff1 = set(followings_data) - set(followers_data)
        print(f"Total number of people who do not follow me back: {len(diff1)}")
        result ={
            "personNotFollowBack": list(diff1)
        }
    # New json file showing people that DO NOT follow me back
    with open("result.json", "w") as result_file:
        json.dump(result, result_file, indent=4)

# Create a new json file saves all of followers and followings from my insta account
except FileNotFoundError:
    bot = instaloader.Instaloader()
    bot.login(user=USERNAME, passwd=PASSWORD)

    profile = instaloader.Profile.from_username(bot.context, USERNAME)

    followers = [follower.username for follower in profile.get_followers()]
    followings = [followee.username for followee in profile.get_followees()]

    instaData = {
    "followers" : followers,
    "followings" : followings
    }

    with open("data.json", "w") as data_file:
        json.dump(instaData, data_file, indent=4)

    




