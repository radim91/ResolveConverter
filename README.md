# ResolveConverter
If you have free version of DaVinci Resolve, you can't use mainstream media codecs (by this I mean h.264 typically in .mp4 container). So you have to change your video source to DNxHR (yuv422p10le) codec.

This simple script uses ffmpeg (be sure to have it installed) to convert .mp4 files to .mov and vice versa.

The easiest way is to put the script into working dir, type ./ResolveConverter, and let it convert all of the files. The script creates "converted" directory where the final videos are stored.
