from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from fantasy import APIClient


class Client:
    def __init__(self, api_client: APIClient):
        self.api: APIClient = api_client
