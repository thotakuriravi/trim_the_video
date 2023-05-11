# trim_the_video

This python code will pic the video and trim the video to the given length or duration.

Firstly we need to install the moviepy library in our environment. use `pip install moviepy`

And Moviepy library needs ffmpeg software. link to download the ffmpeg software `https://ffmpeg.org/download.html#build-windows`
after installing the ffmpeg we need to add it to environment paths. below image shows the variable name and paths.
![image](https://github.com/thotakuriravi/trim_the_video/assets/78135736/ 97b22c0d-e363-4715-89db-3ffad5080e0c)

| Variable name    | variable value |
| -------- | ------- |
| IMAGEIO_ffmpeg_EXE  | C:\Program Files\ImageMagick-7.1.1-Q16\ffmpeg.exe   |
| IMAGEMAGICK_BINARY | C:\Program Files\ImageMagick-7.1.1-Q16\magick.exe     |

after doing this we need check ffmpeg working or not.
### How to Check ffmpeg working or not?
 - To check the ffmpeg working condition Just follow the below steps:
 - Open the command prompt 
 - and type `ffmpeg` and press enter
 - then you find the info like below
 - ![image](https://github.com/thotakuriravi/trim_the_video/assets/78135736/24a07e6c-eefc-49e2-8a17-9fb69bd272b3)
- If not get above info means ffmpeg not working. in that situation we need to uninstall the ffmpeg and again follow the above installation steps

### Then we need to select the video directory and new directory path
. lastly we need to select the duration

