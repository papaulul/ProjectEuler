#  If the numbers 1 to 5 are written out in words: one, two, three, four, five,
#  then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
#
#
#  NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
#  forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
#  letters. The use of "and" when writing out numbers is in compliance with
#  British usage.


di = {1:'one',
2:'two',
3:'three',
4:'four',
5:'five',
6:'six',
7:'seven',
8:'eight',
9:'nine',
10:'ten',
11:'eleven',
12:'twelve',
13:'thirteen',
14:'fourteen',
15:'fifteen',
16:'sixteen',
17:'seventeen',
18:'eighteen',
19:'nineteen',
20:'twenty',
30:'thirty',
40:'fourty',
50:'fifty',
60:'sixty',
70:'seventy',
80:'eighty',
90:'ninety',
100:'hundred',
1000:'onethousand',
0: 'and'}

sum = 0
count=0
#1 to 20
for i in range(1,10):
    sum+=len(di[i])
    count+=1
    sum+=len(di[i*10])
    count+=1

    for k in range(1,10):
        if i > 1:
            sum+=len(di[i*10] + di[k])
            count+=1

    sum+=len(di[i+10])
    count+=1
    sum+=len(di[i]+di[100])
    count+=1

    for j in range(1,10):
        sum+=len(di[i] + di[100] + di[0]+di[j])
        count+=1

        sum+=len(di[i] + di[100] + di[0]+di[j*10])
        count+=1

        for m in range(1,10):
            if j >1:
                sum+=len(di[i] + di[100] + di[0]+di[j*10]+di[m])
                count+=1

        sum+=len(di[i] + di[100] + di[0]+di[j+10])
        count+=1
print("sum: {} and count: {} ".format(sum+len(di[1000]),count+1))
