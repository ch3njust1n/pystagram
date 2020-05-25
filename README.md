# pystagram

API for downloading Instagram videos. Can handle video single videos and edge media.

Example
```
link = 'www.instagram.com/p/B8B9dYtgvDk/'
name = 'video'
gram = Instagram(link)
gram.download(dst='save_dir', filename=name)
```
