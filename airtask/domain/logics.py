from airtask.domain.models import GraphConfig, GraphHydrator, GraphRunner


def run_task(
    config: GraphConfig,
    hydrator: GraphHydrator,
    runner: GraphRunner,
) -> None:
    """
    `run_task` is a function to run a task.
    It takes a configuration of a task graph and a hydrator to generate a task graph.
    Then it runs the task graph.
    """
    task_graph = hydrator.hydrate(config)
    runner.run(graph=task_graph)
