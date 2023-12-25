import sys
import os
# 处理不了跨行的docstring
# Unable to process cross-line docstrings
def main():
    if len(sys.argv) != 2:
        print('Too few command-line arguments')
        sys.exit(1)
    path = sys.argv[1]
    if check_is_file(path):
        if check_py_file(path):
            print(get_count(path))
        else:
            print('Not a Python file')
            sys.exit(1)
    else:
        print('File does not exist')
        sys.exit(1)
def check_is_file(path):
    return os.path.isfile(path)
def check_py_file(path):
    return os.path.basename(path).endswith('.py')
def get_count(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.readlines()
        realcontent = [i for i in content if not i.strip().startswith('#') and i.strip() != '' and not i.strip().startswith("'''") and not i.strip().endswith("'''")]
        # realcontent = check_spaces_comments(content)
        # print(realcontent)
    return len(realcontent)
def check_spaces_comments(content):
    local_content = content[:]
    for i in content:
        i.strip()
        if i.startswith('#'):
            local_content.remove(i)
        elif i == '':
            local_content.remove(i)
    # print(local_content)
    return local_content
if __name__ == "__main__":
    main()
'''
aaa
'''
