from preprocess import preprocess
from evaluate import evaluate


def evaluate_model(files):
    preprocessed = preprocess(files)

    study_type = evaluate(preprocessed)

    return study_type

if __name__ == '__main__':
    paths = ['./example-dicom', './example-dicom']
    out= evaluate_model(paths)
    print(out)