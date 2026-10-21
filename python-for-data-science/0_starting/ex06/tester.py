from ft_filter import ft_filter

numbers = [1, 2, 3, 4, 5]
words = ["Hello", "the", "World"]

print(ft_filter(lambda x: x > 3, numbers))
print(ft_filter(lambda word: len(word) > 4, words))
print(ft_filter(None, [0, 1, "", "hello", False, True]))
print(ft_filter.__doc__ == filter.__doc__)
