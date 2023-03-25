from dataclasses import dataclass
from typing import Optional, Protocol, TypeVar

from airtask.domain.types import TaskName, ParamKey, ParamValue, ProtocolName, DependentTaskName

_T = TypeVar("_T", bound=dict[DependentTaskName, type[Protocol]])


@dataclass
class TaskConfig:
    """
    `TaskImplConfig` is a configuration for a task implementation.
    By specifying both a task protocol name and an instance of `TaskImplConfig`, you can generate a task instance.

    Attributes
    - `impl_name` is a name of the implementation of the protocol.
    - `params` is a dictionary of parameters for the task.
    - `requirement_params` is a dict of parameters for the requirements of the task. Its keys are dependency names.
    """
    impl_name: TaskName  # name of the implementation of the protocol.
    params: dict[ParamKey, ParamValue]
    requirement_params: dict[ProtocolName, "TaskConfig"]


@dataclass
class GraphConfig:
    task: TaskConfig


class Task(Protocol[_T]):
    """
    This protocol doesn't have `load-`-isy methods. Protocols of each class should declare them.
    """
    @classmethod
    def dependent_protocols(cls) -> _T:
        raise NotImplementedError

    def run(self) -> None:
        """
        `run` method doesn't take any parameter. Parameters aren't only for this method, but also for `load` methods.
        :return:
        """
        raise NotImplementedError


@dataclass
class TaskGraph:
    root_task: Task
    dependent_tasks: Optional[list["TaskGraph"]]


class GraphHydrator(Protocol):
    def hydrate(self, config: GraphConfig) -> TaskGraph:
        raise NotImplementedError


class GraphRunner(Protocol):
    def run(self, graph: TaskGraph) -> None:
        raise NotImplementedError
