# MyLeetcodeLog

本仓库为本人Leetcode刷题记录之用，仓库按照简单、中等、困难分为三个文件夹，其中解法和解析位于一个md文件中（不包含示例、提示等），所有包含的题解均在`List.md`中记录，以便搜索。

为便于学习数据结构及算法，本仓库题解均使用`python3`

## collections

该文件夹下为题目合集，每个子文件夹为一个单独的合集，合集中仅包含一个`README.md`，记录了该合集所包含的题目及题解，并附链接指向仓库内题解

## update

本仓库使用`update.py`来更新，该文件接收一个参数[push/pull]

使用`pull`来拉取最新的仓库：

```bash
python3 update.py pull
```

使用`push`来推送最新版本到GitHub：

```bash
python3 update.py push
```

使用`update.py`推送时，自动使用"update"作为`commit`，并自动生成最新的`List.md`
