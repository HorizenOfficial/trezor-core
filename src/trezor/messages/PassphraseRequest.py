# Automatically generated by pb2py
import protobuf as p


class PassphraseRequest(p.MessageType):
    FIELDS = {
        1: ('on_device', p.BoolType, 0),
    }
    MESSAGE_WIRE_TYPE = 41

    def __init__(
        self,
        on_device: bool = None,
        **kwargs
    ) -> None:
        self.on_device = on_device
        super().__init__(**kwargs)
