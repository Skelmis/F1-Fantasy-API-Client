from pydantic import BaseModel


class Reese64Response(BaseModel):
    token: str
    renewInSec: int
    cookieDomain: str


class AuthSubscriberResponse(BaseModel):
    firstName: str
    lastName: str
    homeCountry: str
    id: int
    email: str
    login: str


class AuthDataResponse(BaseModel):
    subscriptionStatus: str
    subscriptionToken: str


class AuthResponse(BaseModel):
    sessionId: str
    passwordIsTemporary: bool
    subscriber: AuthSubscriberResponse
    country: str
    data: AuthDataResponse
