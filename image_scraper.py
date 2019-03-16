import sys
from google_images_download import google_images_download


def scrape_google_image(keyword, number_of_images):
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": keyword, "limit": number_of_images,
                 "print_urls": False}
    image_paths = response.download(arguments)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Please give option keyword, number_of_images')
    else:
        scrape_google_image(sys.argv[1], sys.argv[2])
