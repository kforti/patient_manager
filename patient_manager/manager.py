from patient_manager.models import Patient

import pandas as pd


def get_patient_attr(patient, attr, comp=None):
    if hasattr(patient, attr):
        return getattr(patient, attr)
    elif comp:
        return comp.compute(patient, attr)
    else:
        raise AttributeError


class PatientManager:
    def __init__(self, path, **kwargs):
        self.patients = PatientManager.get_df(path, **kwargs)

    @classmethod
    def get_df(cls, path, **kwargs):
        df = pd.read_csv(path, **kwargs)
        return df

    def find_patient(self, uid):
        pdf = self.patients.query(f'id == "{uid}"')
        pdict = pdf.to_dict('records')[0]
        patient = Patient(**pdict)
        return patient







