# explore_obs.py
from kaggle_environments import make

print("正在初始化环境...")
env = make("kaggriculture", configuration={"episodeSteps": 720}, debug=True)
# 重置环境，获取第0回合的初始状态
states = env.reset()
obs = states[0].observation

print("\n=== 1. Observation 顶层键 ===")
for k in obs.keys():
    print(f"  {k}: {type(obs[k])}")

print("\n=== 2. 关键字段 ===")
print(f"当前回合 step: {obs.get('step')}")
print(f"游戏天数 day: {obs.get('day')}")
print(f"你是玩家: {obs.get('player')}")

print("\n=== 3. 你的农场 (farms[player]) ===")
farm = obs["farms"][obs["player"]]
print(f"资金: {farm.get('money')}")
print(f"农民位置: {farm.get('farmer')}")
# ⚠️ 重点看这里：工人长什么样
print(f"当前工人位置 (hands): {farm.get('hands')}")

tiles = farm.get('tiles', [])
if tiles:
    print(f"土地网格大小: {len(tiles)} x {len(tiles[0])}")
    print(f"第一行地块示例 (看看空地和植物长什么样): \n{tiles[0]}")

print("\n=== 4. 私有库存 (private) ===")
private = obs.get("private", {}) or {}
print(f"种子: {private.get('seeds', {})}")
print(f"仓库: {private.get('shed', {})}")

print("\n=== 5. 市场价格 (market) ===")
market = obs.get("market", {}) or {}
print(f"价格: {market.get('prices', {})}")
print(f"库存: {market.get('inventory', {})}")