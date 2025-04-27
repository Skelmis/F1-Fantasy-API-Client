from __future__ import annotations

import json
from typing import Literal

import httpx

from fantasy import models


class Client:
    def __init__(
        self,
        *,
        reese84: str,
        token: str,
    ):
        """Not designed to be instantiated directly."""
        self.reese84 = reese84
        self.token = token
        self._client = httpx.AsyncClient(base_url="https://fantasy.formula1.com/feeds")

    async def request(
        self,
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
        url: str,
        json: dict = None,
    ):
        resp = await self._client.request(method, url, json=json)
        resp.raise_for_status()
        return resp

    @staticmethod
    async def _get_reese_token() -> models.Reese64Response:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                "https://api.formula1.com/6657193977244c13?d=account.formula1.com",
                json={
                    "solution": {
                        "interrogation": {
                            "st": 162229509,
                            "sr": 1959639815,
                            "cr": 78830557,
                        },
                        "version": "stable",
                    },
                    "error": None,
                    "performance": {"interrogation": 185},
                },
            )
            return models.Reese64Response(**resp.json())

    @classmethod
    async def _auth(
        cls, username: str, password: str, reese84: str
    ) -> models.AuthResponse:
        # TODO Implement
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                "https://api.formula1.com/v2/account/subscriber/authenticate/by-password",
                headers={
                    "authority": "api.formula1.com",
                    "pragma": "no-cache",
                    "cache-control": "no-cache",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    "dnt": "1",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "RaceControl",
                    "Content-Type": "application/json",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "apikey": "fCUCjWrKPu9ylJwRAv8BpGLEgiAuThx7",
                    "sec-ch-ua-platform": '"macOS"',
                    "origin": "https://account.formula1.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://account.formula1.com/",
                    "accept-language": "en-US,en;q=0.9",
                    "content-type": "application/json",
                },
                # cookies={
                #     "reese84": reese84,
                #     "login": json.dumps(
                #         {
                #             "event": "login",
                #             "componentId": "component_login_page",
                #             "actionType": "success",
                #         }
                #     ),
                # },
                json={
                    "DistributionChannel": "d861e38f-05ea-4063-8776-a7e2b6d885a4",
                    "Login": username,
                    "Password": password,
                },
            )
            resp.raise_for_status()
            return models.AuthResponse(**resp.json())

    @classmethod
    async def login(cls, username: str, password: str) -> Client:
        """Login to the API and receive a valid client."""
        reese_token = await cls._get_reese_token()
        auth = await cls._auth(username, password, reese_token.token)
