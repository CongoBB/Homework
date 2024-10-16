from pprint import pprint


def introspection_info(obj):
    methods_attributes = dir(obj)
    methods = []
    attributes = []
    for i in range(len(methods_attributes)):
        if not callable(getattr(obj, methods_attributes[i])):
            if hasattr(obj, methods_attributes[i]):
                attributes.append(methods_attributes[i])
        elif callable(getattr(obj, methods_attributes[i])):
            methods.append(methods_attributes[i])
    if not attributes:
        attributes = 'no attributes'
    if not methods:
        methods = 'no methods'
    try:
        obj_name = obj.__name__
    except AttributeError:
        obj_name = 'this object does not have a name'
    obj_dict = {
        'Type': type(obj),
        'Attributes': attributes,
        'Methods': methods,
        'Module': obj.__module__,
        'Object_name': obj_name
    }
    pprint(obj_dict, sort_dicts=False)


class AClass:
    def __init__(self, a_number):
        self.number = a_number
        self.an_attribute = 'im_an_attribute'

    pass


Example = AClass(5)


introspection_info(Example)
