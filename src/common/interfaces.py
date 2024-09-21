from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class ICoordinatesClient(ABC):
    city: str

    @abstractmethod
    def execute(self):
        raise NotImplementedError


@dataclass
class ICityClient(ABC):
    cities: List

    @abstractmethod
    def execute(self):
        raise NotImplementedError

