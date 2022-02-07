from instagrapi import Client
import requests
import json

username = "USERNAME"
password = "PASSWORD"
def instagram_json():
    response = requests.get(f"https://www.instagram.com/{username}/?__a=1")
    data = response.json()
    data1 = json.dumps(data)
    data2 = json.loads(data1)
    followers = data2['graphql']['user']['edge_followed_by']['count']
    bio = data2['graphql']['user']['biography']
    print(followers)
    return followers, bio
    

def bio():
    followers, bio = instagram_json()
    bio_followers = [int(i) for i in bio.split() if i.isdigit()][0]
    if followers != bio_followers:
        ig = Client()
        ig.login(username, password)
        ig.account_edit(biography=f"I have {followers} followers 😇")
        ig.logout      
        
if __name__ == "__main__":
   bio()