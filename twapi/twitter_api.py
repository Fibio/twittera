import twitter

from datetime import timedelta
from urllib.parse import urlencode

from django.conf import settings
from django.utils.timezone import now


class TwitterAPI:
    """Base API to init twitter api and make search."""

    def __init__(self):
        self.api = twitter.Api(**settings.TW_TOKENS)

    def get_search_options(self, options):
        """Return search options for Twitter API from kwargs or use default options from settings"""
        if not options:
            options = settings.DEFAULT_SEARCH_OPTIONS
            since = now() - timedelta(days=7)
            options['since'] = since.date().isoformat()
        return urlencode(options)

    def get_counts(self, *keywords, **options):
        """Get tweets amount for given keywords.

        Args:
        keywords (list): list of keywords to search;
        options (dict): Twitter search API options,
            see: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html;
        """
        data = {}
        options = self.get_search_options(options)
        for word in keywords:
            query = "{}&{}".format(urlencode({'q': word}), options)
            tweets = self.api.GetSearch(raw_query=query)
            data[word] = len(tweets)
        return data
