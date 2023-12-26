Just a simple snake game in Python for Ableton Push2, based on https://github.com/ffont/push2-python/  library.


Written and tested in windows, while nothing should stop it to work in *nix.

Requires, for windows:

* Python (tested with 3.11 version from Windows Store)
* git installed for fetching  push2 lib. I had installed it this way: ``` winget install --id Git.Git -e --source winget```  (make sure you restart the console/ editor or whatever before running pip for git to appear in environment )
* python libs installed  ```pip install -r requirements.txt```
* libusb dll

libusb-1.0.dll has to be put in this folder

Can be retrieved from 7z files (e.g. libusb-1.0.26-binaries.7z) taken from https://github.com/libusb/libusb/releases

For my 64 bit Windows it was in the following location within archive: libusb-1.0.26.7z\VS2015\MS64\dll\libusb-1.0.dll

Tested with libusb-1.0.20 and  libusb-1.0.26 versions.


Launched as: 
```python3 .\snake.py```