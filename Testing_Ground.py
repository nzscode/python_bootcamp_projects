# numlist1 = [3,6,5,8,33,12,7,4,72,2,42,13]
# numlist2 = [3,6,13,5,7,89,12,3,33,34,1,344,42]

with open("file1.txt") as file1:
    nums1 = []
    for line in file1:
        nums1.append(int(line.strip('\n')))

with open("file2.txt") as file2:
    nums2 = []
    for line in file2:
        nums2.append(int(line.strip('\n')))

result = []
for num in nums1:
    if num in nums2:
        result.append(num)

print(result)