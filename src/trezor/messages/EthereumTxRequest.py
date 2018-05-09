# Automatically generated by pb2py
import protobuf as p


class EthereumTxRequest(p.MessageType):
    FIELDS = {
        1: ('data_length', p.UVarintType, 0),
        2: ('signature_v', p.UVarintType, 0),
        3: ('signature_r', p.BytesType, 0),
        4: ('signature_s', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 59

    def __init__(
        self,
        data_length: int = None,
        signature_v: int = None,
        signature_r: bytes = None,
        signature_s: bytes = None,
        **kwargs
    ) -> None:
        self.data_length = data_length
        self.signature_v = signature_v
        self.signature_r = signature_r
        self.signature_s = signature_s
        super().__init__(**kwargs)
