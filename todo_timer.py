import time
import json

DATA_FILE = "tasks.json"

# 读取本地保存的任务
def load_tasks():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# 保存任务到本地json文件
def save_tasks(task_list):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(task_list, f, ensure_ascii=False, indent=2)

# 添加待办任务
def add_task(task_list):
    content = input("\n请输入任务内容：")
    cate = input("任务分类(学习/社团/生活)：")
    new_task = {
        "content": content,
        "category": cate,
        "finished": False
    }
    task_list.append(new_task)
    print("✅任务添加成功！")
    return task_list

# 展示全部任务
def show_tasks(task_list):
    if len(task_list) == 0:
        print("\n📋 暂无任务")
        return
    print("\n===== 我的待办列表 =====")
    for idx, task in enumerate(task_list):
        status = "✅已完成" if task["finished"] else "⏳未完成"
        print(f"{idx+1}. {status} |【{task['category']}】{task['content']}")

# 修改任务完成状态
def finish_task(task_list):
    show_tasks(task_list)
    try:
        num = int(input("\n输入要标记完成的任务序号：")) - 1
        if 0 <= num < len(task_list):
            task_list[num]["finished"] = True
            print("✅标记完成！")
        else:
            print("序号不存在")
    except ValueError:
        print("输入格式错误")
    return task_list

# 番茄专注计时器
def tomato_timer():
    try:
        minute = int(input("\n请输入专注时长(分钟)："))
        total = minute * 60
        print(f"\n🍅开始{minute}分钟专注计时！")
        while total > 0:
            mins = total // 60
            secs = total % 60
            print(f"\r剩余时间：{mins:02d}:{secs:02d}", end="")
            time.sleep(1)
            total -= 1
        print("\n⏰计时结束！休息一下")
    except ValueError:
        print("输入数字！")

def main():
    task_list = load_tasks()
    while True:
        print("\n======== 大学待办&番茄计时器 ========")
        print("1. 添加任务")
        print("2. 查看全部任务")
        print("3. 标记任务完成")
        print("4. 开启番茄专注计时")
        print("5. 退出程序")
        opt = input("\n请选择功能：")
        if opt == "1":
            task_list = add_task(task_list)
        elif opt == "2":
            show_tasks(task_list)
        elif opt == "3":
            task_list = finish_task(task_list)
        elif opt == "4":
            tomato_timer()
        elif opt == "5":
            save_tasks(task_list)
            print("💾任务已保存，程序退出")
            break
        else:
            print("输入无效，请重新选择")

if __name__ == "__main__":
    main()