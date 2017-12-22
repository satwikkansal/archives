import os
import re
from datetime import datetime


start_date = "2017-04-04"
start_time = "00:00:00"
end_date = "2017-08-23"
end_time = start_time

title_regex = r'title: (.*)\n'
date_regex = r'date: (201\d-[0-1]\d-[0-3]\d).*([0-2]\d:[0-6]\d:[0-6]\d).*\n'

directory = os.path.join(os.getcwd(), "_posts/")


def convert_to_time_obj(date_string, time_string):
    # format yyyy-mm-dd and hh:mm:ss
    date_obj = datetime.strptime(date_string + time_string, "%Y-%m-%d%H:%M:%S")
    return date_obj


def parse_file(content):
    res = {}
    res['name'] = re.findall(title_regex, content)[0]
    res['anchor'] = '-'.join(res['name'].split())
    d, t = None, None

    dates = re.findall(date_regex, content)

    d = dates[0][0]
    t = dates[0][1]
    res['time'] = convert_to_time_obj(d, t)
    res['format_date'] = res["time"].strftime("%d %b %Y, %a")

    res['content'] = '\n'.join(content.split('---')[2:])

    return res


files = os.listdir(directory)

parsed_map = {}

for fname in files:
    with open(os.path.join(directory,fname), 'r') as f:
        content = f.read()
        parsed_obj = parse_file(content)
        parsed_map[fname] = parsed_obj

start_date = convert_to_time_obj(start_date, start_time)
end_date = convert_to_time_obj(end_date, end_time)

print(type(parsed_map))

parsed_map = sorted(parsed_map.items(), key=lambda x: x[1]['time'])

final_post = ""
single_template = """
---
## {name} <a name="{anchor}"></a>
**Published on:** {date}

{content}
---
"""

toc = []


for fname, parsed_obj in parsed_map:
    if parsed_obj["time"]>start_date and parsed_obj["time"]<=end_date:
        final_post += single_template.format(name=parsed_obj["name"],
                                             anchor=parsed_obj["anchor"],
                                             date=parsed_obj["format_date"],
                                             content=parsed_obj["content"])
        toc.append((parsed_obj["name"], parsed_obj['anchor']))

table_of_contents = ''
for post, anchor in toc:
    table_of_contents += "- [{title}](#{hyphen_sep})\n".format(title=post,
                                                               hyphen_sep=anchor)

print(table_of_contents)

final_post = table_of_contents+final_post

with open("output.md", 'w') as f:
    f.write(final_post)
