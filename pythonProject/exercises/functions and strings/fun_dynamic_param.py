def func(*args):
    for i in args:
        print(i)


func(1, 2)
func(3,4,5)
func(1)
func(1, 3, (5, 6, 7))
