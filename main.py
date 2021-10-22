#Add item to python list
languages = ['C', 'Kotlin', 'Javascript']
user_input = input('Enter a programming language...')
languages.append(user_input)
for i in languages:
  print(i)
#Result
>>Enter a programming language...[ Python|    ]
>>'C'
>>'Kotlin'
>>'Javascript'
>>'Python'