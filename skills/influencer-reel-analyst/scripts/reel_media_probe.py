#!/usr/bin/env python3
"""Inspect a short-form video and optionally generate a storyboard."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=True, text=True, capture_output=True)


def ffprobe(video: Path) -> dict:
    result = run([
        "ffprobe",
        "-v",
        "error",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        str(video),
    ])
    return json.loads(result.stdout)


def video_summary(data: dict) -> dict:
    stream = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), {})
    fmt = data.get("format", {})
    duration = float(fmt.get("duration", 0) or 0)
    return {
        "duration_seconds": round(duration, 2),
        "duration_label": f"{int(duration // 60)}:{int(duration % 60):02d}",
        "width": stream.get("width"),
        "height": stream.get("height"),
        "fps": stream.get("r_frame_rate"),
        "video_codec": stream.get("codec_name"),
        "bitrate": fmt.get("bit_rate"),
    }


def make_storyboard(video: Path, output: Path, every_seconds: int) -> None:
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg not found")
    output.parent.mkdir(parents=True, exist_ok=True)
    vf = f"fps=1/{every_seconds},scale=180:-1,tile=6x6"
    run([
        "ffmpeg",
        "-hide_banner",
        "-y",
        "-i",
        str(video),
        "-vf",
        vf,
        "-frames:v",
        "1",
        str(output),
    ])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("--storyboard", type=Path)
    parser.add_argument("--every-seconds", type=int, default=3)
    args = parser.parse_args()

    data = ffprobe(args.video)
    summary = video_summary(data)
    if args.storyboard:
        make_storyboard(args.video, args.storyboard, args.every_seconds)
        summary["storyboard"] = str(args.storyboard)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
