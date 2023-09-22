from prefect import flow
from prefect_dbt.cli.commands import DbtCoreOperation

@flow
def trigger_dbt_flow() -> str:
    result = DbtCoreOperation(
        commands=["pwd", "dbt debug", "dbt run"],
        project_dir="./demo_dbt/",
        profiles_dir="./demo_dbt/.dbt"
    ).run()
    return result

trigger_dbt_flow()