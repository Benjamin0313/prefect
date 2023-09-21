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

