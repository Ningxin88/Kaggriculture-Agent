# submission.py
def melon_maxxer(obs):
    # 1. 读取当前的世界状态（Observe）
    farms = obs.get("farms", [])
    player = obs.get("player", 0)

    if not farms or player >= len(farms):
        return {"farmer": ["PASS"], "hands": [], "market": []}

    farm = farms[player]
    fx, fy = farm["farmer"]
    tile = farm["tiles"][fy][fx]
    money = farm["money"]

    private = obs.get("private", {}) or {}
    seeds = private.get("seeds", {}) or {}
    shed = private.get("shed", {}) or {}
    market_prices = (obs.get("market", {}) or {}).get("prices", {}) or {}
    melon_price = market_prices.get("MELON", 0)

    market = []
    farmer = ["PASS"]

    # ==========================
    # 逻辑A：市场交易（Market）
    # ==========================
    melons_in_shed = shed.get("MELON", 0)

    # 1. 卖瓜策略
    if melons_in_shed > 0:
        if melon_price >= 250:
            market.append(["SELL", "MELON", melons_in_shed])  # 极高价全卖
        elif melon_price >= 180:
            market.append(["SELL", "MELON", melons_in_shed // 2])  # 价格适中卖一半

    # 2. 买种子策略（给农民留够买种子和应急的钱）
    melon_seed_cost = 100  # 假设西瓜种子100块
    if seeds.get("MELON", 0) == 0 and money >= (melon_seed_cost + 200):
        market.append(["BUY_SEED", "MELON", 1])

    # 3. 雇工人策略
    worker_count = len(farm.get("hands", []))
    if money > 2500 and worker_count == 0:
        market.append(["HIRE"])

    # ==========================
    # 逻辑B：农民动作（Farmer）
    # ==========================
    if isinstance(tile, dict):
        kind = tile.get("kind")
        if kind == "PLANT":
            if tile.get("yield_units", 0) > 0:
                farmer = ["HARVEST"]
            elif not tile.get("watered_today", False):
                farmer = ["WATER"]
            else:
                farmer = ["PASS"]
        elif kind == "WEED":
            farmer = ["DIG"]
        elif kind == "ANIMAL":
            farmer = ["PASS"]
    elif tile is None:
        # 如果是空地，检查手里有没有种子
        if seeds.get("MELON", 0) > 0:
            farmer = ["PLANT", "MELON"]
        else:
            farmer = ["PASS"]  # 没种子，原地等待买种子

    # ==========================
    # 逻辑C：工人调度（Hands）
    # ==========================
    hands = []
    if worker_count > 0:
        # 只有买到工人后，这里才会执行。让所有工人原地待命
        for _ in range(worker_count):
            hands.append(["PASS"])

    # ==========================
    # 3. 返回动作（Act）
    # ==========================
    return {"farmer": farmer, "hands": hands, "market": market}