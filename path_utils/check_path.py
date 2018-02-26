from path import *
from type_utils.check import *

check_path = check(is_path, "Argument is not a path: %s")
check_normpath = check(is_normpath, "Argument is not a normalized path: %s")
check_dirpath = check(is_dirpath, "Argument is not a directory path: %s")
check_leaf = check(is_leaf, "Argument is not a leaf path: %s")
check_tar_gz = check(is_targz, "Argument is not a tar.gz path: %s")
check_tgz = check(is_tgz, "Argument is not a tgz path: %s")
check_targz = check(is_targz, "Argument is not a tar.gz or tgz path: %s")
check_fs_path = check(is_fs_path, "Argument is not a path on the file system: %s")
check_dir=check(os.path.isdir, "Argument is not a directory on the file system: %s")
check_exists_path = check_fs_path
check_git_ws = check(is_git_ws, "Argument is not a git work space: %s")
