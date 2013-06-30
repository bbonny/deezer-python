class Resource(object):
    """
    """

    def __init__(self, resource, options, session):
        self._resource = resource
        self._options = options
        self._session = session


class User(Resource):
    """A Deeser user."""

    def __init__(self, options, session):
        Resource.__init__(self, 'user/{0}', options, session)
        if raw:
            self._parse_raw(raw)
