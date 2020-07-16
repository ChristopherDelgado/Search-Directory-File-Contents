# importing os to allow for directory changes
import os

def search_directory(dir, filetype, search) -> list:
    """Search files in the given directory with the given file extension for the desired search criteria"""
    # change directory to the given directory
    os.chdir(dir)
    # declaring the list that will be returned
    files_with_search = []
    # Use a try and except to prevent crashing on no files found
    try:
        # for every object in directory check its extension
        for file in os.listdir(os.getcwd()):
            if file.endswith(filetype):
                # retrieve all instances of the search criteria in the file and append to list
                files_with_search.append(get_instances(file, search))
    except Exception as e:
        raise e
        print('No Files Found')
    return files_with_search


def get_instances(file, search) -> list:
    """Return all instances of the search criteria found in the given file in a list where [0] is the file's name"""
    # save the files name before modifying it into a read file
    file_name = file
    # retrieve full directory of the file
    directory = os.getcwd() + '\\' + file
    # open the file for reading
    file = open(directory, 'r')
    file = file.read()
    if file.__contains__(search):
        this_file_todo = [file_name]
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
    return None


def print_results(double_list, search):
    """Print all files that contain the search criteria as well as what was found"""
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
