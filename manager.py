

DATA_PATH = "/home/kevin/PycharmProjects/heart_patient_manager/datasets_737503_1278636_heart_modified.csv"


class Patient:
    def __init__(self,
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal,
        target,
        id):
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trestbps = trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal
        self.target = target
        self.id = id


def get_patient_data(path):
    patients = {}
    with open(path, 'r') as file:
        for i, row in enumerate(file):
            if i == 0:
                continue

            row = row.strip()
            row = row.split(',')
            patient_data = [float(num) for num in row[:-1]]
            patient_data.append(row[-1])
            patient = Patient(*patient_data)
            patients[patient.id] = patient

    return patients


def find_patient(patients, uid):
    return patients[uid]


def get_patient_attr(patient, attr, comp=None):
    if hasattr(patient, attr):
        return getattr(patient, attr)
    elif comp:
        return comp.compute(patient, attr)
    else:
        raise AttributeError


class BaseCompute:
    def compute(self, patient, attr):
        fn = getattr(self, attr)
        result = fn(patient)
        return result


class PatientsCompute(BaseCompute):
    def __init__(self, patients):
        self.patients = patients

    def chol_percentile(self, patient):
        return "80th"


patients = get_patient_data(DATA_PATH)
#print(patients)
p = find_patient(patients, '9f4c3308-babb-4c42-8790-6bdbb7248f99')
comp = PatientsCompute(patients)
percentile = get_patient_attr(p, "chol_percentile", comp)
print(p)
print(percentile)