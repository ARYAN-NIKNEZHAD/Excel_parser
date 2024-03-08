# stuff from rest framework
from rest_framework.pagination import LimitOffsetPagination



class DefaultLimitOffSetPagination(LimitOffsetPagination):
    """
    this is a limit of set pagination 
    limit=number(int)
    """
    
    #  min limit we can pass througth query_params
    min_limit = 1

    # max limit we can pass througth query_params
    max_limit = 100
  
    default_limit = 10 

    def get_limit(self, request):
        """
        Override the `get_limit` method to set a default limit for the number of items returned per page.
        """
        if self.limit_query_param and request.query_params.get(self.limit_query_param):
            try:
                # if the limit was pass is an a, b,c....... pass
                if request.query_params.get(self.limit_query_param).isalpha():
                    pass
                # must be greater than 0 (the limit)
                elif int(request.query_params.get(self.limit_query_param)) > 0:
                    return int(request.query_params.get(self.limit_query_param))

            except (KeyError, ValueError):
                pass

        # Return the default limit otherwise
        return self.default_limit