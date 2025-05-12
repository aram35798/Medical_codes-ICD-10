translations = {
    "Essential hypertension": "I10",
    "Type 2 diabetes mellitus": "E11.9",
    "Acute bronchitis": "J20.9",
    "Low back pain": "M54.5",
    "Migraine without aura": "G43.0",
    "I10": "Essential hypertension",
    "E11.9": "Type 2 diabetes mellitus",
    "J20.9": "Acute bronchitis",
    "M54.5": "Low back pain",
    "G43.0": "Migraine without aura"
}


condition = input("Enter the medical condition or ICD code: ")

code = translations.get(condition)

if code:
    print(f"The ICD-10 code for '{condition}' is {code}.")
else:
    print(f"Sorry, ICD-10 code for '{condition}' not found.")