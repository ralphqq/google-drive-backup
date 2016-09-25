import os
import shutil

import settings as st

def copyfile(s, d):
    """Does the actual copying from s to d."""
    cond1 = False
    cond2 = False
    
    if not os.path.exists(d):
        cond1 = True
    else:
        cond2 = os.stat(s).st_mtime - os.stat(d).st_mtime > 1
    
    if cond1 or cond2:
        shutil.copy2(s, d)

def copytree(src, dst, symlinks=False, ignore=None, mode='dir', skip=[]):
    """Copies contents of src directory to dst."""
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        
        if d not in skip:
            if mode == 'tree':
                
                if os.path.isdir(s):
                    copytree(s, d, symlinks, ignore, mode)
                else:
                    copyfile(s, d)
            elif mode == 'dir':
                copyfile(s, d)

def start():
    print 'Preparing...'
    
    for src, mode, skip in st.SRC:
        src_root = os.path.split(src)[1]
        dst_root = os.path.join(st.DST, src_root)
        if not os.path.exists(dst_root):
            os.makedirs(dst_root)
        
        if skip:
            skip = [os.path.join(dst_root, skp) for skp in skip]
        
        print 'Copying %s to %s' % (src, dst_root)
        copytree(src=src, dst=dst_root, mode=mode, skip=skip)
    
    print 'Finished.'

if __name__ == '__main__':
    if not st.SRC:
        print 'Please specify at least one directory to be backed up.'
    if not st.DST:
        print 'Please specify the full path to the destination directory.'
    else:
        start()
