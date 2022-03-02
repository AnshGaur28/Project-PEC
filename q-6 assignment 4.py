George = input('input your word george: ')
barbie = input('input your word barbie: ')
def anagraming(s):
    if s=='':
        return [s]
    else:
        ans = []
        for w in anagraming(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans
meaning = (anagraming('eye'))
if barbie in meaning:
    print('true friends')
else:
    print('fake friends')




