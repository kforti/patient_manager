from patient_manager.manager import PatientManager


def test_manager():
    DATA_PATH = "/home/kevin/bin/patient_manager/datasets_737503_1278636_heart_modified.csv"

    pm = PatientManager(DATA_PATH)
    # print(patients)
    p = pm.find_patient('9f4c3308-babb-4c42-8790-6bdbb7248f99')
    assert vars(p) == {'age': 61.0,
                       'sex': 0.0,
                       'cp': 0.0,
                       'trestbps': 145.0,
                       'chol': 307.0,
                       'fbs': 0.0,
                       'restecg': 0.0,
                       'thalach': 146.0,
                       'exang': 1.0,
                       'oldpeak': 1.0,
                       'slope': 1.0,
                       'ca': 0.0,
                       'thal': 3.0,
                       'target': 0.0,
                       'id': '9f4c3308-babb-4c42-8790-6bdbb7248f99'}

