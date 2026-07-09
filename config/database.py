"""MongoDB connection and collection helpers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import PyMongoError, ServerSelectionTimeoutError

from config.settings import settings
from utils.logger import get_logger

logger = get_logger(__name__)


@dataclass
class MongoConnection:
    """Lazy MongoDB connection wrapper."""

    uri: str = settings.mongodb_uri
    database_name: str = settings.mongodb_name
    timeout_ms: int = 5000
    _client: MongoClient[Any] | None = None

    def client(self) -> MongoClient[Any]:
        """Return a MongoDB client, creating it on first use."""

        if self._client is None:
            self._client = MongoClient(self.uri, serverSelectionTimeoutMS=self.timeout_ms)
        return self._client

    def database(self) -> Database[Any]:
        """Return the configured MongoDB database."""

        return self.client()[self.database_name]

    def collection(self, name: str) -> Collection[Any]:
        """Return a MongoDB collection by name."""

        return self.database()[name]

    def is_available(self) -> bool:
        """Return True when MongoDB responds to a ping."""

        try:
            self.client().admin.command("ping")
            return True
        except (ServerSelectionTimeoutError, PyMongoError) as exc:
            logger.warning("MongoDB is not available: %s", exc)
            return False


mongo = MongoConnection()
