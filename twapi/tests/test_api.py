import os

import vcr
from django.test import TestCase

from twapi.twitter_api import TwitterAPI


CUR_DIR = os.path.dirname(os.path.realpath(__file__))


class TwitterAPITestCase(TestCase):

    @vcr.use_cassette(f'{CUR_DIR}/vcr_cassettes/tweets.yaml', match_on=['path'])
    def test_get_counts_should_return_tweets_amount(self):
        counts = TwitterAPI().get_counts('brexit', 'Ukraine')
        self.assertDictEqual(counts, {'brexit': 71, 'Ukraine': 53})
