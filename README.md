# Instagram-bio-followers-display
## Display your Instagram Followers on Bio

**Did you ever wonder how TomScott did this**

![This is an image](readme/Capture1.PNG)

**ignore it let's do it for Instagram** 

![This is an image](readme/Capture2.PNG)

**like this**

## Installation

1. Download the repository

    ```bash
    git clone https://github.com/Pasanlaksitha/Instagram-bio-followers-display.git
    ```
2. open bio.py and enter username password 
    ```python
    username = "USERNAME"
    password = "PASSWORD"
    ```
3. schedule for the run program (recommended: 6 hours ) 

## Other Usage

you can convert this for following and posts count also 

- for following count 
    ```python
    #change scraping json to this
    followers = data2['graphql']['user']['edge_follow']['count']
    ```
- read JSON on Instagram https://www.instagram.com/boinkchimp/?__a=1 to do more



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://github.com/Pasanlaksitha/Instagram-bio-followers-display/blob/main/LICENSE/)