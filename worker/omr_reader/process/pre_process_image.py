import os

import cv2
import numpy as np

from util.debug_log import debug_log


def _gray_threshold(hist):
    sum = 0
    for v in hist:
        sum += v

    sub_sum = 0
    for idx, v in enumerate(hist):
        sub_sum += v
        if sum / 10 < sub_sum:
            return max(0, idx - 1)
    return 254


def _marker_point(connected_components, left, top, width, height):
    biggest_area_size = 0
    result = (left, top, width, height)
    for component in connected_components:
        (x, y, w, h, area) = component
        if area < 8 * 8 or 50 * 50 < area:
            continue
        if x < left or left + width < x + w:
            continue
        if y < top or top + height < y + h:
            continue
        if area < w * h * 8 / 10:
            continue
        if biggest_area_size < area:
            biggest_area_size = area
            result = (x, y, w, h)
    return result


def pre_process_image(image_path, dst_path):
    os.makedirs(dst_path, exist_ok=True)

    image_name = os.path.basename(image_path)

    original_image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    gray_threshold = _gray_threshold(hist)
    (thresh, black_and_white_image) = cv2.threshold(gray_image, gray_threshold, 255, cv2.THRESH_BINARY)

    inverted_image = cv2.bitwise_not(black_and_white_image)
    cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(inverted_image)

    page_width = 1656
    page_height = 2338
    marker_left = 75
    marker_right = 100
    marker_top = 57
    marker_bottom = 50
    lt = _marker_point(stats, 0, 0, marker_left * 2, marker_top * 2)
    rt = _marker_point(stats, page_width - marker_right * 2, 0, marker_right * 2, marker_top * 2)
    lb = _marker_point(stats, 0, page_height - marker_bottom * 2, marker_left * 2, marker_bottom * 2)
    rb = _marker_point(stats, page_width - marker_right * 2, page_height - marker_bottom * 2, marker_right * 2,
                       marker_bottom * 2)

    if lt[2] * lt[3] + lb[2] * lb[3] < rt[2] * rt[3] + rb[2] * rb[3]:
        src_points = np.float32([
            [lt[0] + lt[2] / 2, lt[1] + lt[3] / 2],
            [rt[0] + rt[2] / 2, rt[1] + rt[3] / 2],
            [lb[0] + lb[2] / 2, lb[1] + lb[3] / 2],
            [rb[0] + rb[2] / 2, rb[1] + rb[3] / 2],
        ])
    else:
        src_points = np.float32([
            [rb[0] + rb[2] / 2, rb[1] + rb[3] / 2],
            [lb[0] + lb[2] / 2, lb[1] + lb[3] / 2],
            [rt[0] + rt[2] / 2, rt[1] + rt[3] / 2],
            [lt[0] + lt[2] / 2, lt[1] + lt[3] / 2],
        ])
    dst_points = np.float32([
        [marker_left, marker_top],
        [page_width - marker_left, marker_top],
        [marker_left, page_height - marker_bottom],
        [page_width - marker_left, page_height - marker_bottom]
    ])
    transform_mat = cv2.getPerspectiveTransform(src_points, dst_points)
    result_image = cv2.warpPerspective(black_and_white_image, transform_mat, (page_width, page_height))
    result_image = cv2.rotate(result_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    dst_image_path = dst_path + "/" + image_name
    debug_log(f"preprocessed file image_name = {dst_image_path}")
    cv2.imwrite(dst_image_path, result_image)
    return dst_image_path
