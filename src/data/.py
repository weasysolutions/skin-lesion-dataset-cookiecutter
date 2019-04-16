
   
    
    for 
    
    shutil.mktree()
    
    create_dir(os.path.join(absolute_path,rel_subs[0]))
    
    try:
        for dir_set in args:
            
    
    
    def __init__(self,*args):
        len(args)
        self.dir = base_dir
        self.sub_dirs = [os.path.join(self.dir, subdir_name) for subdir_name in subdir_names]
        
    def create_dir(self,directory):
 
    
    def make(self):
        self.create_dir(self.dir)
        for sub_dir in self.sub_dirs:
            self.create_dir(sub_dir)
            
    @classmethod         
    def mktree(cls,self,sub_sub_dirs):
        
        for sub,sub_sub in self.sub_dirs,sub_sub_dirs:
            cls.(sub,sub_sub).make
        
            
    def erase(self):
        try:
            shutil.rmtree(self.dir)
        except:
              
    