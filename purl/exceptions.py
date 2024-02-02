class PurlException(Exception):
    """
    Custom exception for purl.py
    """

    def __init__(self, message):
        super().__init__(message)

class URLRequired(PurlException):
    """ A valid URL is required to make a request """