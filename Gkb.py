file = open('nuts.txt', 'w+')
text2 = []
p = 0

file.writelines(' 68 ')
file.writelines(' 83 ')
file.writelines(' 9 ')
file.writelines(' 2 ')
file.writelines(' 8 ')
file = open('nuts.txt', 'r+')
text = file.writelines()[0].strip()
rus = ["шестьдесят восемь", "восемьдесят три", "девять", "два", "восемь"]
nums = ["68", "83", "9", "2", "8"]
for i in text.split():
    text2.append(i.replace (nums[p], rus[p]))
    p += 1
file2 = open('nutsRu','w+')
file2.writelines(text)
file2.close()
file.close ()
print(text2)
