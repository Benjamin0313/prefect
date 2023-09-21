# import httpx
# from prefect import flow

# @flow
# def get_repo_info():
#     url = "https://api.github.com/repos/PrefectHQ/prefect"
#     response = httpx.get(url)
#     response.raise_for_status()
#     repo = response.json()
#     print("PrefectHQ/prefect repository statistics 🤓:")
#     print(f"Stars 🌠 : {repo['stargazers_c ount']}")
#     print(f"Forks 🍴 : {repo['forks_count']}")

#####  #####
# import httpx
# from prefect import flow

# @flow
# def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
#     url = f"https://api.github.com/repos/{repo_name}"
#     response = httpx.get(url)
#     response.raise_for_status()
#     repo = response.json()
#     print(f"{repo_name} repository statistics 🤓:")
#     print(f"Stars 🌠 : {repo['stargazers_count']}")
#     print(f"Forks 🍴 : {repo['forks_count']}")

import httpx
from prefect import flow, get_run_logger

@flow(log_prints=True)
def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
    url = f"https://api.github.com/repos/{repo_name}"
    response = httpx.get(url)
    response.raise_for_status()
    repo = response.json()
    logger = get_run_logger()
    logger.info("%s repository statistics 🤓:", repo_name)
    logger.info(f"Stars 🌠 : %d", repo["stargazers_count"])
    logger.info(f"Forks 🍴 : %d", repo["forks_count"])