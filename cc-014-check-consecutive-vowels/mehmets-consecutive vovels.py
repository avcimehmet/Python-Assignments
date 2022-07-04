vovels = ('a', 'i', 'o', 'u', 'e')

word = input('please enter a string: ')

filter = [i+1 for i in range(len(word)-1) if word[i] in vovels and word[i+1] in vovels]

if len(filter) > 0:
  print('positive')
else:
  print('negative')
    