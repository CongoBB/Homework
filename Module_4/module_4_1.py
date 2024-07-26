from fake_math import divide as fake_div
from true_math import divide as true_div

result1 = fake_div(420, 5)
result2 = fake_div(3439849238, 0)
result3 = true_div(999, 9)
result4 = true_div(15, 0)

print('{}\n{}\n{}\n{}\n'.format(result1, result2, result3, result4))
