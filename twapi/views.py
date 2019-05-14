from rest_framework.views import APIView
from rest_framework.response import Response

from .twitter_api import TwitterAPI


class TweetsCountView(APIView):
    """View to build tweets histogram."""

    def get(self, request):
        return Response(TwitterAPI().get_counts('brexit', 'Ukraine'))
