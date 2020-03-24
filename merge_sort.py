import tempfile

file_size = 20000

def algoritm_merge_sort(array):
    if len(array) < 2:
        return array
    else:
        middle = int(len(array) / 2)
        left = algoritm_merge_sort(array[:middle])
        right = algoritm_merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def create_ini(range_tempfile):
    file_handles = []
    for _ in range(0, range_tempfile):
        f_handle = tempfile.NamedTemporaryFile(delete=False)
        file_handles.append(f_handle)
    return file_handles




def merge_sort(file_input_name, file_output_name):
    arr_int = []
    temp_file_value = []
    arr_file_temp = []
    count = 0
    file_number = 0
    check = False
    add_iterations = 0
    with open(file_input_name, "r", encoding='utf-8') as file:
        for i in file.read():
            if i == '\n':
                count += 1
            if count == file_size:
                file_number = file_number + 1
                count = 0
        if count > 0:
            file_number += 1
            add_iterations = count
            check = True

    file_handles = create_ini(file_number)

    with open(file_input_name, "r", encoding='utf-8') as file:
        for i in range(0, file_number):
            with open(file_handles[i].name, 'a', encoding='utf-8') as file_temp:
                for j in range(0, file_size):
                    temp = file.readline()
                    if len(temp) > 0:
                        file_temp.write(temp)
                    else:
                        break


    for i in range(0, file_number):
        arr_int.clear()
        with open(file_handles[i].name, "r", encoding='utf-8') as file_temp:
            for j in range(0, file_size):
                temp = file_temp.readline()
                if len(temp) > 0:
                    arr_int.append(int(temp))
                else:
                    break
            arr_int = algoritm_merge_sort(arr_int)

            file_temp2 = open(file_handles[i].name, "w", encoding='utf-8')
            file_temp2.close()

            with open(file_handles[i].name, "a", encoding='utf-8') as file_temp:
                for j in arr_int:
                    file_temp.writelines('{}\n'.format(j))

    arr_int.clear()

    with open(file_output_name, 'a', encoding='utf-8') as file:
        for j in range(0, file_number):
            arr_file_temp.append(open(file_handles[j].name, 'r', encoding='utf-8'))

        for i in range(0, file_number):
            temp = arr_file_temp[i].tell()
            temp_file_value.append(int(arr_file_temp[i].readline()))
            arr_file_temp[i].seek(temp)

        if check:
            n = file_number - 1
        else:
            n = file_number
        for _ in range(0, (n * file_size) + add_iterations + 1):
            min_value = min(temp_file_value)
            for i in range(0, file_number):
                temp = arr_file_temp[i].tell()
                if len(arr_file_temp[i].readline()) > 0:
                    arr_file_temp[i].seek(temp)
                    if int(arr_file_temp[i].readline()) == min_value:
                        print(min_value)
                        file.writelines('{}\n'.format(min_value))
                        temp = arr_file_temp[i].tell()
                        arr_file_temp[i].seek(temp)
                        temp_file_value.remove(min_value)
                        if len(arr_file_temp[i].readline()) > 0:
                            arr_file_temp[i].seek(temp)
                            temp_file_value.append(int(arr_file_temp[i].readline()))
                            arr_file_temp[i].seek(temp)
                        break
                    else:
                        arr_file_temp[i].seek(temp)
    pass

#merge_sort('input_numbers.txt', 'output_numbers.txt')

#with open('output_numbers.txt', 'a', encoding='utf-8') as file:
    #for i in range(0, 250):
        #with open(file_handles[i].name, 'r', encoding='utf-8') as file_temp:
            #file.write(file_temp.read())