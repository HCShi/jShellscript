#!/bin/bash
# A complete, cross-platform solution to record, convert and stream audio and video.
ffmpeg -i hell.mkv -ss 00:00:00 -t 00:06:03 -async 1 cut.mkv  # 按照时间来切割视频
