import os
import json
import subprocess
import re
from lxml import etree

CHUNK_SIZE = 128 * 1024 * 1024


def export_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def extract_posts(archive_path, xml_filename, filters):
    command = [r'C:\Program Files\7-Zip\7z.exe', 'e', archive_path, xml_filename, '-so']
    with subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=CHUNK_SIZE) as process:
        context = etree.iterparse(process.stdout, events=('start', 'end'))
        for event, elem in context:
            if event == 'end' and elem.tag == 'row':
                x = all(f[1](elem.attrib.get(f[0], '')) for f in filters)
                if x:
                    yield dict(elem.attrib)
                elem.clear()


def get_post_ids(folder_path):
    pattern = r'post-(\d+)\.json'
    for filename in os.listdir(folder_path):
        match = re.match(pattern, filename)
        if match:
            yield match.group(1)


def extract_posts_section(archive_path, xml_filename, post_ids):
    command = [r'C:\Program Files\7-Zip\7z.exe', 'e', archive_path, xml_filename, '-so']

    with subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=CHUNK_SIZE) as process:
        context = etree.iterparse(process.stdout, events=('start', 'end'))
        for event, elem in context:
            if event == 'end' and elem.tag == 'row':
                pid = elem.attrib.get('PostId', '')
                if pid in post_ids:
                    yield pid, dict(elem.attrib)
                elem.clear()


def update_posts(archive_path, xml_filename, posts_dir, section):
    post_ids = set(get_post_ids(posts_dir))
    for pid, comment in extract_posts_section(archive_path, xml_filename, post_ids):
        post_filename = os.path.join(posts_dir, f'post-{pid}.json')
        with open(post_filename) as f:
            post = json.load(f)
        if section not in post:
            post[section] = []
        post[section].append(comment)
        print(f"Updating {section} in post {pid}")
        export_json(post, post_filename)


def add_answers_to_question(questions_dir, answers_dir):
    answers_ids = set(get_post_ids(answers_dir))
    for aid in answers_ids:
        answer_filename = os.path.join(answers_dir, f'post-{aid}.json')
        with open(answer_filename) as f:
            answer = json.load(f)
        qid = answer['ParentId']
        question_filename = os.path.join(questions_dir, f'post-{qid}.json')
        with open(question_filename) as f:
            question = json.load(f)

        if 'answers' not in question:
            question['answers'] = []
        question['answers'].append(answer)
        print(f"Adding answers to question {qid}")
        export_json(question, question_filename)
