import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid_file_link(link, base_url):
    """
    Check if the link is a valid file link.
    """
    parsed_link = urlparse(urljoin(base_url, link))
    return bool(parsed_link.netloc) and bool(parsed_link.path)

def download_file(file_url, download_folder):
    """
    Download a file from the given URL to the specified folder.
    """
    # Get the filename from the URL
    filename = os.path.basename(urlparse(file_url).path)
    download_path = os.path.join(download_folder, filename)

    # Download the file
    print(f'Downloading {file_url} to {download_path}')
    response = requests.get(file_url, stream=True)
    response.raise_for_status()

    # Save the file
    with open(download_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

def download_files_from_url(url, download_folder):
    """
    Download all files linked from the specified URL to the given folder.
    """
    # Make a request to the website
    response = requests.get(url)
    response.raise_for_status()  # Check that the request was successful

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links
    links = soup.find_all('a')

    # Create the download folder if it does not exist
    os.makedirs(download_folder, exist_ok=True)

    # Loop through all the links
    for link in links:
        href = link.get('href')
        if href and is_valid_file_link(href, url):
            file_url = urljoin(url, href)
            try:
                download_file(file_url, download_folder)
            except Exception as e:
                print(f'Failed to download {file_url}: {e}')

if __name__ == '__main__':
    url = 'https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/'  # Replace with the target URL
    download_folder = 'downloaded_files'  # Replace with your desired download folder
    download_files_from_url(url, download_folder)