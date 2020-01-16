
class DetailSerializerMixin:

    serializer_detail_class = None

    def get_serializer_class(self):
        error_message = "'{0}' should include a 'serializer_detail_class' attribute".format(self.__class__.__name__)
        
        assert self.serializer_detail_class is not None, error_message
        
        if self.action == 'retrieve':
            return self.serializer_detail_class
        else:
            return super().get_serializer_class()

class CreateSerializerMixin:

    serializer_create_class = None

    def get_serializer_class(self):
        error_message = "'{0}' should include a 'serializer_create_class' attribute".format(self.__class__.__name__)
        
        assert self.serializer_create_class is not None, error_message
        
        if self.action == 'create':
            return self.serializer_create_class
        else:
            return super().get_serializer_class()

class UpdateSerializerMixin:

    serializer_update_class = None

    def get_serializer_class(self):
        error_message = "'{0}' should include a 'serializer_update_class' attribute".format(self.__class__.__name__)
        
        assert self.serializer_update_class is not None, error_message
        
        if self.action == 'update':
            return self.serializer_update_class
        else:
            return super().get_serializer_class()