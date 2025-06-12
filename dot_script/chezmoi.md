
## 日常命令

```

alias cm="chezmoi"

cm add 添加文件
cm edit 编辑文件
    如果不是使用 chezmoi 进行的更新，那么就再一次 cm add 
cm apply 应用 chezmoi 进行的更新
cm pull 从仓库拉取新内容到 local 仓库，如果要进行应用，则再执行一次 cm apply 
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
