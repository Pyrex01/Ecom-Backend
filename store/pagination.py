from rest_framework.pagination import PageNumberPagination ,OrderedDict
from rest_framework.response import Response



class ListPage(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 10000
    def get_paginated_response(self, data):
        return Response(OrderedDict([
             ('countItemsOnPage', self.page_size),
             ('current', self.page.number),
             ('next', self.get_next_link()),
             ('previous', self.get_previous_link()),
             ('results', data)
         ]))