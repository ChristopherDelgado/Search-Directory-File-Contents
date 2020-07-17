# importing os to allow for directory changes
import os
import docx

def search_directory(dir, filetype, search, specific = 1) -> list:
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
                temp_list = get_instances(file, search, specific)
                if temp_list is not None:
                    files_with_search.append(temp_list)
    except Exception as e:
        raise e
        print('No Files Found')
    return files_with_search


def get_instances(file, search, specific) -> list:
    """Return all instances of the search criteria found in the given file in a list where [0] is the file's name"""
    # save the files name before modifying it into a read file
    file_name = file
    # retrieve full directory of the file
    directory = os.getcwd() + '\\' + file
    # handle different file types accordingly
    if file.endswith('.docx'):
        # handle .docx extension
        file = docx.Document(directory)
        temp = ''
        for p in file.paragraphs:
            temp += (r'%s' % p.text) + '\n'
        file = temp
        end_character = '.'
    else:
        # open the file for reading
        file = open(directory, 'r')
        file = file.read()
        end_character = '\n'
    # check if the file holds the desired search criteria
    if file.__contains__(search):
        this_file_todo = [file_name]
        if specific == 0:
            while file.__contains__(search):
                # store index where search is found
                start_index = file.find(search)
                # update file seek location
                temp_file = file[start_index:-1]
                # store newline character index
                end_index = temp_file.find(end_character)
                # if end_index is found as a positive integer add the start index to it
                if end_index >= 0:
                    end_index += start_index
                # append the search to the list and update file seek
                this_file_todo.append('...' + file[start_index:end_index] + '...')
                file = file[end_index:-1]
            return this_file_todo
        else:
            while file.__contains__(search):
                # store index where search is found
                start_index = file.find(search)
                # making sure result is exact match
                temp_exact_file = file[start_index:-1]
                temp_end_index = temp_exact_file.find(' ') + start_index
                temp_result = file[start_index:temp_end_index]
                if search.__eq__(temp_result):
                    # update file seek location
                    temp_file = file[start_index:-1]
                    # store newline character index
                    end_index = temp_file.find(end_character)
                    # if end_index is found as a positive integer add the start index to it
                    if end_index >= 0:
                        end_index += start_index
                    # append the search to the list and update file seek
                    this_file_todo.append('...' + file[start_index:end_index] + '...')
                    file = file[end_index:-1]
                else:
                    file = file[temp_end_index:-1]
            return this_file_todo

    return None


def print_results(double_list, search):
    """Print all files that contain the search criteria as well as what was found"""
    input('%d Files found containing "%s" press ENTER for first file\n' % (len(double_list), search))
    for list in double_list:
        for index in range(0, len(list)):
            print(list[index])
        input('\npress ENTER for the next file\n')

