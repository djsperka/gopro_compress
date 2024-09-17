# gopro_compress	

Combine and compress GoPro videos.

Our GoPro camera will split longer videos (longer than ~30min) into multiple MP4 files. 
The individual video files are also obscenely large, due to the codec used, the frame rate (60fps) and the resolution of the raw videos.
This project will concatenate these videos and compress them as well. A title and time display are added to the resulting video. Audio is preserved.

## Getting Started

Clone this repo first, and fetch the prerequisites below. 

### Prerequisites

The things you need before installing the software.

* Python >= 3.8.10
* [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)
* ffmpeg is required - see *ffmpeg-python* docs above. For Windows, I used the 6.0 **build-essentials** release from [this site](https://github.com/GyanD/codexffmpeg/releases/tag/6.0)

### Installation

Set up a virtual env (optional)

```
PS C:\Users\djsperka\Desktop\work> python -m venv --copies ./gpc-venv/
PS C:\Users\djsperka\Desktop\work> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
PS C:\Users\djsperka\Desktop\work> .\gpc-venv\Scripts\Activate.ps1
(gpc-venv) PS C:\Users\djsperka\Desktop\work> python -m pip install ffmpeg-python
Collecting ffmpeg-python
  Using cached ffmpeg_python-0.2.0-py3-none-any.whl (25 kB)
Collecting future
  Downloading future-1.0.0-py3-none-any.whl (491 kB)
     |████████████████████████████████| 491 kB 1.6 MB/s
Installing collected packages: future, ffmpeg-python
Successfully installed ffmpeg-python-0.2.0 future-1.0.0
```

## Usage

A few examples of useful commands and/or tasks.

```
import video_files as vf
import process_video_files as pvf

# raw videos copied from the camera are in this folder. 
gpvf=vf.GPVideoFolder('C:/Users/djsperka/Desktop/raw');

# Process the videos.
# pvf.concatenate_all_gpvideos(gpvf, 'label1', 'label2', output_folder, dry-run-tf)
# Args:
# gpvf - a GPVideoFolder object
# label1, label2 - output filename is 'label1_creationdate_label2.mp4'. Both label1 and label2 are also
#                  part of the overlay text written on the output video.
# output_folder - folder where output mp4 files are placed.
# dry-run-tf - if True, then just a dry-run; no output files are written. If False, then create output mp4 files.
# 
pvf.concatenate_all_gpvideos(gpvf, 'multiple', 'PairTraining', 'c:/Users/djsperka/Desktop/out', False)
```

