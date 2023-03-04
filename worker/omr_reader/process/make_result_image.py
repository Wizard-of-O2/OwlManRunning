import json

import cv2


def make_result_image(src_image_path, marker_info_list, answer_path, dst_directory, index):
    with open(answer_path) as f:
        json_data = json.load(f)
    if not json_data:
        return
    dst_path = f"{dst_directory}/result_{index}.png"

    image = cv2.imread(src_image_path)
    image_width = image.shape[1]
    image_height = image.shape[0]

    overlay = image.copy()

    for answer_key in json_data:
        for model in marker_info_list:
            if model.name == answer_key:
                for answer in json_data[answer_key]:
                    if 0 > answer or answer >= len(model.rects):
                        continue
                    rect = model.rects[answer]

                    checkmark_dx = 10
                    checkmark_dy = 20

                    center_x = int(image_width * (rect[0] + rect[2] / 2))
                    bottom_y = int(image_height * (rect[1] + rect[3] * 2 / 3))

                    cv2.line(overlay, (center_x - checkmark_dx, bottom_y - checkmark_dy), (center_x, bottom_y),
                             (0, 0, 255), thickness=3)
                    cv2.line(overlay, (center_x, bottom_y), (center_x + checkmark_dx, bottom_y - checkmark_dy),
                             (0, 0, 255), thickness=3)

                    break

    alpha = 0.4
    result = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
    cv2.imwrite(dst_path, result)

    return dst_path
