from typing import Union

from httpx import URL as _URL
from urllib.parse import urljoin

URLTypes = Union["URL", str]


class URL(_URL):
    """A subclass of httpx's URL class, with additional convenience methods for URL manipulation."""

    def join(self, url: URLTypes) -> "URL":
        """
        Join the current URL with the given URL.

        Args:
            url (Union[URL, str]): The URL to join with.

        Returns:
            URL: A new URL instance representing the joined URL.

        """
        return URL(urljoin(str(self), str(URL(url))))

    def __truediv__(self, url: URLTypes) -> "URL":
        """
        Append the given URL to the current URL using the '/' operator.

        Args:
            url (Union[URL, str]): The URL to append.

        Returns:
            URL: A new URL instance representing the joined URL.

        """
        return URL(urljoin(str(self) + "/", str(URL(url))))

    def __bool__(self):
        """Return True if the URL is not empty.

        Returns:
            bool: True if the URL is not empty.

        """
        return str(self) != ""

    def replace(self, old: str, new: str) -> "URL":
        """
        Replace a substring in the URL.

        Args:
            old (str): The substring to replace.
            new (str): The new substring to replace with.

        Returns:
            URL: A new URL instance with the substring replaced.

        """
        return URL(str(self).replace(old, new))
