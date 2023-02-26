import json
import shutil
import sys

from model.load_model import load_model
from process.pdf_to_images import pdf_to_images
from process.pre_process_image import pre_process_image
from process.read_marker import read_marker
from util.debug_log import debug_log


def process(src_path, type_name):
    temp_input_path = "temp/input"
    temp_preprocessed_path = "temp/preprocessed"

    shutil.rmtree(temp_input_path, ignore_errors=True)
    shutil.rmtree(temp_preprocessed_path, ignore_errors=True)

    model = load_model(type_name)

    result_list = {}

    image_files = pdf_to_images(src_path, temp_input_path)
    for (page_idx, file) in image_files:
        # for file in ["temp/input/image_0.png"]:
        preprocessed = pre_process_image(file, temp_preprocessed_path)
        page_result = read_marker(preprocessed, model)
        result_list[f"{page_idx}"] = page_result

    debug_log("done.")
    return result_list


if __name__ == '__main__':
    n = len(sys.argv)
    if n != 3:
        debug_log("Usage: python main.py <input_file_path> <type_name>")
        debug_log("Example: python main.py input/type_a.pdf type_a")
        exit(1)
    processed_result = process(sys.argv[1], sys.argv[2])

    print(json.dumps(processed_result))
