import os
from os import walk

from pdf2image import convert_from_path

from util.debug_log import debug_log


def pdf_to_images(src_path, dst_path):
    os.makedirs(dst_path, exist_ok=True)

    result = []
    for (dir_path, _, filenames) in walk(dst_path):
        for filename in filenames:
            image_path = dir_path + "/" + filename
            if os.path.isfile(image_path):
                os.remove(image_path)

    image_idx = 0
    images = convert_from_path(src_path)
    page_idx = 0
    for image in images:
        result_file_name = f"image_{image_idx + 1}.png"

        image = image.resize((1656, 2338))
        result_path = dst_path + "/" + result_file_name
        image.save(result_path, "png")
        result.append((page_idx, result_path))
        debug_log(f"copy {page_idx} page -> {result_file_name}")

        image_idx = image_idx + 1
        page_idx = page_idx + 1

    return result
