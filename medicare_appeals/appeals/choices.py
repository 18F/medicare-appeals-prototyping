APPEAL_CATEGORY = (
    ("03", "Acute Inpatient Hospital"),
    ("04", "Office-based Lab/X-ray"),
    ("05", "Nursing Home"),
    ("06", "Outpatient Therapies/CORF"),
    ("07", "Ground Transportation"),
    ("08", "Home Health"),
    ("11", "Hospice"),
    ("12", "Non-Medicare Benefit"),
    ("21", "Out of Area"),
    ("24", "Skilled Nursing Facility"),
    ("26", "Air Ambulance"),
    ("30", "Pathology/Laboratory"),
    ("31", "Imaging/Radiology"),
    ("32", "Drugs"),
    ("33", "Vision Services"),
    ("34", "Chiropractic"),
    ("35", "Dental"),
    ("39", "AC Dismissal"),
    ("41", "Outpatient Hospital/ASC"),
    ("42", "Acute Inpatient Rehab."),
    ("43", "Acute Inpatient Psych"),
    ("44", "Outpt Psych/Com Mental Hlth"),
    ("45", "Partial Psych Hosp"),
    ("46", "Intermediate Care"),
    ("47", "Long Term Care Hospital"),
    ("48", "Rurla Health Clinic/FQHC"),
    ("4-", "SRD Facility"),
    ("50", "Other"),
    ("51", "Medical/Surgical Supplies"),
    ("52", "Hosp Bed & Support Surfaces"),
    ("53", "Oxygen"),
    ("54", "Manual Wheelchairs"),
    ("55", "Miscellaneous DMEPOS"),
    ("56", "Orthoses"),
    ("57", "Drugs Miscellaneous"),
    ("58", "Enteral/Parenteral Nutri."),
    ("59", "Glucose Monitors"),
    ("60", "Office E/M Services"),
    ("61", "Hospital E/M Services"),
    ("62", "Facility E/M: SNF/Asst/Home"),
    ("65", "Integum/musc-skeletal Sur"),
    ("66", "Respiratory/Cardiovsclr Sur"),
    ("67", "Nervous System Surgery"),
    ("68", "Gastro./Urinary/Genital Sur"),
    ("69", "Other Surgery"),
    ("70", "Anesthesia"),
    ("71", "Podiatry"),
    ("72", "Radiation/Chemo/Infusion"),
    ("73", "Audiology"),
    ("74", "IDTF"),
    ("79", "Technical Denial"),
    ("80", "MSP"),
    ("81", "Copay/Deductible"),
    ("82", "Eligibility"),
    ("83", "Consolidated Billing"),
    ("84", "Infustion Pumps"),
    ("85", "Nebulizers & Drugs"),
    ("87", "Prostheses"),
    ("88", "Ostomy & Urological"),
    ("89", "Pos. Airway Pressure Device"),
    ("90", "Neg. Pressure Wound Therapy"),
    ("91", "Pneumatic compressor"),
    ("92", "Repairs"),
    ("93", "Respiratroy-Miscellaneous"),
    ("94", "Surgical Dressings"),
    ("95", "Therapeutic Shoes"),
)

APPEAL_STATUS = (("o", "Open"), ("c", "Closed"), ("p", "Promoted"),
                 ("r", "Reopened"))

APPEAL_STATUS_DEFAULT = "o"

APPEAL_WORKFLOW_TYPE = (
    ("d", "Dismissal"),
    ("g", "General"),
    ("mf", "Misfiled"),
    ("mr", "Misrouted"),
    ("nc", "No Count/Inquiry"),
)

APPEAL_WORKFLOW_TYPE_DEFAULT = "g"
