
# coding: utf-8

# In[84]:

# WORKING WITH ZIP FILES

get_ipython().system('jupyter nbconvert --to script config_template.ipynb')


# In[77]:

# Package

import zipfile
import os


# In[78]:

# Point Jupyter Notebook to the correct dir

Dir = r'C:\Users\Chris.Cirelli\Desktop\Python Programming Docs\Learn Python\ZipFiles'
os.chdir(Dir)


# In[79]:

# Create a ZipFile

def create_zipFile(zip_name, target_dir):
    '''The purpose of this function is to create a zipfile
    a.) inputs: a string of the name of the zip file to be created and the directory where the files are located
    b.) create zipFile name
    c.) Wih the zip file open, write to the zipfile. 
    d.) Print the dir_list to confirm the zip file was create
    e.) Return none as the file was created on the shared drive.'''
    
    from zipfile import ZipFile
    zip_name = str(zip_name) + '.zip'
    target_dir = os.chdir(target_dir)
    File_list = os.listdir()
    
    with ZipFile (zip_name, 'w') as zip:
        for file in File_list:
            if '.txt' in file:
                zip.write(file)
            
    return None
      
   


# In[80]:

create_zipFile('shitballs', Dir)


# In[35]:

# Inspect Zip File


# In[81]:

Dir_list = [print(x) for x in os.listdir()]


# In[82]:

def inspect_zipFile(filename):
    from zipfile import ZipFile
         
    with ZipFile (filename) as zip:
        zip.printdir()
    
    return None


# In[83]:

inspect_zipFile('shitballs.zip')


# In[52]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



