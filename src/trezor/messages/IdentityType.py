# Automatically generated by pb2py
import protobuf as p


class IdentityType(p.MessageType):
    FIELDS = {
        1: ('proto', p.UnicodeType, 0),
        2: ('user', p.UnicodeType, 0),
        3: ('host', p.UnicodeType, 0),
        4: ('port', p.UnicodeType, 0),
        5: ('path', p.UnicodeType, 0),
        6: ('index', p.UVarintType, 0),  # default=0
    }

    def __init__(
        self,
        proto: str = None,
        user: str = None,
        host: str = None,
        port: str = None,
        path: str = None,
        index: int = None,
        **kwargs
    ) -> None:
        self.proto = proto
        self.user = user
        self.host = host
        self.port = port
        self.path = path
        self.index = index
        super().__init__(**kwargs)
