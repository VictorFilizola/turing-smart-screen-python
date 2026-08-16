#!/bin/bash
# Regenerate the screen videos from the GIFs. Run from repo root.
set -e
cd "$(dirname "$0")/.."

# 9" screen (PID 0x0092, landscape 1920x480):
#   skeleton ping-pong, crop 1/3 off top + 1/5 off bottom, stretch to fill, rotate for landscape mount
ffmpeg -y -i turin-smart-screen-themes/skeleton-skeletons-ezgif.com-speed.gif \
  -vf "crop=640:224:0:160,scale=1920:480,setsar=1,fps=25,transpose=1" \
  -c:v libx264 -profile:v baseline -pix_fmt yuv420p -movflags +faststart \
  turin-smart-screen-themes/skeleton-skeletons-ezgif-9inch.mp4

# 2.8" round screen (PID 0x0028, 480x480): redskull, flipped 180
ffmpeg -y -i turin-smart-screen-themes/redskull.gif \
  -vf "scale=480:480:flags=lanczos,hflip,vflip,setsar=1,fps=25" \
  -c:v libx264 -profile:v baseline -pix_fmt yuv420p -movflags +faststart \
  turin-smart-screen-themes/redskull-2.8inch.mp4

echo "Done. Play with:"
echo "  .venv/bin/python video-mode.py turin-smart-screen-themes/skeleton-skeletons-ezgif-9inch.mp4 --pid 0x0092 --loop"
echo "  .venv/bin/python video-mode.py turin-smart-screen-themes/redskull-2.8inch.mp4 --pid 0x0028 --loop"
