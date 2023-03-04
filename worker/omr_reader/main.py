import argparse
import json
import os
import shutil
import sys

from model.load_model import load_model
from process.make_result_image import make_result_image
from process.pdf_to_images import pdf_to_images
from process.pre_process_image import pre_process_image
from process.read_marker import read_marker
from util.debug_log import debug_log


def _read_answer_model(answer_path):
    with open(answer_path) as f:
        if not f:
            debug_log("Cannot open answer file.")
            return
        json_data = json.load(f)
    return json_data


def process(src_path, type_name, answer_path):
    temp_input_path = "temp/input"
    temp_preprocessed_path = "temp/preprocessed"

    src_directory = os.path.dirname(src_path)
    result_image_directory = f"{src_directory}/result"

    shutil.rmtree(temp_input_path, ignore_errors=True)
    shutil.rmtree(temp_preprocessed_path, ignore_errors=True)
    shutil.rmtree(result_image_directory, ignore_errors=True)

    os.makedirs(result_image_directory, exist_ok=True)

    model = load_model(type_name)
    answer_model = None
    if answer_path:
        answer_model = _read_answer_model(answer_path)

    result_list = {}

    image_files = pdf_to_images(src_path, temp_input_path)
    for (page_idx, file) in image_files:
        (rotated, preprocessed) = pre_process_image(file, temp_preprocessed_path)
        page_result = read_marker(preprocessed, model)

        if answer_model:
            result_image_path = make_result_image(rotated, model, answer_model, page_result, result_image_directory,
                                                  page_idx)
            page_result["result_image"] = result_image_path

        result_list[f"{page_idx}"] = page_result

    debug_log("done.")
    return result_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Input PDF file path and type')
    parser.add_argument('pdf_path', type=str, help='PDF file path')
    parser.add_argument('type', type=str, choices=['type_a', 'type_b'], help='type of file')
    parser.add_argument('-a', '--answer', type=str, help='answer file path')

    args = parser.parse_args()

    if not (args.pdf_path and args.type):
        debug_log('Error: required arguments missing')
        debug_log("Example: python main.py input/type_a.pdf type_a")
        parser.print_usage()
        sys.exit(1)

    debug_log('PDF file path:' + args.pdf_path)
    debug_log('File type:' + args.type)

    answer_path = None
    if args.answer:
        answer_path = args.answer

    processed_result = process(args.pdf_path, args.type, answer_path)

    print(json.dumps(processed_result))
