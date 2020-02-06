


n_str_text = 0

with open ('file_2.txt') as f_t:
    for line in f_t:
        #print(line)
        n_str_text += 1
        words = line.split()
        #print(words)
        print(f'строка {n_str_text} , слов:', len(words))



print('колличество строк:', n_str_text)





