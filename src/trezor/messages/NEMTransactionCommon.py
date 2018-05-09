# Automatically generated by pb2py
import protobuf as p
if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None


class NEMTransactionCommon(p.MessageType):
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('network', p.UVarintType, 0),
        3: ('timestamp', p.UVarintType, 0),
        4: ('fee', p.UVarintType, 0),
        5: ('deadline', p.UVarintType, 0),
        6: ('signer', p.BytesType, 0),
    }

    def __init__(
        self,
        address_n: List[int] = None,
        network: int = None,
        timestamp: int = None,
        fee: int = None,
        deadline: int = None,
        signer: bytes = None,
        **kwargs
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.network = network
        self.timestamp = timestamp
        self.fee = fee
        self.deadline = deadline
        self.signer = signer
        super().__init__(**kwargs)
