from prefect import flow

@flow(name="My Flow")
def my_flow():
    return 1 + 1
