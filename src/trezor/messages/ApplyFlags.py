# Automatically generated by pb2py
import protobuf as p


class ApplyFlags(p.MessageType):
    FIELDS = {
        1: ('flags', p.UVarintType, 0),
    }
    MESSAGE_WIRE_TYPE = 28

    def __init__(
        self,
        flags: int = None,
        **kwargs
    ) -> None:
        self.flags = flags
        super().__init__(**kwargs)
