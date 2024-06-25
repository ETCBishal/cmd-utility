"""
Download images from Flickr based on a search term using Selenium WebDriver and parallel processing.

This script takes a folder path to save images and a search term as command-line arguments. 
It uses a custom `get_urls` function from `Utils.py` to fetch image URLs from Flickr, then 
downloads these images concurrently.

Usage:
    python downloa.py <folder_to_save_img> <search_term>

Example:
    python download.py /path/to/save nature

Arguments:
    folder_to_save_img: The directory where images will be saved.
    search_term: The search term to find images on Flickr.
"""

import sys
import os
import requests
from concurrent.futures import ProcessPoolExecutor
from Utils import get_urls  # custom helper method in Utils.py

# Parse command-line arguments
folder_to_save_img = " ".join(sys.argv[1:2])
search = " ".join(sys.argv[2:])


def download_images(image_url, image_name):
    """
    Download a single image and save it to the specified folder.

    Args:
        image_url (str): The URL of the image to download.
        image_name (str): The name to save the image as.
    """


    response = requests.get(image_url)
    response.raise_for_status()

    try:
        # Ensure the directory exists
        os.makedirs(folder_to_save_img, exist_ok=True)

        print(f"[START] Downloading {image_name}.jpg")
        with open(f"{folder_to_save_img}/{image_name}.jpg", "wb") as image:
            image.write(response.content)
        print(f"[END] Done Downloading {image_name}.jpg")

    except Exception as e:
        print(f"[ERROR] Failed to download {image_name}.jpg: {e}")


if __name__ == "__main__":
    # Get image URLs and names
    image_urls, image_names = get_urls(search)

    # Download images using ProcessPoolExecutor
    with ProcessPoolExecutor() as executor:
        executor.map(download_images, image_urls, image_names)
