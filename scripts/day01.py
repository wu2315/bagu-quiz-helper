a = float(input("输入第一个数："))
b = float(input("输入第二个数："))

print(f"和：{a + b}")
print(f"差：{a - b}")
print(f"积：{a * b}")
if b != 0:
    print(f"商：{a / b}")
else:
    print("除数不能为 0")


# ========== 练习 2：等级判断 ==========
score = float(input("输入考试分数："))   # ← 这行是缺的

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")