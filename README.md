Create Env
```
conda create -n MLOps python=3.7 -y
```



Activate env 
``` conda activate MLOps```




Create requirements.txt
```touch requirements.txt
write ===> dvc,
           dvc[drive]
```




Install the requirements
```pip install -r requirements.txt```



Download the data set (winQuality) from kaggle


NOTE==> always do git init before dvc init
beacuse it dvc build upon git

Commands
```
git init
```
```
dvc init
```
```
dvc add data_given/winequality.csv
```
```
git add .
```
```
git commit -m "initial commit"
```
```
git remote add origin https://github.com/sarangtamrakar/simple-dvc-demo.git
```
```
git branch -M main
```
```
git push -u origin main
```
