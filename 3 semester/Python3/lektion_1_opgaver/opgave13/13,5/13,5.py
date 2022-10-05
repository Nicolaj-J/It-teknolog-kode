def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        print(helper.calls)
        return func(*args, **kwargs)
    helper.calls = 0
    return helper

@call_counter
def calculate(x):
    return x

for i in range(10):
    if i % 2 == 0:
        print(calculate("hej"))
    else:
        calculate("no")