import os
#os module is a part of standard built in library module, so we don't need to install third party module

#print(dir(os))
#output of above print statement ['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']

print(os.getcwd())
##ouput is C:\Users\hamsals\Desktop\pythonlearning


os.chdir("C:\\Users\\hamsals\\Desktop")

print(os.getcwd())
#C:\Users\hamsals\Desktop

#if we won't give argument to the list dir , it display all the folders and files in the current directory
#current directory here is desktop
#print(os.listdir())
['.git', 'app.pdf', 'app1.pdf', 'app2.pdf', 'Application For Employment.pdf', 'Atom.lnk', 'backside.pdf', 'brg-my-seat-2017-01-23220511.551.pdf', 'Build flow.pptx', 'build_presentation.pptx', 'bv commnad history', 'Confirmation Appraisal Form 2018.xls', 'Copy of Confirmation Appraisal Form 2018_1.xls', 'Copy of Samsung8LPP_val_checklist.xlsx', 'databookchk.xlsx', 'desktop.ini', 'dlatch.docx', 'doc.pdf', 'Expert_python_programming.pdf', 'f.pdf', 'front.pdf', 'Gratuity forms.pdf', 'hamsa', 'hamsa_build_presentation.pptx', 'image001.jpg', 'Julyplan.xlsx', 'Karapetyan_1_presentation.pdf', 'lped1034_ts28nphllogl30hdl140f.pdf', 'lped1038_ts28nphhlogl35hdl140f.pdf', 'lped1040_ts28nphhlogl40hdl140f.pdf', 'lped1042_ts28nphllogl40hdl140f.pdf', 'lvf-characterization-in-siliconsmart.pdf', 'Mediassist Appln Form (9).xls', 'New Microsoft Excel Worksheet.xlsx', 'New PF Form 2 .pdf', 'photo.jpg', 'plan.pdf', 'pythonlearning', 'quiz', 'Release of UMC14FFC 7.5T .pdf', 'release_notes', 'samsung', 'sf.pdf', 'snps_area_check.docx', 'SYNOPSYS Emp Verifact Form.pdf', 'task.pdf', 'team.pdf', 'test.docx', 'ti_diff_liberty.xlsx', 'transport application form.pdf', 'ts22drc_lvs_ant.xlsx', 'ts22xlsheet.xlsx', 'view_ckecks.xlsx', '~$doc.pdf', '~$f-characterization-in-siliconsmart.pdf', '~$lease of UMC14FFC 7.5T .pdf', '~$l_book.pdf', '~$pert_python_programming.pdf', '~$ps_area_check.docx', '~$test.docx']

##to create a directory we have to keywords mkdir, makedirs
#mkdir to create only one directory
#makedirs is to create the directory tree
os.chdir("C:\\Users\\hamsals\\Desktop\pythonlearning")
#os.mkdir("os_demo")
print(os.listdir())
#output is ['.git', 'all_in_one_lef', 'conditionals&booleans.py', 'dictionaries.py', 'functions.py', 'git commands', 'import_module_exploring_std_lib.py', 'import_module_main.py', 'input_import_module_exploring_std.py', 'int&float.py', 'list_tuples_sets.py', 'loops&iterators.py', 'mainfunction.py', 'os', 'os_demo', 'prac', 'prac.py', 'practise.py', 'python1.py', 'strings.py', 'symmetric_or', 'underlying_os_functionality.py', '__pycache__']
#os.makedirs("os_demo\sub_dir")
print(os.listdir("os_demo"))
#output after the above print statement is ['sub_dir']


#similar to create directory we have functions for the deleting derctories
#rmdir(), will  remove only top level directory
#removedires(), will remove subdirectories also
#os.rmdir("os_demo")
#os.removedirs("os_demo\sub_dir")
#os.rename('prac.py','rough.py')
#print(os.listdir())
#['.git', 'all_in_one_lef', 'conditionals&booleans.py', 'dictionaries.py', 'functions.py', 'git commands',
#'import_module_exploring_std_lib.py', 'import_module_main.py', 'input_import_module_exploring_std.py',
#'int&float.py', 'list_tuples_sets.py', 'loops&iterators.py', 'mainfunction.py', 'os', 'os_demo', 'prac.py',
# 'practise.py', 'python1.py', 'rough', 'strings.py', 'symmetric_or', 'underlying_os_functionality.py', '__pycache__']


##to know the details of the file
print(os.stat("rough.py"))
#os.stat_result(st_mode=33206, st_ino=4503599627546341, st_dev=1313269400,
#st_nlink=1, st_uid=0, st_gid=0, st_size=123, st_atime=1537253232, st_mtime=1537253306, st_ctime=1537253232)
#mtime means last modified time, size means size in bytes


#to know details of the only particular function. size
print(os.stat("rough.py").st_size)
#output is 123 byt

#to know details of the only particular function, last modified time
print(os.stat("rough.py").st_mtime)
#output is 1537253306.0048325


#to get the last modified time(time stamp) in the human readable format,
from datetime import datetime
mod_time=os.stat("rough.py").st_mtime
print(datetime.fromtimestamp(mod_time))
#output is 2018-09-18 12:18:26.004833


#os .walk methos is extremely useful, if we have file some where in the desktop, we forgot where it is
#then this os.walk method traverses till the end of the directory tree and finds it
#os.walk() method walks through  directories tree from to down , untill the end of directory structure
#it returns tuple of 3 values, first one is path of the directory,
#second one is directory names
#third one is filenames inside the directory
for dirpath,dirnames,filenames in os.walk("C:\\Users\\hamsals\\Desktop\pythonlearning\\os_demo"):
    print('current path',dirpath)
    print('dir names',dirnames)
    print('file names',filenames)
#current path C:\Users\hamsals\Desktop\pythonlearning\os_demo
#dir names ['sub_dir', 'sub_dir22']
#file names ['prd', 'rty', 'sub_dir2']
#current path C:\Users\hamsals\Desktop\pythonlearning\os_demo\sub_dir
#dir names []
#file names ['parc', 'prac2']
#current path C:\Users\hamsals\Desktop\pythonlearning\os_demo\sub_dir22
#dir names []
#file names []

#now lets talk about the environmental variables
#we have so many environmental variables
print(os.environ.get('HOME'))
#output is C:\Users\hamsals


#what if we want to combine the temp.txt file with the above home directory path
# some people will use concatination
#this is guess work , because sometimes backslashes comes at end, if we keep one back slash then it will become double slash
file_path=os.environ.get('HOME')+'temp.txt'
print(file_path)
#output is C:\Users\hamsalstemp.txt



#using the above method we will miss the slashes
#to avoid the guess work we go for os.path.join method
#for that we have one inbuild functtion in the osmodule
#os.path module has lot of functionalities to work with paths
#the one that we are going to use here is os.path.join method
file_path=os.path.join(os.environ.get('HOME'),'temp.txt')
print(file_path)
#C:\Users\hamsals\temp.txt


#basename,dirname,split
#basename gives the lastname
print(os.path.basename('/tmp/tem.txt'))
#output is tem.txt

print(os.path.basename(file_path))
#output here is temp.txt

print(os.path.dirname(file_path))
#output is C:\Users\hamsals

print(os.path.dirname('/tmp/tem.txt'))
#output is /tmp

print(os.path.split('/tmp/tem.txt'))
#output is ('/tmp', 'tem.txt')

print(os.path.split(file_path))
#output is ('C:\\Users\\hamsals', 'temp.txt')


##one more example for the os.path.basename,dirname,split
print(os.path.dirname("C:\\Users\\hamsals\\Desktop\pythonlearning\\os_demo"))
#output is C:\Users\hamsals\Desktop\pythonlearning

print(os.path.basename("C:\\Users\\hamsals\\Desktop\pythonlearning\\os_demo"))
#output is os_demo

print(os.path.split("C:\\Users\\hamsals\\Desktop\pythonlearning\\os_demo"))
#output is ('C:\\Users\\hamsals\\Desktop\\pythonlearning', 'os_demo')




##splitext will seperate the file root and the extension
print(os.path.splitext('/tmp/tem.txt'))
('/tmp/tem', '.txt')
print(os.path.splitext('/tmp/tem.py'))
('/tmp/tem', '.py')




#last most common useful thing is exsist, isdir,isfile
#exists will returns fasle if the file is not present in the file system
print(os.path.exists('/tmp/tem.txt'))
#outpu is False, since /tmp/te.txt does not exists in our file system
print(os.path.exists("C:\\Users\\hamsals\\Desktop\pythonlearning\\os_demo"))
#output is True



print(os.path.isdir('/tmp/tem.txt'))
#outpu is False, since /tmp/te.txt does not exists in our file system
print(os.path.isdir("C:\\Users\\hamsals\\Desktop\pythonlearning\\os_demo"))
#output is True



print(os.path.isfile('/tmp/tem.txt'))
#outpu is False, since /tmp/te.txt does not exists in our file system
print(os.path.isfile("C:\\Users\\hamsals\\Desktop\pythonlearning\\os_demo\\sub_dir\prac2"))
#output is True
print(os.path.isfile("C:\\Users\\hamsals\\Desktop\pythonlearning\\os_demo"))
#output is False
