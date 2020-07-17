


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