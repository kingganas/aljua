import subprocess

def start_ffmpeg(input_url, output_dir):
    output_path = f"{output_dir}/output_hd.m3u8"
    ffmpeg_cmd = [
        "nohup", "ffmpeg",
        "-i", input_url,
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-tune", "zerolatency",
        "-r", "30",
        "-b:v", "1000k",
        "-maxrate", "1000k",
        "-bufsize", "3200k",
        "-g", "30",
        "-c:a", "aac",
        "-ar", "44100",
        "-b:a", "64k",
        "-start_number", "0",
        "-hls_time", "1",
        "-hls_list_size", "15",
        "-hls_flags", "delete_segments+independent_segments",
        "-y", output_path
    ]
    subprocess.Popen(ffmpeg_cmd)

input_url = "rtmp://140.99.130.9/live/stream"
output_dir = "stream"
start_ffmpeg(input_url, output_dir)
