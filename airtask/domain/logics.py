from typing import Optional

from airtask.domain.exceptions import UnknownTaskName, UnknownProtocolName
from airtask.domain.models import TaskGraph, TaskCollection, TaskConfig, Task
from airtask.domain.types import ProtocolName


def hydrate_graph(
    root_config: TaskConfig,
    collection: TaskCollection,
    protocol_name: Optional[ProtocolName] = None,
) -> TaskGraph:
    if protocol_name is not None:
        try:
            root_task_class = collection.tasks[protocol_name]
        except KeyError:
            raise UnknownProtocolName(protocol_name)
    else:
        try:
            root_task_class = collection.task_names_to_classes[root_config.task_name]
        except KeyError:
            raise UnknownTaskName(root_config.task_name)
    # hydrate root task
    root_task = root_task_class.from_params(root_config.params)
    sub_graphs = [
        hydrate_graph(
            root_config=config, collection=collection, protocol_name=protocol_name
        )
        for protocol_name, config in root_config.requirement_params
    ]
    return TaskGraph(root_task=root_task, sub_graphs=sub_graphs)
