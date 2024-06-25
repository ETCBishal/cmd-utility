from selenium import webdriver
from selenium.webdriver.common.by import By

def get_urls(search):
    """
    Fetch image URLs from Flickr using Selenium WebDriver.

    This function navigates to Flickr and retrieves image URLs based on the specified search term.

    Args:
        search (str): The search term or category of images to fetch from Flickr.

    Returns:
        tuple:
            img_urls (list of str): A list of image URLs retrieved from Flickr.
            custom_img_names (list of str): A list of custom image names based on the search term.

    Example:
        >>> from Utils import get_urls
        >>> img_urls, custom_img_names = get_urls('nature')
    """
    
    browser = webdriver.Firefox()
    browser.get(f'https://www.flickr.com/search/?text={search}')

    img_tags = browser.find_elements(By.TAG_NAME, 'img')

    image_urls = [tag.get_attribute('src') for tag in img_tags]
    image_names = [f'{search}-{i}' for i in range(len(image_urls))]

    return image_urls, image_names
