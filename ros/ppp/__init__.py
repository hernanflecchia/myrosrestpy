from ros._base import BaseModule, BaseProps

from .aaa import PPPAAA
from .profile import PPPProfile
from .secret import PPPSecret
from .active import PPPActive


class PPPModule(BaseModule):
    _profile: BaseProps[PPPProfile] = None
    _secret: BaseProps[PPPSecret] = None
    _active: BaseProps[PPPActive] = None

    @property
    def aaa(self) -> PPPAAA:
        return self.ros.get_as("/ppp/aaa", PPPAAA)

    @property
    def profile(self):
        if not self._profile:
            self._profile = BaseProps(self.ros, "/ppp/profile", PPPProfile)
        return self._profile

    @property
    def secret(self):
        if not self._secret:
            self._secret = BaseProps(self.ros, "/ppp/secret", PPPSecret)
        return self._secret

    @property
    def active(self):
        if not self._active:
            self._active = BaseProps(self.ros, "/ppp/active", PPPActive)
        return self._active
    
__all__ = ["PPPAAA", "PPPModule", "PPPProfile", "PPPSecret", "PPPActive"]
