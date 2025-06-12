
## 日常命令

cm add 添加文件
cm edit 编辑文件
    如果不是使用 chezmoi 进行的更新，那么就再一次 cm add 
cm apply 应用 chezmoi 进行的更新

## 自动提交的配置

~/.config/chezmoi/chezmoi.toml
[git]
    autoCommit = true
    autoPush = true

## 新机器

sh -c "$(curl -fsLS get.chezmoi.io)" -- init --apply $GITHUB_USERNAME

只用一次的新机器

sh -c "$(curl -fsLS get.chezmoi.io)" -- init --one-shot $GITHUB_USERNAME
