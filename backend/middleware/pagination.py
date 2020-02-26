from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from collections import OrderedDict

class CustomPagination(PageNumberPagination):

    page_size_query_param = 'pageSize'
    page_query_param = 'pageNo'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('totalCount', self.page.paginator.count),
            ('pageNo', self.page.number),
            ('data', data),
        ]))