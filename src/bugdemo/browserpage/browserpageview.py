from Products.Five.browser import BrowserView

class TestView1(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request
        print "testview_1"

class TestView2(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request
        print "testview_2"
