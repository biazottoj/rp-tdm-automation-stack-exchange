import helper
import shutil
import os


def remove_duplicates(dest_dir, src_dir):
    allfiles = os.listdir(src_dir)
    for f in allfiles:
        if not os.path.exists(os.path.join(dest_dir, f)):
            src_path = os.path.join(src_dir, f)
            dest_path = os.path.join(dest_dir, f)
            shutil.move(src_path, dest_path)

    shutil.rmtree(src_dir)


def extract_posts(archives_dir, archives_dict, output_dir, filters):
    archive_path = archives_dir + archives_dict["posts"]["archive_path"]
    xml_filename = archives_dict["posts"]["xml_filename"]

    for p in helper.extract_posts(archive_path, xml_filename, filters):
        print(p["Id"])
        helper.export_json(p, f'{output_dir}post-{p["Id"]}.json')


def update_posts(archives_dir, archives_dict, dict_key, posts_dir, section):
    archive_path = archives_dir + archives_dict[dict_key]["archive_path"]
    xml_filename = archives_dict[dict_key]["xml_filename"]

    helper.update_posts(archive_path, xml_filename, posts_dir, section)


def execute(archives_dir, archives_dict, output_dir, filters):
    extract_posts(archives_dir, archives_dict, output_dir, filters)
    update_posts(archives_dir, archives_dict, "comments", output_dir, "comments")
    update_posts(archives_dir, archives_dict, "posthistory", output_dir, "history")


def extraction_execute(archives_dir, data_files, output_questions, output_answers, flag):

    if flag == 'Tags':
        search = 'technical-debt'
        back_up = 'tech-debt'
    else:
        search = 'technical debt'
        back_up = 'tech debt'

    question_filters = [
        ('PostTypeId', lambda x: x == '1'),
        (flag, lambda x: search in x.lower()),
    ]
    execute(archives_dir, data_files, output_questions, question_filters)

    question_ids = set(helper.get_post_ids(output_questions))
    answer_filters = [
        ('PostTypeId', lambda x: x == '2'),
        ('ParentId', lambda x: x in question_ids),
    ]
    execute(archives_dir, data_files, output_answers, answer_filters)

    helper.add_answers_to_question(output_questions, output_answers)
    try:
        shutil.rmtree(output_answers)
    except FileNotFoundError:
        pass
