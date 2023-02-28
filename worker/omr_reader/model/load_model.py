from model.define_type_a_model import define_type_a_model
from model.define_type_b_model import define_type_b_model


def load_model(type_name):
    if type_name == "type_a":
        return define_type_a_model()
    if type_name == "type_b":
        return define_type_b_model()
    raise Exception("Model not found for type: " + type_name)
