from dataclasses import dataclass
import datetime
import subprocess
import sys

import pandas as pd

video_embed_template = '''
<iframe id="ytplayer" type="text/html" width="640" height="360"
	src="https://www.youtube.com/embed/{}?autoplay=0&modestbranding=1"
frameborder="0">
</iframe>
'''

@dataclass
class Video:
	video_id: str
	upload_date: str


@dataclass
class Project:
	title: str
	short_description: str
	video_string: str
	presentation_url: str

	def __post_init__(self):
		self.videos = list(extract_videos_from_urls(self.video_string))
		# Use the first video upload date as a proxy for the date of project
		self.date = self.videos[0].upload_date.strftime('%b, %Y')

	def create_formatted_string(self):
		video_string = "\n".join([video_embed_template.format(vid.video_id) for vid in self.videos])

		string = f'''
### {self.title}

> {self.short_description}

{self.date} \\| <a href="{self.presentation_url}" target="_blank">Presentation</a> 

{video_string}
'''
		return string


def convert_row_to_project(row):
	return Project(
		row['Name'],
		row['Short description'],
		row['Demo links'],
		row['Presentation link'])


def extract_videos_from_urls(string):
	urls = string.split(",")
	for url in urls:
		video_id = url.split('v=')[-1]
		yield Video(
			video_id, get_upload_date_of_video(video_id)
			)


def get_upload_date_of_video(vid_identifier):
    out = subprocess.Popen(['youtube-dl', '--get-filename', '-o', "%(upload_date)s", vid_identifier],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    if stderr:
        raise Exception(stderr)
    return datetime.datetime.strptime(stdout.strip().decode(), '%Y%m%d')


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Filename missing")
		sys.exit(1)

	fname = sys.argv[1]
	df = pd.read_csv(fname)

	projects = []

	for idx, row in df.iterrows():
		projects.append(convert_row_to_project(row))

	print("---\n".join([project.create_formatted_string() for project in projects]))

