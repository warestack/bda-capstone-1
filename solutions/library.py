# # import yt_dlp


# # def download_video(url):
# #     ydl_opts = {
# #         "outtmpl": "videos/%(title)s.%(ext)s"
# #     }

# #     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #         ydl.download([url])

# import csv
# import yt_dlp


# def download_video(url):
#     ydl_opts = {
#         "outtmpl": "videos/%(title)s.%(ext)s"
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])


# def read_video_urls(csv_path):
#     urls = []

#     with open(csv_path, newline="") as file:
#         reader = csv.DictReader(file)

#         for row in reader:
#             urls.append(row["url"])

#     return urls

import csv
import yt_dlp


def read_video_urls(csv_path):
    urls = []

    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            urls.append(row["url"])

    return urls


def download_video(url):
    ydl_opts = {
        "outtmpl": "videos/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])