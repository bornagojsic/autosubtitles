import os, re, zipfile

p = os.getcwd()
vids = []

for item in os.listdir(p):
	if item.endswith('.zip'):
		file_name = os.path.abspath(item)
		with zipfile.ZipFile(file_name, 'r') as z:
			z.extractall(p)
		os.remove(file_name)
	elif not (item.endswith('.py') or item.endswith('.srt')):
		vids.append(item)

subtitles = [(item, list(map(int, re.findall(r'\d{1,3}', re.findall(r'\d{1,3}\D\d{1,3}', item)[0])))) for item in os.listdir(p) if item.endswith('.srt')]

videos = [(item, list(map(int, re.findall(r'\d{1,3}', re.findall(r'\d{1,3}\D\d{1,3}', item)[0])))) for item in vids]

for vid in videos:
	for sub in subtitles:
		if vid[1] == sub[1]:
			try:
				os.rename(f'{p}\\{sub[0]}', re.findall(r'.*\.', vid[0])[0] + "srt")
			except:
				pass
