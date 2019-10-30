# First install official youtube-dl
## For Windows
pip install youtube-dl 
## For Ubuntu
sudo add-apt-repository ppa:nilarimogard/webupd8 -y

sudo apt-get update

sudo apt-get install youtube-dl

# To download best availble video (mp4) and best available audio (m4a) and then merge them together(replace VIDEO_URL with the link of YouTube video)
### youtube-dl -citw -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]' VIDEO_URL

