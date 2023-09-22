# import httpx
# from prefect import flow

####################################################################
########## フロー ##########
# @flow
# def get_repo_info():
#     url = "https://api.github.com/repos/PrefectHQ/prefect"
#     response = httpx.get(url)
#     response.raise_for_status()
#     repo = response.json()
#     print("PrefectHQ/prefect repository statistics 🤓:")
#     print(f"Stars 🌠 : {repo['stargazers_c ount']}")
#     print(f"Forks 🍴 : {repo['forks_count']}")

##### 引数を追加 #####
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

##### ログ #####
# import httpx
# from prefect import flow, get_run_logger

# @flow(log_prints=True)
# def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
#     url = f"https://api.github.com/repos/{repo_name}"
#     response = httpx.get(url)
#     response.raise_for_status()
#     repo = response.json()
#     logger = get_run_logger()
#     logger.info("%s repository statistics 🤓:", repo_name)
#     logger.info(f"Stars 🌠 : %d", repo["stargazers_count"])
#     logger.info(f"Forks 🍴 : %d", repo["forks_count"])

##### 再実行 #####
# import httpx
# from prefect import flow

# @flow(retries=3, retry_delay_seconds=5, log_prints=True)
# def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
#     url = f"https://api.github.com/repos/{repo_name}"
#     response = httpx.get(url)
#     response.raise_for_status()
#     repo = response.json()
#     print(f"{repo_name} repository statistics 🤓:")
#     print(f"Stars 🌠 : {repo['stargazers_count']}")
#     print(f"Forks 🍴 : {repo['forks_count']}")

####################################################################
########## タスク ##########
# import httpx
# from prefect import flow, task


# @task
# def get_url(url: str, params: dict = None):
#     response = httpx.get(url, params=params)
#     response.raise_for_status()
#     return response.json()


# @flow(retries=3, retry_delay_seconds=5, log_prints=True)
# def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
#     url = f"https://api.github.com/repos/{repo_name}"
#     repo_stats = get_url(url)
#     print(f"{repo_name} repository statistics 🤓:")
#     print(f"Stars 🌠 : {repo_stats['stargazers_count']}")
#     print(f"Forks 🍴 : {repo_stats['forks_count']}")

##### キャッシング
# import httpx
# from datetime import timedelta
# from prefect import flow, task, get_run_logger
# from prefect.tasks import task_input_hash


# @task(cache_key_fn=task_input_hash, 
#       cache_expiration=timedelta(hours=1),
#       )
# def get_url(url: str, params: dict = None):
#     response = httpx.get(url, params=params)
#     response.raise_for_status()
#     return response.json()

# import httpx
# from datetime import timedelta
# from prefect import flow, task
# from prefect.tasks import task_input_hash


# @task(cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=1))
# def get_url(url: str, params: dict = None):
#     response = httpx.get(url, params=params)
#     response.raise_for_status()
#     return response.json()


# def get_open_issues(repo_name: str, open_issues_count: int, per_page: int = 100):
#     issues = []
#     pages = range(1, -(open_issues_count // -per_page) + 1)
#     for page in pages:
#         issues.append(
#             get_url(
#                 f"https://api.github.com/repos/{repo_name}/issues",
#                 params={"page": page, "per_page": per_page, "state": "open"},
#             )
#         )
#     return [i for p in issues for i in p]


# @flow(retries=3, retry_delay_seconds=5, log_prints=True)
# def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
#     repo_stats = get_url(f"https://api.github.com/repos/{repo_name}")
#     issues = get_open_issues(repo_name, repo["open_issues_count"])
#     issues_per_user = len(issues) / len(set([i["user"]["id"] for i in issues]))
#     print(f"{repo_name} repository statistics 🤓:")
#     print(f"Stars 🌠 : {repo_stats['stargazers_count']}")
#     print(f"Forks 🍴 : {repo_stats['forks_count']}")
#     print(f"Average open issues per user 💌 : {issues_per_user:.2f}")

# import httpx
# from datetime import timedelta
# from prefect import flow, task
# from prefect.tasks import task_input_hash


# @task(cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=1))
# def get_url(url: str, params: dict = None):
#     response = httpx.get(url, params=params)
#     response.raise_for_status()
#     return response.json()


# def get_open_issues(repo_name: str, open_issues_count: int, per_page: int = 100):
#     issues = []
#     pages = range(1, -(open_issues_count // -per_page) + 1)
#     for page in pages:
#         issues.append(
#             get_url(
#                 f"https://api.github.com/repos/{repo_name}/issues",
#                 params={"page": page, "per_page": per_page, "state": "open"},
#             )
#         )
#     return [i for p in issues for i in p]


# @flow(retries=3, retry_delay_seconds=5, log_prints=True)
# def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
#     repo_stats = get_url(f"https://api.github.com/repos/{repo_name}")
#     issues = get_open_issues(repo_name, repo_stats["open_issues_count"])
#     issues_per_user = len(issues) / len(set([i["user"]["id"] for i in issues]))
#     print(f"{repo_name} repository statistics 🤓:")
#     print(f"Stars 🌠 : {repo_stats['stargazers_count']}")
#     print(f"Forks 🍴 : {repo_stats['forks_count']}")
#     print(f"Average open issues per user 💌 : {issues_per_user:.2f}")

import httpx
from prefect import flow

@flow(log_prints=True)
def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
    url = f"https://api.github.com/repos/{repo_name}"
    response = httpx.get(url)
    response.raise_for_status()
    repo = response.json()
    print(f"{repo_name} repository statistics 🤓:")
    print(f"Stars 🌠 : {repo['stargazers_count']}")
    print(f"Forks 🍴 : {repo['forks_count']}")


if __name__ == "__main__":
    get_repo_info.serve(
        name="my-first-deployment",
        cron="* * * * *",
        tags=["testing", "tutorial"],
        description="Given a GitHub repository, logs repository statistics for that repo.",
        version="tutorial/deployments",
    )
