# [Tutorial Overview](https://docs.prefect.io/latest/tutorial/)

## フロー
- 内容
  - 入力を受け取る
  - 作業を実行
  - 出力を返す
  
- @flow デコレータを追加することでフローを作成する
```
17:09:39.219 | INFO    | prefect.engine - Created flow run 'wise-labradoodle' for flow 'get-repo-info'
PrefectHQ/prefect repository statistics 🤓:
Stars 🌠 : 12844
Forks 🍴 : 1330
17:09:39.626 | INFO    | Flow run 'wise-labradoodle' - Finished in state Completed()
```

- log_prints=True
  - print でも同じ出力が得られそう

- [Prefect アーティファクト](https://docs.prefect.io/latest/tutorial/flows/)
  - 上を使ってメトリクスと出力の保存

- 対象のフローを実行して、対話的に実行できる
```
python -i repo_info.py

get_repo_info()
```


## タスク
- @task
  - フロー内で呼び出されるデコレーターで修飾された関数
  - タスクを接続するもの
  - 全てのタスクはフローから呼び出される
  - キャッシュがあるらしい

## デプロイメント
- スケジュールやイベントをトリガーに実行したい