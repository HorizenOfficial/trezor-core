# Automatically generated by pb2py
import protobuf as p


class FirmwareUpload(p.MessageType):
    FIELDS = {
        1: ('payload', p.BytesType, 0),  # required
        2: ('hash', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 7

    def __init__(
        self,
        payload: bytes = None,
        hash: bytes = None,
        **kwargs
    ) -> None:
        self.payload = payload
        self.hash = hash
        super().__init__(**kwargs)
