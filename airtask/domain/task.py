from dataclasses import dataclass
from typing import TypeAlias, Protocol

ParamKey: TypeAlias = str
ParamValue: TypeAlias = str | int | float | bool
ProtocolName: TypeAlias = str
ProtocolImplName: TypeAlias = str


class Task(Protocol):
    """
    This protocol doesn't have `load-`-isy methods. Protocols of each class should declare them.
    """

    def run(self) -> None:
        """
        `run` method doesn't take any parameter. Parameters aren't only for this method, but also for `load` methods.
        :return:
        """
        raise NotImplementedError


class TaskFlow(Protocol):
    def execute(self) -> None:
        raise NotImplementedError


@dataclass
class TaskFlowConfigItem:
    impl_name: ProtocolImplName
    params: dict[ParamKey, ParamValue]
    requirement_params: dict[ProtocolName, "TaskFlowConfigItem"]


class TaskFlowManager(Protocol):
    def generate_flow(self, root_config: TaskFlowConfigItem):
        raise NotImplementedError
