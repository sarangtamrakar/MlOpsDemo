import os

dirs = [
    'data/'+'raw',
    'data/'+'processed',
    'notebook',
    'saved_models',
    'src'
]

for dir in dirs:
    if not os.path.isdir(dir):
        os.makedirs(dir)
        with open(dir+'/'+'.gitkeep','w') as f:
            pass


files = ['dvc.yaml','params.yaml','.gitignore',os.path.join('src','__init__.py')]

for file in files:
    with open(file,'w') as p:
        pass

