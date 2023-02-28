from model.marker_model import MarkerModel


def _build_rects(start_x, start_y, width, height, count, step_x, step_y):
    result = []
    for i in range(count):
        result.append((start_x + i * step_x, start_y + i * step_y, width, height))
    return result


def define_type_b_model():
    result = []

    for x in range(12):
        dx = x * 0.0168
        dy = 0
        result.append(
            MarkerModel("given_name_" + str(x + 1), _build_rects(0.045 + dx, 0.255 + dy, 0.011, 0.02, 27, 0, 0.0249),
                        is_required=False, is_multiple=False))

    for x in range(12):
        dx = x * 0.0168
        dy = 0
        result.append(
            MarkerModel("surname_" + str(x + 1), _build_rects(0.264 + dx, 0.255 + dy, 0.011, 0.02, 27, 0, 0.0249),
                        is_required=False, is_multiple=False))

    for i in range(0, 30):
        dx = (i // 15) * 0.076
        dy = (i % 15) * 0.03866
        result.append(
            MarkerModel("answer_0_" + str(i + 1), _build_rects(0.496 + dx, 0.235 + dy, 0.011, 0.02, 4, 0.0146, 0),
                        is_required=False, is_multiple=True))

    for i in range(0, 30):
        dx = (i // 15) * 0.076
        dy = (i % 15) * 0.03866
        result.append(
            MarkerModel("answer_1_" + str(i + 1), _build_rects(0.660 + dx, 0.235 + dy, 0.011, 0.02, 4, 0.0146, 0),
                        is_required=False, is_multiple=True))

    for i in range(0, 30):
        dx = (i // 15) * 0.076
        dy = (i % 15) * 0.03866
        result.append(
            MarkerModel("answer_2_" + str(i + 1), _build_rects(0.824 + dx, 0.235 + dy, 0.011, 0.02, 4, 0.0146, 0),
                        is_required=False, is_multiple=True))

    return result
