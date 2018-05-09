# Automatically generated by pb2py
import protobuf as p


class CosiSignature(p.MessageType):
    FIELDS = {
        1: ('signature', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 74

    def __init__(
        self,
        signature: bytes = None,
        **kwargs
    ) -> None:
        self.signature = signature
        super().__init__(**kwargs)
