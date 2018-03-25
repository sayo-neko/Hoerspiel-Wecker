# Hoerspiel-Wecker

## Dependencies

### Linux

- Python 3.6
- ffmpeg (optional)

```
apt-get install python3 ffmpeg
pip install flask python-mpd2
```

### Windows

- Python 3.6
- ffmpeg (optional?)
- MPD: https://www.musicpd.org/download/win32/0.20.10/

    -> Download to bin folder.

```
cd ./bin/
mpd ../config/mpd.conf
```


## Run

```
python app.py
```