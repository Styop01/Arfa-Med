from rest_framework.pagination import BasePagination, PageNumberPagination
from rest_framework.response import Response

# endpoint --------->  ?start_index=1&end_index=7
class CustomIndexPagination(BasePagination):
    page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        self.start_index = int(request.query_params.get('start_index', 0))
        self.end_index = int(request.query_params.get(
            'end_index', self.start_index + self.page_size))

        # Validate start and end index values
        if self.start_index < 0:
            self.start_index = 0
        if self.end_index < self.start_index:
            self.end_index = self.start_index + self.page_size

        return list(queryset[self.start_index:self.end_index])

    def get_paginated_response(self, data):

        return Response({
            'start_index': self.start_index,
            'end_index': self.end_index - 1,
            'count': self.start_index + len(data),
            'results': data,
        })

#
# class CustomPageNumberPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 1000
