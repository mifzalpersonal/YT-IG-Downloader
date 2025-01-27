import yt_dlp
import instaloader
from TikTokApi import TikTokApi


def download_youtube_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_instagram_video(url):
    loader = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(loader.context, url.split('/')[-2])
    loader.download_post(post, target="downloads")


def download_tiktok_video(url):
    with TikTokApi() as api:
        video = api.video(id=url.split('/')[-1])
        video.download("downloads/tiktok_video.mp4")


def main():
    print("Rek ngadonlot naon kang? (yt/tt/ig):")
    platform = input().lower()
    print("Asupken link url na:")
    url = input().strip()

    if platform == "yt":
        download_youtube_video(url)
    elif platform == "ig":
        download_instagram_video(url)
    elif platform == "tt":
        download_tiktok_video(url)
    else:
        print("Invalid platform!")


if __name__ == "__main__":
    main()
