# 20.Hospital Management System Patient Registration (Dictionary), Appointment Scheduling (list), Medical Records Storage (file handling), Doctor information (Tuple), Billing System (Class & object), Report Generation (Python libraries)

# HOSPITAL MANAGEMENT SYSTEM

import csv
from datetime import datetime

patients = {}

def register_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    phone = input("Enter Phone Number: ")

    patients[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone
    }

    print("Patient registered successfully!\n")


appointments = []

def schedule_appointment():
    patient_id = input("Enter Patient ID: ")
    doctor_id = input("Enter Doctor ID: ")
    date = input("Enter Appointment Date (DD-MM-YYYY): ")
    time = input("Enter Appointment Time: ")

    appointment = [patient_id, doctor_id, date, time]
    appointments.append(appointment)

    print("Appointment scheduled successfully!\n")


def display_appointments():
    if not appointments:
        print("No appointments found.\n")
        return

    print("\n--- Appointment List ---")
    for appointment in appointments:
        print("Patient ID:", appointment[0])
        print("Doctor ID:", appointment[1])
        print("Date:", appointment[2])
        print("Time:", appointment[3])


def add_medical_record():
    patient_id = input("Enter Patient ID: ")
    diagnosis = input("Enter Diagnosis: ")
    treatment = input("Enter Treatment: ")
    medicines = input("Enter Medicines: ")

    with open("medical_records.txt", "a") as file:
        file.write(
            f"Patient ID: {patient_id}\n"
            f"Diagnosis: {diagnosis}\n"
            f"Treatment: {treatment}\n"
            f"Medicines: {medicines}\n"
            f"Date: {datetime.now().strftime('%d-%m-%Y')}\n"
            f"{'-'*40}\n"
        )



def view_medical_records():
    try:
        with open("medical_records.txt", "r") as file:
            records = file.read()

        print("\n--- Medical Records ---")
        print(records)

    except FileNotFoundError:
        print("No medical records found.\n")


doctors = (
    ("D101", "Dr. Amit Sharma", "Cardiologist"),
    ("D102", "Dr. Priya Singh", "Neurologist"),
    ("D103", "Dr. Rahul Das", "Orthopedic"),
    ("D104", "Dr. Sneha Roy", "General Physician")
)

def display_doctors():
    print("\n Doctor Information ")

    for doctor in doctors:
        print("Doctor ID :", doctor[0])
        print("Name      :", doctor[1])
        print("Specialty :", doctor[2])



class Billing:
    def __init__(self, patient_name, consultation, medicine, room_charge):
        self.patient_name = patient_name
        self.consultation = consultation
        self.medicine = medicine
        self.room_charge = room_charge

    def calculate_bill(self):
        return self.consultation + self.medicine + self.room_charge

    def display_bill(self):
        total = self.calculate_bill()

        print("\n--- Hospital Bill ---")
        print("Patient Name :", self.patient_name)
        print("Consultation :", self.consultation)
        print("Medicine     :", self.medicine)
        print("Room Charge  :", self.room_charge)
        print("---------------------")
        print("Total Bill   :", total)


def generate_bill():
    name = input("Enter Patient Name: ")
    consultation = float(input("Enter Consultation Charge: "))
    medicine = float(input("Enter Medicine Charge: "))
    room_charge = float(input("Enter Room Charge: "))

    # Object creation
    bill = Billing(name, consultation, medicine, room_charge)

    bill.display_bill()


def generate_report():
    print("\n--- Hospital Report ---")
    print("Total Patients     :", len(patients))
    print("Total Appointments :", len(appointments))
    print("Total Doctors      :", len(doctors))

    # Creating a CSV report
    with open("hospital_report.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Hospital Management Report"])
        writer.writerow(["Total Patients", len(patients)])
        writer.writerow(["Total Appointments", len(appointments)])
        writer.writerow(["Total Doctors", len(doctors)])

    print("Report generated successfully!")
    print("File: hospital_report.csv\n")


while True:
  
    print("     HOSPITAL MANAGEMENT SYSTEM")
    print("1. Register Patient")
    print("2. Schedule Appointment")
    print("3. View Appointments")
    print("4. Add Medical Record")
    print("5. View Medical Records")
    print("6. Doctor Information")
    print("7. Generate Bill")
    print("8. Generate Hospital Report")
    print("9. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        register_patient()

    elif choice == "2":
        schedule_appointment()

    elif choice == "3":
        display_appointments()

    elif choice == "4":
        add_medical_record()

    elif choice == "5":
        view_medical_records()

    elif choice == "6":
        display_doctors()

    elif choice == "7":
        generate_bill()

    elif choice == "8":
        generate_report()

    elif choice == "9":
        print("Thank you for using Hospital Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
