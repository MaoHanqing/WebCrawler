import requests
import os
def load_image_urls(files , type = ".json"):
	dic = {}
	for file in files:
		f = open(file)
		fileText = f.read()
	    images = fileText.split()
		image_list = images.split(",\n")
		fileName = file[:-len(type)]
		dic[fileName] = image_list
	return dic

def download_iamge(folder,url):
    if not os.path.exists(folder):
        os.makedirs(folder)

    if not examine_url(url):
    	return

    req = requests.get(url)

    if req.status_code == requests.codes.ok:
        name = url.split('/')[-1]
        f = open("./"+folder+'/'+name,'wb')
        f.write(req.content)
        f.close()
        print("image_download")
        return True
    else:
		print("image_download_false")
    	return False
    	
def examine_url(url):
	if url is "":
		return False
	return True

def load_files(path = None,type = ".json"):
	files = []
	if not path:
		path = os.getcwd()
	fileNames = os.listdir(path)
	for file in fileNames:
		if file.endswith(type):
			files.append(file)
	return files

files = load_files()
dic = load_image_urls(files) 
for key,value in dic.items():
	for url in value:
		download_iamge(key, url)	
		
	