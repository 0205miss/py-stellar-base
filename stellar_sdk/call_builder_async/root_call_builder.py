from ..call_builder_async.base_call_builder import BaseCallBuilder
from ..client.base_async_client import BaseAsyncClient


class RootCallBuilder(BaseCallBuilder):
    """Creates a new :class:`RootCallBuilder` pointed to server defined by horizon_url.
    Do not create this object directly, use :func:`stellar_sdk.server.Server.root`.

    :param horizon_url: Horizon server URL.
    :param client: The client instance used to send request.
    """

    def __init__(self, horizon_url: str, client: BaseAsyncClient) -> None:
        super().__init__(horizon_url, client)
