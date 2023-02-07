# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# print("\n ---------- \n")

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# tính S = (1 / ((1/3) + (1/5) + (1/7) + ... + (1/99))).
s_denominator = 0
for i in range(3,100,2):
    # if i==1:
    #     continue

    # if i % 2 == 0:
    #     continue

    s_denominator += 1/i

s = 1 / s_denominator
s = round(s,2)

print("S = " + str(s))