import os, re, zipfile
from tkinter import Tk
from tkinter import filedialog
from time import sleep


def rename(sub, vid):
	try:
		os.rename(f'{p}/{sub[0]}', p + '/' + re.findall(r'.*\.', vid[0])[0] + "srt")
	except:
		pass


def r(item):
	return (item, list(map(int,re.findall(r'\d{1,3}', re.findall(r'\d{1,3}\D\d{1,3}', item)[0]))))


extensions = '.webm .mpg .mp2 .mpeg .mpe .mpv .ogg .mp4 .m4p .m4v .avi .wmv .mov .qt .flv .swf'.split()

yes = ['y', 'Y', 'yes', 'Yes', 'YES']

def main():
	s = 1 if input("Are you trying to add subtitles to a series or a movie?[s/m]\n: ") in ['s', 'S', 'series', 'Series', 'SERIES'] else 0

	if input("Are the video files in this directory?[y/n]\n: ") in yes:
		p = os.getcwd()
	else:
		print("Please choose the directory contaning the video files.")
		sleep(1)
		root = Tk()
		root.withdraw()
		p = filedialog.askdirectory()
		root.destroy()

	directory = os.listdir(p)
	vids = []

	for item in directory:
		if any(item.endswith(ext) for ext in ['.rar', '.zip', '.7z']):
			file_name = f"{p}/{item}"
			with zipfile.ZipFile(file_name, 'r') as z:
				z.extractall(p)
			os.remove(file_name)
		elif any([item.endswith(ext) for ext in extensions]):
			vids.append(item)

	if s:
		subtitles = [r(item) for item in directory if item.endswith('.srt')]
		videos = [r(item) for item in vids]

		if subtitles and videos:
			print("Subtitles are added!")
		else:
			print("There are no video files in this directory!")
			if input("Do you want to try again?[y/n]\n: ") in yes:
				main()
			else:
				quit()

		[rename(sub, vid) for vid in videos for sub in subtitles if vid[1] == sub[1]]
	else:
		srt = [item for item in directory if item.endswith('.srt')]
		if len(srt) == 1 and len(vids) == 1:
			rename(srt, vids)
			print("Subtitles are added!")
		elif not srt or vids:
			print("There are no video files in this directory!")
			if input("Do you want to try again?[y/n]\n: ") in yes:
				main()
			else:
				quit()

if __name__ == '__main:__':
        main()
