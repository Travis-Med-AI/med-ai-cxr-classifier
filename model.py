from tensorflow.keras.models import load_model


def get_model():
    model = load_model('MobileNet_chest_abd_msk_Xray_extra_dense09-0.02.h5')

    return model