from dataclasses import dataclass, field
from typing import Optional, Protocol, TypeVar, Generic

from airtask.domain.types import TaskName, ParamKey, ParamValue, ProtocolName, DependentTaskName

_P = TypeVar("_P", bound=dict[DependentTaskName, type[Protocol]])
_T = TypeVar("_T", bound="Task")


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
    task_name: TaskName  # name of the implementation of the protocol.
    params: dict[ParamKey, ParamValue]
    requirement_params: dict[ProtocolName, "TaskConfig"]


@dataclass
class Task(Generic[_P]):
    dependent_protocols: _P
    """
    This is not a protocol since its implementation doesn't depend on specific frameworks.
    """

    @classmethod
    def from_params(cls: type[_T], params: dict[ParamKey, ParamValue]) -> _T:
        """
        Override this method if you want a customized deserializer
        :param params:
        :return:
        """
        return cls(**params)

    def run(self) -> None:
        """
        `run` method doesn't take any parameter. Parameters aren't only for this method, but also for `load` methods.
        :return:
        """
        raise NotImplementedError


@dataclass
class TaskGraph:
    root_task: Task
    sub_graphs: Optional[list["TaskGraph"]]


@dataclass
class TaskCollection:
    tasks: dict[ProtocolName, dict[TaskName, type[Task]]]
    task_names_to_classes: dict[TaskName, type[Task]] = field(init=False)

    def __post_init__(self):
        self.task_names_to_classes = {}
        for protocol_name, tasks in self.tasks.items():
            for task_name, task_class in tasks.items():
                self.task_names_to_classes[task_name] = task_class


class GraphRunner(Protocol):
    def run(self, graph: TaskGraph) -> None:
        raise NotImplementedError
