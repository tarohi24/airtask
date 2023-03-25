from dataclasses import dataclass
from typing import Protocol

import pytest

from airtask.domain.task import generate_task_graph
from airtask.domain.types import ProtocolCollection
from airtask.domain.entities import Task


class LoadText(Protocol):
    ...


class GenerateSearchQuery(Protocol):
    ...


class SearchWithQuery(Protocol):
    ...


@dataclass
class LoadTextFromLocal(Task):
    value: int

    @classmethod
    def dependent_protocols(cls) -> dict:
        return dict()


class LoadTextFromRemote(Task):
    @classmethod
    def dependent_protocols(cls) -> dict:
        return dict()


class GenerateSearchQueryImpl(Task):
    message: str

    @classmethod
    def dependent_protocols(cls) -> dict:
        return {
            "load_text": LoadText,
        }


class SearchImpl(Task):
    @classmethod
    def dependent_protocols(cls) -> dict:
        return {
            "query": GenerateSearchQuery,
        }


class TestGenerateTaskGraph:
    @pytest.fixture
    def protocol_collection(self) -> ProtocolCollection:
        return {
            LoadText: [LoadTextFromLocal, LoadTextFromRemote],
            GenerateSearchQuery: [GenerateSearchQueryImpl],
            SearchWithQuery: [SearchImpl],
        }

    def test_generate_task_graph(self, protocol_collection: ProtocolCollection):
        graph = generate_task_graph(
            protocol_collection=protocol_collection,
        )
        pass
