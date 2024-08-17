class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name
        self.health_records = []

    def add_record(self, record):
        self.health_records.append(record)

    def get_latest_record(self):
        return self.health_records[-1] if self.health_records else None

    def compare_with_latest(self, record):
        latest_record = self.get_latest_record()
        if not latest_record:
            return False  # No previous record to compare
        # Logic to compare current record with the latest record
        return any(abs(latest_record[k] - record[k]) > 5 for k in record)


class HealthMonitoringSystem:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    def get_patient(self, patient_id):
        return self.patients.get(patient_id, None)

    def input_patient_data(self, patient):
        record = {}
        while True:
            key = input("Enter the health parameter (or 'done' to finish): ").strip()
            if key.lower() == 'done':
                break
            try:
                value = float(input(f"Enter the value for {key}: "))
                record[key] = value
            except ValueError:
                print("Invalid input, please enter a numeric value.")

        if patient.compare_with_latest(record):
            print(f"New significant changes detected for {patient.name}. New diagnosis needed.")
        else:
            print(f"No significant changes detected for {patient.name}. No new diagnosis needed.")

        patient.add_record(record)


def main():
    system = HealthMonitoringSystem()

    while True:
        patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")

        patient = system.get_patient(patient_id)
        if not patient:
            patient = Patient(patient_id, name)
            system.add_patient(patient)

        system.input_patient_data(patient)

        if input("Enter 'q' to quit or any other key to continue: ").strip().lower() == 'q':
            break


if __name__ == "__main__":
    main()
