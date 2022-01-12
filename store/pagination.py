from rest_framework.pagination import PageNumberPagination ,OrderedDict,replace_query_param,remove_query_param
from rest_framework.response import Response



class ListPage(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_next_link(self):
        if not self.page.has_next():
            return None
        url = self.request.build_absolute_uri('https://shopingbazar.sytes.net')
        page_number = self.page.next_page_number()
        return replace_query_param(url, self.page_query_param, page_number)
    
    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        if page_number == 1:
            return remove_query_param(url, self.page_query_param)
        return replace_query_param(url, self.page_query_param, page_number)

    def get_paginated_response(self, data):
        return Response(OrderedDict([
             ('current', self.page.number),
             ('next', self.get_next_link()),
             ('previous', self.get_previous_link()),
             ('results', data)
         ]))