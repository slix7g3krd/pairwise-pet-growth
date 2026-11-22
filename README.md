# pairwise-pet-growth

## 领域

游戏、图形与多媒体

## 主题

宠物养成

## 说明

离线结算、固定种子与状态隔离。

初始状态下 `gameplay/pet_growth.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
