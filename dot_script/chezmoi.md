
https://www.chezmoi.io/user-guide/daily-operations/

## 日常命令

```
alias cm="chezmoi"

cm cd 打开 cm 的 working space
cm add 添加文件
cm edit 编辑文件
    如果不是使用 chezmoi 进行的更新，那么就再一次 cm add 
cm apply
    应用 chezmoi 进行的更新
cm edit --apply
    修改同时进行 local 的更新

cm git pull 从仓库拉取新内容到 local 仓库，
    cm diff 查看不同内容 (q) 退出预览
    如果要进行应用到本地，则再执行一次 cm apply
cm re-add
    将本地的 update 之后的内容 应用到远程
```


## 自动提交的配置

```
~/.config/chezmoi/chezmoi.toml
[git]
    autoCommit = true
    autoPush = true
```

## 新机器

```
sh -c "$(curl -fsLS get.chezmoi.io)" -- init --apply $GITHUB_USERNAME
```

只用一次的新机器

```
sh -c "$(curl -fsLS get.chezmoi.io)" -- init --one-shot $GITHUB_USERNAME
```
