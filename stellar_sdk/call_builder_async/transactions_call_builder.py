from typing import Union

from ..call_builder_async.base_call_builder import BaseCallBuilder
from ..client.base_async_client import BaseAsyncClient


class TransactionsCallBuilder(BaseCallBuilder):
    """Creates a new :class:`TransactionsCallBuilder` pointed to server defined by horizon_url.
    Do not create this object directly, use :func:`stellar_sdk.server.Server.transactions`.

    See `All Transactions <https://www.stellar.org/developers/horizon/reference/endpoints/transactions-all.html>`_

    :param horizon_url: Horizon server URL.
    :param client: The client instance used to send request.
    """

    def __init__(self, horizon_url: str, client: BaseAsyncClient) -> None:
        super().__init__(horizon_url, client)
        self.endpoint: str = "transactions"

    def transaction(self, transaction_hash: str) -> "TransactionsCallBuilder":
        """The transaction details endpoint provides information on a single transaction.
        The transaction hash provided in the hash argument specifies which transaction to load.

        See `Transaction Details <https://www.stellar.org/developers/horizon/reference/endpoints/transactions-single.html>`_


        :param transaction_hash: transaction hash
        :return: current TransactionsCallBuilder instance
        """
        self.endpoint = f"transactions/{transaction_hash}"
        return self

    def for_account(self, account_id: str) -> "TransactionsCallBuilder":
        """This endpoint represents all transactions that affected a given account.

        See `Transactions for Account <https://www.stellar.org/developers/horizon/reference/endpoints/transactions-for-account.html>`_

        :param account_id: account id
        :return: current TransactionsCallBuilder instance
        """
        self.endpoint = f"accounts/{account_id}/transactions"
        return self

    def for_ledger(self, sequence: Union[str, int]) -> "TransactionsCallBuilder":
        """This endpoint represents all transactions in a given ledger.

        See `Transactions for Ledger <https://www.stellar.org/developers/horizon/reference/endpoints/transactions-for-ledger.html>`_

        :param sequence: ledger sequence
        :return: current TransactionsCallBuilder instance
        """
        self.endpoint = f"ledgers/{sequence}/transactions"
        return self

    def include_failed(self, include_failed: bool) -> "TransactionsCallBuilder":
        """Adds a parameter defining whether to include failed transactions. By default only
        transactions of successful transactions are returned.

        :param include_failed: Set to `True` to include failed transactions.
        :return: current TransactionsCallBuilder instance
        """
        self._add_query_param("include_failed", include_failed)
        return self