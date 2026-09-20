from kaggle_environments import make
from submission import melon_maxxer

print("开始运行模拟环境")

env = make("kaggriculture",configuration={"episodeSteps":720},debug=True)

env.run([melon_maxxer,"random"])

with open("replay.html","w",encoding="utf-8") as f:
    f.write(env.render(mode="html"))

print("跑完了！请在左侧项目栏找到 replay.html，右键选择 'Open in Browser' 查看录像。")