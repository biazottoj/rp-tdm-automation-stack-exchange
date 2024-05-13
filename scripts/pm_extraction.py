import extraction
import os


def pm_execute_extraction():
    data_files = {
        "posts": {"archive_path": "pm.stackexchange.com.7z", "xml_filename": "Posts.xml"},
        "comments": {"archive_path": "pm.stackexchange.com.7z", "xml_filename": "Comments.xml"},
        "posthistory": {"archive_path": "pm.stackexchange.com.7z", "xml_filename": "PostHistory.xml"}
    }
    os.makedirs(archives_dir := "../pmData/", exist_ok=True)
    os.makedirs(output_dir := "../pmOutput/", exist_ok=True)
    os.makedirs(tags_output_questions := output_dir + "tag_questions/", exist_ok=True)
    # os.makedirs(tags_output_answers := output_dir + "tag_answers/", exist_ok=True)
    os.makedirs(body_output_questions := output_dir + "body_questions/", exist_ok=True)
    # os.makedirs(body_output_answers := output_dir + "body_answers/", exist_ok=True)
    os.makedirs(title_output_questions := output_dir + "title_questions/", exist_ok=True)
    # os.makedirs(title_output_answers := output_dir + "title_answers/", exist_ok=True)

    # extraction.extraction_execute(archives_dir, data_files, tags_output_questions, tags_output_answers, 'Tags')
    # extraction.extraction_execute(archives_dir, data_files, body_output_questions, body_output_answers, 'Body')
    # extraction.extraction_execute(archives_dir, data_files, title_output_questions, title_output_answers, 'Title')

    extraction.remove_duplicates(body_output_questions, tags_output_questions)
    extraction.remove_duplicates(body_output_questions, title_output_questions)
    os.rename(body_output_questions, output_dir + "questions/")
