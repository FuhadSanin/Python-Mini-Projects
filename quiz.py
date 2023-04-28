def check(x, ans, s):
    score = s
    if ans == x.lower():
        print("Correct !!")
        score += 1
    else:
        print("Incorrect !!")
    return score


s = 0
print("Welcome to Quiz")

d = {
    "1 > Who is the father Computer ? : ": "charles babbage",
    "2 > Who is the father of Computer Science ? ": "alan turing",
    "3 > Who is the founder of Apple ? : ": "steve jobs",
    "4 > What is CPU stands for ? : ": "central processing unit"
}
for i in d:
    x = input(i)
    s = check(x, d.get(i), s)

print(f"\nScore is : {s} / {len(d)}")
