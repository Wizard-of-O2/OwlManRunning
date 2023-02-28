from model.marker_model import MarkerModel


def _build_rects(start_x, start_y, width, height, count, step_x, step_y):
    result = []
    for i in range(count):
        result.append((start_x + i * step_x, start_y + i * step_y, width, height))
    return result


def define_type_a_model():
    result = [
        MarkerModel("centre_number_1", _build_rects(0.066, 0.427, 0.01, 0.02, 10, 0, 0.0295), is_required=True,
                    is_multiple=False),
        MarkerModel("centre_number_2", _build_rects(0.098, 0.427, 0.01, 0.02, 10, 0, 0.0295), is_required=True,
                    is_multiple=False),

        MarkerModel("student_number_1", _build_rects(0.179, 0.427, 0.01, 0.02, 10, 0, 0.0295), is_required=True,
                    is_multiple=False),
        MarkerModel("student_number_2", _build_rects(0.212, 0.427, 0.01, 0.02, 10, 0, 0.0295), is_required=True,
                    is_multiple=False),
        MarkerModel("student_number_3", _build_rects(0.244, 0.427, 0.01, 0.02, 10, 0, 0.0295), is_required=True,
                    is_multiple=False),
        MarkerModel("student_number_4", _build_rects(0.276, 0.427, 0.01, 0.02, 10, 0, 0.0295), is_required=True,
                    is_multiple=False),
    ]

    for i in range(0, 60):
        dx = (i // 20) * 0.101
        dy = (i % 20) * 0.03866
        result.append(
            MarkerModel("answer_0_" + str(i + 1), _build_rects(0.356 + dx, 0.140 + dy, 0.011, 0.02, 5, 0.0146, 0),
                        is_required=False, is_multiple=True))

    for i in range(0, 60):
        dx = (i // 20) * 0.101
        if i // 20 == 2:
            dx += 0.003
        dy = (i % 20) * 0.03866
        result.append(
            MarkerModel("answer_1_" + str(i + 1), _build_rects(0.676 + dx, 0.140 + dy, 0.011, 0.02, 5, 0.0146, 0),
                        is_required=False, is_multiple=True))

    return result
