slice_me = ("The", "next", "time", "we", "meet", "drinks", "are", "on", "me")
slice_tuple = slice_me[5:9]
print(slice_tuple)
# result ('drinks', 'are', 'on', 'me')

slice_this_list = ["The", "next", "time", "we", "meet", "drinks", "are", "on", "me"]
slice_list = slice_this_list[5:9]
print(slice_list)
# result ['drinks', 'are', 'on', 'me']

slice_this_string = "The next time we meet, drinks are on me."
slice_string = slice_this_string[5:9]
print(slice_string)
# result 'ext '

# append method
living_room = ("rug", "table", "chair", "TV", "dustbin", "shelf")
apartment = []
apartment.append(living_room)
print(apartment)
# result [('rug', 'table', 'chair', 'TV', 'dustbin', 'shelf')]

# extend method
apartment = []
apartment.extend(living_room)
print(apartment)
# result ['rug', 'table', 'chair', 'TV', 'dustbin', 'shelf']

# stack
todays_temperatures = [23, 32, 33, 31]
todays_temperatures.append(29)
print(todays_temperatures)
# result [23, 32, 33, 31, 29]
morning = todays_temperatures.pop(0)
print("This morning temperature was %.02f" % morning)
# result This morning temperature was 23.00
print(todays_temperatures)
# result [32, 33, 31, 29]
late_morning = todays_temperatures.pop(0)
print("Todays late morning temperature was %.02f." % late_morning)
# result Todays late morning temperature was 32.00.
print(todays_temperatures)
# result [33, 31, 29]
noon = todays_temperatures.pop(0)
print("Todays noon temperature was %.02f." % noon)
# result Todays noon temperature was 33.00.
print(todays_temperatures)
# result [31, 29]
night = todays_temperatures.pop()
print("Todays night temperature was %.02f." % night)
# result Todays night temperature was 29.00.
print(todays_temperatures)
# result [31]
# pop 如果指定元素, 将会把最后一个元素删除, 而不是这里所示的第一个元素

# set
alphabet = ["a", "b", "b", "c", "a", "d", "e"]
print (alphabet)
# result ['a', 'b', 'b', 'c', 'a', 'd', 'e']
alph2 = set(alphabet)
print(alph2)
# result {'b', 'c', 'a', 'd', 'e'}
# 集合中的数据不允许有重复, 所以alphabet中的重复字母 a 和 b 被删除了

