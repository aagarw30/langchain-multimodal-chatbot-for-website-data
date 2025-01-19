import requests # Helps to send HTTP requests to a server and get the response.
from bs4 import BeautifulSoup # Helps to parse the structure of a webpage and extract specific parts.
import html2text # Converts webpage HTML into plain text


def get_data_from_website(url):
    """
    This function will help retrieve text content and metadata from a given URL.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        tuple: A tuple containing the text content (str) and metadata (dict).
        text will contain the main content of the webpage in markdown format.
        metadata will contain the title, URL, description, and keywords of the webpage.
    """
    
    
    # Get response from the server
    """
    The requests.get() function sends a GET request to the server and returns the response (downloads the content of the webpage).
    The response object contains the server's response to the HTTP request.
    The status_code attribute of the response object contains the HTTP status code returned by the server.
    If the status code is 500, it means there was a server error.
    """
    response = requests.get(url)
    if response.status_code == 500:
        print("Server error")
        return
    
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    """
    The BeautifulSoup constructor takes two arguments:
    1. The content to be parsed (response.content in this case).
    2. The parser to be used ('html.parser' in this case).
    The parsed content is stored in the soup variable.
    """

    # Removing js and css code
    for script in soup(["script", "style"]):
        script.extract()
        """
        The extract() method removes the tag and its contents from the parse tree.

        """

    # Extract text in markdown format
    html = str(soup)
    html2text_instance = html2text.HTML2Text()
    html2text_instance.images_to_alt = True
    html2text_instance.body_width = 0
    html2text_instance.single_line_break = True
    text = html2text_instance.handle(html)
    """
    The html2text.HTML2Text() class creates an instance of the HTML2Text class.
    The images_to_alt attribute is set to True to convert images to alt text.
    The body_width attribute is set to 0 to remove line wrapping.
    The single_line_break attribute is set to True to remove extra line breaks.
    The handle() method converts the HTML content to plain text.
    
    """

    # Extract page metadata
    try:
        page_title = soup.title.string.strip()
    except:
        page_title = url.path[1:].replace("/", "-")
    meta_description = soup.find("meta", attrs={"name": "description"})
    meta_keywords = soup.find("meta", attrs={"name": "keywords"})
    if meta_description:
        description = meta_description.get("content")
    else:
        description = page_title
    if meta_keywords:
        meta_keywords = meta_description.get("content")
    else:
        meta_keywords = ""

    metadata = {'title': page_title,
                'url': url,
                'description': description,
                'keywords': meta_keywords}

    return text, metadata

"""
this will return the text content and metadata of the webpage.
the logic includes:
try for the page title, if not found, then use the path of the URL.
find the meta description and keywords of the webpage.
create a dictionary with the title, URL, description, and keywords.
finally, return the text content and metadata as a tuple.

"""

# Calling the web crawling function :
#textt, metadataa = get_data_from_website("https://creditcards.wellsfargo.com/?sub_channel=WEB&vendor_code=WF")

#print(textt)

#print(metadataa)