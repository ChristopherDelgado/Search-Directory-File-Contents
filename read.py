import os


def search_directory(dir, filetype, search) -> list:
    os.chdir(dir)
    files_with_search = []
    try:
        for file in os.listdir(os.getcwd()):
            if file.endswith(filetype):
                files_with_search.append(get_instances(file, search))
    except Exception as e:
        raise e
        print('No Files Found')
    return files_with_search


def get_instances(file, search) -> list:
    this_file_todo = [file]
    directory = os.getcwd() + '\\' + file
    file = open(directory, 'r')
    file = file.read()
    while file.__contains__(search):
        # store index where search is found
        start_index = file.find(search)
        # update file seek location
        temp_file = file[start_index:-1]
        # store newline character index
        end_index = temp_file.find('\n')
        if end_index >= 0:
            end_index += start_index
        # append the search to the list and update file seek
        this_file_todo.append('...' + file[start_index:end_index] + '...')
        file = file[end_index:-1]
    return this_file_todo

def print_results(double_list, search):
    input('%d Files found containing "%s" press ENTER for first file\n' % (len(double_list), search))
    for list in double_list:
        for index in range(0, len(list)):
            print(list[index])
        input('\npress ENTER for the next file\n')

while True:
    m_input = input("Enter directory, .file extension, and search in that format\n")
    m_input = m_input.split(',')
    for i in range(0, len(m_input)):
        m_input[i] = m_input[i].strip()
    print_results(search_directory(m_input[0], m_input[1], m_input[2]), m_input[2])
    m_option = input('Would you like to search another directory?\n')
    if m_option.lower().__eq__('yes'):
        continue
    else:
        break
