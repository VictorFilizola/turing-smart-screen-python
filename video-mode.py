#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-or-later
#
# turing-smart-screen-python - a Python system monitor and library for USB-C displays like Turing Smart Screen or XuanFang
# https://github.com/mathoudebine/turing-smart-screen-python/
#
# Copyright (C) 2021 Matthieu Houdebine (mathoudebine)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Minimal video player for Turing USB screens (TUR_USB revision: 2.8" round, 4.6", 5.2", 8", 8.8", 9.2", 12.3")
#
# Usage:
#   python video-mode.py res/videos/matrix.mp4              # play once
#   python video-mode.py res/videos/matrix.mp4 --loop       # loop until Ctrl+C
#   python video-mode.py res/videos/matrix.mp4 --pid 0x0092 # target 9.2" screen
#   python video-mode.py res/videos/matrix.mp4 --pid 0x0028 # target 2.8" round screen
#
# Screen auto-detected when --pid omitted (AUTO).

import argparse

from library.pythoncheck import check_python_version
check_python_version()

from library.lcd.lcd_comm_turing_usb import LcdCommTuringUSB, send_video
from library.log import logger


def main():
    parser = argparse.ArgumentParser(
        description="Play an MP4 video on a Turing USB screen (TUR_USB revision).")
    parser.add_argument("video", help="Path to the .mp4 video file")
    parser.add_argument("--loop", action="store_true", help="Loop the video until interrupted")
    parser.add_argument("--pid", default="AUTO",
                        help="USB product id in hex (0x0092 = 9.2\", 0x0028 = 2.8\" round), or AUTO (default)")
    parser.add_argument("--brightness", type=int, default=100, help="Screen brightness in %% (0-100, default 100)")
    args = parser.parse_args()

    lcd = LcdCommTuringUSB(com_port=args.pid)
    lcd.InitializeComm()
    lcd.SetBrightness(args.brightness)

    logger.info("Playing %s (loop=%s)", args.video, args.loop)
    send_video(lcd.dev, args.video, loop=args.loop, brightness=args.brightness)


if __name__ == "__main__":
    main()
