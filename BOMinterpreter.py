def input_file():
    BOM_list = []
    with open ('BOM.txt', 'r') as BOM:

        length = BOM.readlines()
        for line in length:
            BOM_list.append(line.strip())

    return BOM_list

BOM_list = input_file()

def print_scripture(start, end):

    if start in BOM_list and end in BOM_list:
        start_index = BOM_list.index(start)
        end_index = BOM_list.index(end)
        current_index = start_index + 1
        while current_index != end_index:
            print(BOM_list[current_index])
            if BOM_list[current_index] == '' and BOM_list[current_index+1] != end:
                current_index +=2
            else:
                current_index+=1
    else:
        print('Invalid Reference!')

def parse_ref(scripture):

    reference = scripture
    ref_list = reference.split()
    numberz = ref_list.pop(-1)
    mid_book = ' '.join(ref_list)
    book = mid_book.title()
    if "Of" in book:
        book = "Words of Mormon"

    if ':' not in numberz:
        chapter = int(numberz)
        start = f"{book} {chapter}"
        end = f"{book} {chapter + 1}"
    elif '-' in numberz:
        verses = numberz.split(':')[1].split('-')
        chapter = numberz.split(':')[0]
        verses[1] = int(verses[1])
        start = f"{book} {chapter}:{verses[0]}"
        end = f"{book} {chapter}:{verses[1]+1}"
    else:
        chapter = int(numberz.split(':')[0])
        verse = int(numberz.split(':')[1])
        start = f"{book} {chapter}:{verse}"
        end = f"{book} {chapter}:{verse + 1}"
    
    print_scripture(start, end)

    return

#parse_ref("Words of mormon 1:1-3")
              
#find_scripture('1 Nephi 3:7')

def main():
    scripture = input("Which verse would you like to read? >> ")

    if scripture == 'exit':
        print('Amen.')
        return
    
    if scripture == "amen.":
        return
    
    try:
        print('')
        parse_ref(scripture)
        main()
    except:
        print('Invalid reference! Try something like >> 1 Nephi 3:7')
        main()

if __name__ == "__main__":
    print('')
    main()