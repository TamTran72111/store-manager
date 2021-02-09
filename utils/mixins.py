from unidecode import unidecode


def _generate_search_name(name):
    return unidecode(name).lower()


class SearchNameMixin:
    """
    This mixin helps convert unicode name to ascii search_name. It also
    provides a `search` method.
    """

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        instance.search_name = _generate_search_name(instance.name)

    @classmethod
    def search(cls, name):
        search_name = _generate_search_name(name)
        return cls.objects\
            .filter(search_name__contains=search_name)\
            .order_by('search_name')
