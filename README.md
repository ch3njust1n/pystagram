# pystagram

API for downloading Instagram videos. Can handle video single videos and edge media.

Install
```
git clone https://github.com/ch3njust1n/pystagram.git && cd pystagram
python setup.py build
sudo python setup.py install
```

Example
```
from pystagram import Instagram
link = 'www.instagram.com/p/B8B9dYtgvDk/'
name = 'video'
gram = Instagram(link)
gram.download(dst='save_dir', filename=name)
```
