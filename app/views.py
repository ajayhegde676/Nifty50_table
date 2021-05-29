from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from nsetools import Nse
from rest_framework.response import Response


class NiftyView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Nifty.html'

    def get(self,request):
        nse = Nse()
        top_gainers = nse.get_top_gainers()
        top_losers = nse.get_top_losers()
        return Response ({'gainer':top_gainers,'loser':top_losers})


