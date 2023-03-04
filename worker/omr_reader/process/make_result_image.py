import cv2


def make_result_image(src_image_path, marker_info_list, answer_model, page_result, dst_directory, index):
    dst_path = f"{dst_directory}/result_{index + 1}.png"

    image = cv2.imread(src_image_path)
    image_width = image.shape[1]
    image_height = image.shape[0]

    overlay = image.copy()

    for answer_key in answer_model:
        for model in marker_info_list:
            if model.name == answer_key:
                for answer in answer_model[answer_key]:
                    _draw_check_mark(overlay, image_width, image_height, model, answer, 0, (0, 0, 255))

    for marker_key in page_result:
        for model in marker_info_list:
            if model.name == marker_key:
                for answer in page_result[marker_key]:
                    _draw_check_mark(overlay, image_width, image_height, model, answer, -10, (0, 255, 0))
                    break
    alpha = 0.4
    result = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
    cv2.imwrite(dst_path, result)

    return dst_path


def _draw_check_mark(overlay, image_width, image_height, model, index, y_offset, color):
    if 0 > index or index >= len(model.rects):
        return
    rect = model.rects[index]
    checkmark_dx = 10
    checkmark_dy = 20
    center_x = int(image_width * (rect[0] + rect[2] / 2))
    bottom_y = int(image_height * (rect[1] + rect[3] * 2 / 3)) + y_offset
    cv2.line(overlay, (center_x - checkmark_dx, bottom_y - checkmark_dy), (center_x, bottom_y), color, thickness=3)
    cv2.line(overlay, (center_x, bottom_y), (center_x + checkmark_dx, bottom_y - checkmark_dy), color, thickness=3)
