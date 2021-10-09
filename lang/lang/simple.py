languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%s needs interpreter" %lang)
    elif lang in ['c', 'java']:
        print("%s needs compiler" %lang)
    else:
        print("should not reach here")