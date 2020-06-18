from preprocess import preprocess
from evaluate import evaluate


def evaluate_model(file):
    preprocessed = preprocess(file)

    study_type = evaluate(preprocessed)

    return study_type

if __name__ == '__main__':
    out= evaluate_model('./example-dicom')
    print(out)