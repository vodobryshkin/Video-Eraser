from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def to_seconds(time):
    time_list = time.split(':')

    seconds = time_list[-1]

    if ',' in seconds:
        seconds_list = seconds.split(',')
        k = 1

        for i in range(len(seconds_list[1])):
            k *= 0.1

        opt = int(seconds_list[0]) + int(seconds_list[1]) * k
    else:
        opt = int(time_list[-1])

    return int(time_list[0]) * 3600 + int(time_list[1]) * 60 + opt


def film_crop(start_time, end_time, name, target_name):
    ffmpeg_extract_subclip(name, to_seconds(start_time), to_seconds(end_time), targetname=target_name)
