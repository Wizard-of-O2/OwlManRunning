import cv2

from util.debug_log import debug_log

DEBUG = False
SINGLE_MIN_RATIO = 0.25
MULTIPLE_MIN_RATIO = 0.4


def read_marker(image_path, marker_info_list):
    result = {}

    image = cv2.imread(image_path)
    image_width = image.shape[1]
    image_height = image.shape[0]

    is_valid = True
    for marker_info in marker_info_list:
        ratios = []
        for rect in marker_info.rects:
            x = int(image_width * rect[0])
            y = int(image_height * rect[1])
            w = int(image_width * rect[2])
            h = int(image_height * rect[3])

            total_pixel_count = w * h
            black_pixel_count = 0
            for dy in range(h):
                for dx in range(w):
                    if image[y + dy, x + dx][0] < 128:
                        black_pixel_count += 1
            ratio = black_pixel_count / total_pixel_count
            ratios.append(ratio)

        answer_count = sum(ratio >= MULTIPLE_MIN_RATIO for ratio in ratios)
        if marker_info.is_multiple and 2 <= answer_count:
            marker_result = [i for i, ratio in enumerate(ratios) if ratio >= MULTIPLE_MIN_RATIO]
        else:
            max_ratio_index = max(range(len(ratios)), key=ratios.__getitem__)
            if ratios[max_ratio_index] >= SINGLE_MIN_RATIO:
                marker_result = [max_ratio_index]
            else:
                marker_result = []
        result[marker_info.name] = marker_result
        if marker_info.is_required and 0 == len(marker_result):
            is_valid = False
    result["is_valid"] = is_valid

    if DEBUG:
        debug_log(result)
        for marker_info in marker_info_list:
            for rect in marker_info.rects:
                x = int(image_width * rect[0])
                y = int(image_height * rect[1])
                w = int(image_width * rect[2])
                h = int(image_height * rect[3])
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow("image", image)
        cv2.waitKey(0)

    return result
