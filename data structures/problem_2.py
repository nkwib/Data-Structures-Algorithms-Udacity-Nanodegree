
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    files = []

    def recursive_search(suffix, path):
        if (len(suffix) == 0): return
        if (len(path) == 0): return
        try:
            entries = os.listdir(path)
            for e in entries:
                e_path = os.path.join(path, e)
                if os.path.isdir(e_path):
                    recursive_search(suffix, e_path)
                if e.endswith(suffix): 
                    files.append(os.path.join(e_path))
        except:
            return []

    recursive_search(suffix, path)
    return files

def test(s, p):
    res = find_files(s, p)
    if len(res) == 0: 
        print('No file with the extension "{}" found in the path "{}"'.format(s,p))
        return
    for i in res:
        print(i)

test('.py', 'test_folder/')
test('.py', '../../p0/')
test('.c', '../')
test('', '')
test('', '../../')
test('.exe', '../../..')
test('.md', '../')