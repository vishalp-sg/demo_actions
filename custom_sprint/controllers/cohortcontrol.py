import json
from datetime import datetime
from odoo import http

class CohortController(http.Controller):

    @http.route('/create_new_cohort', website=True, auth='public')
    def create_new_cohort(self):

        cohort_data = {
            "success": True,
            "data": [
                {
                    "batchId": "IISC-AC-DHAI-09",
                    "primarySKUs": [
                        "IISC-AC-DHAI"
                    ],
                    "secondarySKUs": [],
                    "applicationFeeSKUs": [
                        "IISC-AFRI-DHAI",
                        "IISC-AFTS-DHAI",
                        "IISC-AFUS-DHAI"
                    ],
                    "salesFrom": "2024-04-16",
                    "salesTo": "2024-08-07",
                    "deliveryStarts": "2024-08-07",
                    "deliveryEnds": "2025-03-12",
                    "platformValidity": "2025-10-15",
                    "calendarId": "",
                    "category": "ops_batch"
                }
            ]
        }

        cohort_model = http.request.env['cohorts.cohorts']
        for record in cohort_data.get('data', []):
            data = {
                "batchId": record['batchId'],
                "primary_sku_ids": [
                    [0, 0, {"name": sku}]
                    for sku in record["primarySKUs"]
                ],
                "secondary_sku_ids": [
                    [0, 0, {"name": sku}]
                    for sku in record["secondarySKUs"]
                ],
                "fees_sku_ids": [
                    [0, 0, {"name": sku}]
                    for sku in record["applicationFeeSKUs"]
                ],
                "salesFrom": record['salesFrom'],
                "salesTo": record['salesTo'],
                "deliveryStarts": record['deliveryStarts'],
                "deliveryEnds": record['deliveryEnds'],
                "platformValidity": record['platformValidity'],
                "calendarId": record['calendarId'],
                "category": record['category']
            }
            cohort_model.create(data)

        return http.request.redirect('/web')

    @http.route('/create_new_student', website=True, auth='public')
    def create_new_student(self):
        student_data = {
            "academicData": [
                {
                    "CGPA_GPA__c": "NA",
                    "Id": "a0P5i00000SCIQPEA5",
                    "Name": "10th",
                    "Percentage__c": "70",
                    "attributes": {
                        "type": "Academic__c",
                        "url": "/services/data/v58.0/sobjects/Academic__c/a0P5i00000SCIQPEA5"
                    }
                },
                {
                    "CGPA_GPA__c": "NA",
                    "Id": "a0P5i00000SCIQQEA5",
                    "Name": "12th",
                    "Percentage__c": "72",
                    "attributes": {
                        "type": "Academic__c",
                        "url": "/services/data/v58.0/sobjects/Academic__c/a0P5i00000SCIQQEA5"
                    }
                },
                {
                    "Graduation_Discipline__c": "CSE",
                    "Graduation_Qualifying_Degree__c": "BTech",
                    "Id": "a0P5i00000SCIQREA5",
                    "Institute__c": "LPU",
                    "Marks_Scored__c": "5500",
                    "Name": "Graduation",
                    "Total_Marks__c": "1000",
                    "University__c": "LPU",
                    "Year_of_Passing__c": "2020",
                    "attributes": {
                        "type": "Academic__c",
                        "url": "/services/data/v58.0/sobjects/Academic__c/a0P5i00000SCIQREA5"
                    }
                },
                {
                    "Graduation_Discipline__c": "CS",
                    "Graduation_Qualifying_Degree__c": "Masters",
                    "Id": "a0P5i00000SCIQSEA5",
                    "Institute__c": "LPU",
                    "Marks_Scored__c": "6600",
                    "Name": "PostGraduation",
                    "Total_Marks__c": "1000",
                    "University__c": "LPU",
                    "Year_of_Passing__c": "2024",
                    "attributes": {
                        "type": "Academic__c",
                        "url": "/services/data/v58.0/sobjects/Academic__c/a0P5i00000SCIQSEA5"
                    }
                },
                {
                    "Id": "a0P5i00000SCIQTEA5",
                    "Name": "Highest Graduation",
                    "attributes": {
                        "type": "Academic__c",
                        "url": "/services/data/v58.0/sobjects/Academic__c/a0P5i00000SCIQTEA5"
                    }
                },
                {
                    "Id": "a0P5i00000SCIQUEA5",
                    "Name": "Other Education Details-1",
                    "attributes": {
                        "type": "Academic__c",
                        "url": "/services/data/v58.0/sobjects/Academic__c/a0P5i00000SCIQUEA5"
                    }
                },
                {
                    "Id": "a0P5i00000SCIQVEA5",
                    "Name": "Other Education Details-2",
                    "attributes": {
                        "type": "Academic__c",
                        "url": "/services/data/v58.0/sobjects/Academic__c/a0P5i00000SCIQVEA5"
                    }
                },
                {
                    "Id": "a0P5i00000SCIQWEA5",
                    "Name": "Research Publication 1",
                    "Research_Publication_Authors__c": "Authors1,Authors2",
                    "Research_Publication_Journal__c": "No Journal Name",
                    "Research_Publication_Title__c": "Research One",
                    "Research_Publication_Year__c": "2000",
                    "attributes": {
                        "type": "Academic__c",
                        "url": "/services/data/v58.0/sobjects/Academic__c/a0P5i00000SCIQWEA5"
                    }
                },
                {
                    "Id": "a0P5i00000SCIQXEA5",
                    "Name": "Research Publication 2",
                    "Research_Publication_Authors__c": "Authors1,Authors2",
                    "Research_Publication_Journal__c": "No Journal Name",
                    "Research_Publication_Title__c": "Research Two",
                    "Research_Publication_Year__c": "2001",
                    "attributes": {
                        "type": "Academic__c",
                        "url": "/services/data/v58.0/sobjects/Academic__c/a0P5i00000SCIQXEA5"
                    }
                },
                {
                    "Id": "a0P5i00000SCIQYEA5",
                    "Name": "Research Publication 3",
                    "Research_Publication_Authors__c": "Authors1,Authors2",
                    "Research_Publication_Journal__c": "No Journal Name",
                    "Research_Publication_Title__c": "Research Three",
                    "Research_Publication_Year__c": "2002",
                    "attributes": {
                        "type": "Academic__c",
                        "url": "/services/data/v58.0/sobjects/Academic__c/a0P5i00000SCIQYEA5"
                    }
                },
                {
                    "Id": "a0P5i00000SCIQZEA5",
                    "Name": "Research Publication 4",
                    "Research_Publication_Authors__c": "Authors1,Authors2",
                    "Research_Publication_Journal__c": "No Journal Name",
                    "Research_Publication_Title__c": "Research Four",
                    "Research_Publication_Year__c": "2003",
                    "attributes": {
                        "type": "Academic__c",
                        "url": "/services/data/v58.0/sobjects/Academic__c/a0P5i00000SCIQZEA5"
                    }
                },
                {
                    "Id": "a0P5i00000SCIQaEAP",
                    "Name": "Research Publication 5",
                    "attributes": {
                        "type": "Academic__c",
                        "url": "/services/data/v58.0/sobjects/Academic__c/a0P5i00000SCIQaEAP"
                    }
                }
            ],
            "data": {
                "Aadhaar_Number__c": "17402404",
                "Age_Group__c": "Below 26",
                "Application_Fee_Form_Submitted__c": True,
                "Application_Fee_Paid_Date__c": "2024-04-24T12:11:07.000+0000",
                "Application_Fee__c": 1500,
                "Application_Order_Id__c": "1163689",
                "Application_PDF_Link__c": "https://emasters.iitk.ac.in//documents/98724-ed6a7b094e29c8b55241328ba89b0c30a2c1823818d462123061fc5c5478b952-48321.pdf",
                "Application_Process_Status__c": "Documents Submitted",
                "Basic_Details_Form_Submitted__c": True,
                "Birth_Date__c": "2010-10-10",
                "Caste_Category__c": "General",
                "City__c": "Hyderabad",
                "CohortProgramParentAccount__c": "Indian Institute of Technology Kanpur",
                "CohortProgram__c": "eFTM",
                "Cohort_Applied__c": "On Page",
                "Cohort_Name__c": "IITK-eFTM4-6",
                "Contacted__c": "New Lead",
                "Country__c": "India",
                "CreatedDate": "2024-04-24T12:10:25.000+0000",
                "Designation__c": "SDE",
                "Disability__c": "No",
                "District__c": "Hyderabad",
                "DoNotCall": False,
                "Do_Not_SMS__c": False,
                "Education_Details_Form_Submitted__c": True,
                "Education_Documents_Uploaded__c": True,
                "Email": "ansarisabid32+test@gmail.com",
                "EmailAddress": "ansarisabid32+test@gmail.com",
                "Experience_Details_Form_Submitted__c": False,
                "Experience_Documents_Uploaded__c": False,
                "Family_Member_Name__c": "F Name",
                "FirstName": "Sabid Ansari",
                "Gender__c": "Male",
                "HasOptedOutOfEmail": False,
                "Highest_Qualification__c": "M.Tech",
                "Id": "00Q5i00000dWjr7EAC",
                "IsConverted": False,
                "Landing_Page__c": "eMaster SOP Form Submitted",
                "LastName": "",
                "LeadId": "00Q5i00000dWjr7EAC",
                "Lead_Owner_Name__c": "Ishmeet K",
                "LinkedIn__c": "https://www.linkedin.com/in/sabid",
                "Marketing_Qualification__c": "MQL",
                "MobilePhone": "+91-9872448321",
                "NSDC_Form_Submitted__c": False,
                "Nationality__c": "Indian",
                "Organisation__c": "Organization One",
                "OwnerId": "0055i00000BAVzHAAX",
                "Permanent_Address_District__c": "Hyderabad",
                "Permanent_Address_State__c": "Telangana",
                "Permanent_Address_ZIP__c": "500032",
                "Permanent_Country__c": "India",
                "Permanent_Street__c": "Magna One Living, Indiranagar",
                "Phone": "+91-9872448321",
                "Postal_Code__c": "500032",
                "Program__c": "eFTM",
                "Program_and_Location__c": "IITK-eFTM4-6",
                "Registration_Form_Submitted__c": False,
                "SOP_Form_Submitted__c": False,
                "State__c": "Telangana",
                "Statement_of_Purpose__c": "Write between 100 - 250 words (1000 characters)\r\nWrite about why you want to enrol in to the program\r\nWrite about what you hope to achieve from the program\r\nBe clear and specific\r\nEdit and proofreadWrite between 100 - 250 words (1000 characters)\r\nWrite about why you want to enrol in to the program\r\nWrite about what you hope to achieve from the program\r\nBe clear and specific\r\nEdit and proofreadWrite between 100 - 250 words (1000 characters)\r\nWrite about cific\r\nEdit and proofreadwhy you want to enrol in to the program\r\nWrite about what you hope to achieve from the program\r\nBe clear and spebout why you want to enrol in to the program\r\nWrite about what you hope to achieve from the program\r\nBe clear and specific\r\nEdit and proofreadWrite between 100 - 250 words (1000 characters)\r\nWrite about why you want to enrol in to the program\r\nWrite about what you hope to achieve from the program\r\nBe clear and specific\r\nEdit and proofreadWrite between 100 - 250 words (1000 characters)\r\nWrite about cific\r\nEdit and proofreadw",
                "Status": "Applicant Documents Uploaded",
                "Street__c": "Magna One Living, Indiranagar",
                "Total_Experience__c": "2 - 5 Years",
                "Upload_Document_Form_Submitted__c": True,
                "attributes": {
                    "type": "Lead",
                    "url": "/services/data/v58.0/sobjects/Lead/00Q5i00000dWjr7EAC"
                },
                "mx_City": "Hyderabad",
                "mx_Program": "eFTM"
            },
            "employerData": [
                {
                    "Company_Working_Since__c": "2020-10",
                    "Company_Working_Till__c": "2021-10",
                    "Employment_Status__c": "Permanent Employee",
                    "Functional_Area__c": "Lead",
                    "Gross_Pay_per_Annum__c": "Below 5 lakh",
                    "Id": "a0V5i00000IRnZFEA1",
                    "Job_Title__c": "SDE",
                    "Name": "Organization One",
                    "Nature_Of_Occupation__c": "Research and Development",
                    "Occupational_Fields__c": "IT and ITEs",
                    "Presently_Working__c": "Experience Latest",
                    "Type_Of_Organisation__c": "Private Sector - MNCs",
                    "attributes": {
                        "type": "Employer__c",
                        "url": "/services/data/v58.0/sobjects/Employer__c/a0V5i00000IRnZFEA1"
                    }
                },
                {
                    "Id": "a0V5i00000IRnZGEA1",
                    "Name": "a0V5i00000IRnZG",
                    "attributes": {
                        "type": "Employer__c",
                        "url": "/services/data/v58.0/sobjects/Employer__c/a0V5i00000IRnZGEA1"
                    }
                },
                {
                    "Company_Working_Since__c": "2021-10",
                    "Company_Working_Till__c": "2023-10",
                    "Id": "a0V5i00000IRnZHEA1",
                    "Job_Title__c": "SDE",
                    "Name": "Organization Two",
                    "Presently_Working__c": "Experience 2",
                    "Type_Of_Organisation__c": "Private Sector - MNCs",
                    "attributes": {
                        "type": "Employer__c",
                        "url": "/services/data/v58.0/sobjects/Employer__c/a0V5i00000IRnZHEA1"
                    }
                },
                {
                    "Company_Working_Since__c": "2023-10",
                    "Company_Working_Till__c": "2024-10",
                    "Id": "a0V5i00000IRnZIEA1",
                    "Job_Title__c": "SDE",
                    "Name": "Organization Three",
                    "Presently_Working__c": "Experience 3",
                    "Type_Of_Organisation__c": "Public Sector - State Government",
                    "attributes": {
                        "type": "Employer__c",
                        "url": "/services/data/v58.0/sobjects/Employer__c/a0V5i00000IRnZIEA1"
                    }
                },
                {
                    "Id": "a0V5i00000IRnZJEA1",
                    "Name": "a0V5i00000IRnZJ",
                    "attributes": {
                        "type": "Employer__c",
                        "url": "/services/data/v58.0/sobjects/Employer__c/a0V5i00000IRnZJEA1"
                    }
                },
                {
                    "Id": "a0V5i00000IRnZKEA1",
                    "Name": "a0V5i00000IRnZK",
                    "attributes": {
                        "type": "Employer__c",
                        "url": "/services/data/v58.0/sobjects/Employer__c/a0V5i00000IRnZKEA1"
                    }
                }
            ],
            "leadId": "00Q5i00000dWjr7EAC",
            "message": "Success",
            "status_code": "1001",
            "success": True
        }

        data = student_data.get('data', False)

        student_name = ''
        FirstName = data.get('FirstName', False)
        LastName = data.get('LastName', False)
        if FirstName and LastName:
            student_name = ' '.join([FirstName, LastName])
        elif FirstName and not LastName:
            student_name = FirstName
        elif LastName and not FirstName:
            student_name = LastName

        existing_student = http.request.env['res.partner'].search([('name', '=', student_name)])

        if existing_student:
            # Handle duplicate scenario (log, update existing record, etc.)
            # self.write({'status': 'duplicate'})  # Update webhook record status
            # ... (Optional: Update existing student record if needed)
            return "<H1>Student already exists</H1>"

        objResPartner = http.request.env['res.partner']
        objStudentAcademic = http.request.env['student.academic']
        objStudentEmployer = http.request.env['student.employer']
        objCountry = http.request.env['res.country']

        lst_student_academic = []
        for academic in student_data.get('academicData'):
            # student_academic = objStudentAcademic.search([('academicId', '=', academic['Id'])], limit=1)
            # if not student_academic:
            student_academic = objStudentAcademic.create({
                'academicId': academic.get('Id'),
                'university': academic.get('University__c', ''),
                'institute': academic.get('Institute__c', ''),
                'academic_name': academic.get('Name', ''),
                'graduation_qualifying_degree': academic.get('Graduation_Qualifying_Degree__c', ''),
                'research_publication_title': academic.get('Research_Publication_Title__c', ''),
                'graduation_discipline': academic.get('Graduation_Discipline__c', ''),
                'year_of_passing': academic.get('Year_of_Passing__c', ''),
                'marks_scored': academic.get('Marks_Scored__c', ''),
                'total_marks': academic.get('Total_Marks__c', ''),
                'cgpa_gpa': academic.get('CGPA_GPA__c', ''),
                'percentage': academic.get('Percentage__c', ''),
                'attribute_type': academic.get('attributes', False) and academic['attributes'].get('type', ''),
                'attribute_url': academic.get('attributes', False) and academic['attributes'].get('url', '')
            })

            lst_student_academic.append(student_academic.id)

        lst_student_employer = []
        for employer in student_data.get('employerData'):
            # student_employer = objStudentEmployer.search([('employerId', '=', employer['Id'])], limit=1)
            # if not student_employer:
            student_employer = objStudentEmployer.create({
                'employerId': employer.get('Id'),
                'employer_name': employer.get('Name', ''),
                'type_of_organisation': employer.get('Type_Of_Organisation__c', ''),
                'job_title': employer.get('Job_Title__c', ''),
                'working_since': employer.get('Company_Working_Since__c', ''),
                'working_till': employer.get('Company_Working_Till__c', ''),
                'functional_area': employer.get('Functional_Area__c', ''),
                'nature_of_occupation': employer.get('Nature_Of_Occupation__c', ''),
                'occupational_fields': employer.get('Occupational_Fields__c', ''),
                'presently_working': employer.get('Presently_Working__c', ''),
                'gross_pay_per_annum': employer.get('Gross_Pay_per_Annum__c', ''),
                'employment_status': employer.get('Employment_Status__c', ''),
                'attribute_type': employer.get('attributes', False) and employer['attributes'].get('type', ''),
                'attribute_url': employer.get('attributes', False) and employer['attributes'].get('url', '')
            })
            lst_student_employer.append(student_employer.id)

        if data:
            country_name = data.get('Country__c', False)
            country = False
            if country_name:
                country = objCountry.search([('name', '=ilike', country_name)], limit=1)

            state_name = data.get('State__c', False)
            state = False
            if state_name:
                state = objCountry.search([['name', '=ilike', state_name]], limit=1)

            if data.get('CreatedDate', False):
                create_date = datetime.strptime(str(data.get('CreatedDate')), '%Y-%m-%dT%H:%M:%S.%f%z')
                create_date = create_date.strftime("%Y-%m-%d %H:%M:%S")

            else:
                create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            email = data.get('Email')
            student = objResPartner.search([('email', '=', email)], limit=1)
            if not student:
                student = objResPartner.create({
                    'is_student': True,
                    'create_date': create_date,

                    'name': student_name,
                    'email': data.get('Email', ''),
                    'phone': data.get('Phone', ''),
                    'mobile': data.get('MobilePhone', ''),
                    'gender': data.get('Gender__c', ''),
                    'function': data.get('Designation__c', ''),
                    'organisation': data.get('Organisation__c', ''),

                    'nationality': data.get('Nationality__c', ''),
                    'street': data.get('Street__c', ''),
                    'city': data.get('City__c', ''),
                    'district': data.get('District__c', ''),
                    'zip': data.get('Postal_Code__c', ''),
                    'state_id': state and state.id or False,
                    'country_id': country and country.id or False,

                    'permanent_street': data.get('Permanent_Street__c', ''),
                    'permanent_city': data.get('mx_City', ''),
                    'permanent_district': data.get('Permanent_Address_District__c', ''),
                    'permanent_zip': data.get('Permanent_Address_ZIP__c', ''),
                    'permanent_state': data.get('Permanent_Address_State__c', ''),
                    'permanent_country': data.get('Permanent_Country__c', ''),

                    'family_member_name': data.get('Family_Member_Name__c', ''),
                    'aadhaar_number': data.get('Aadhaar_Number__c', ''),
                    'age_group': data.get('Age_Group__c', ''),
                    'birth_date': data.get('Birth_Date__c', ''),
                    'caste_category': data.get('Basic_Details_Form_Submitted__c', ''),

                    'disability': data.get('Disability__c', ''),
                    'converted': data.get('IsConverted', False),
                    'do_not_call': data.get('DoNotCall', False),
                    'do_not_sms': data.get('Do_Not_SMS__c', False),
                    'do_not_email': data.get('HasOptedOutOfEmail', False),

                    'highest_qualification': data.get('Highest_Qualification__c', ''),
                    'education_details_form_submitted': data.get('Education_Details_Form_Submitted__c', False),
                    'education_documents_uploaded': data.get('Education_Documents_Uploaded__c', False),

                    'total_experience': data.get('Total_Experience__c', ''),
                    'marketing_qualification': data.get('Marketing_Qualification__c', ''),
                    'experience_details_form_submitted': data.get('Experience_Details_Form_Submitted__c', False),
                    'experience_documents_uploaded': data.get('Experience_Documents_Uploaded__c', False),

                    'application_fee_form_submitted': data.get('Application_Fee_Form_Submitted__c', False),
                    'application_fee_paid_date': data.get('Application_Fee_Paid_Date__c', ''),
                    'application_fee': data.get('Application_Fee__c', ''),
                    'application_order_id': data.get('Application_Order_Id__c', ''),
                    'application_pdf_link': data.get('Application_PDF_Link__c', ''),
                    'application_process_status': data.get('Application_Process_Status__c', ''),

                    'basic_details_form_submitted': data.get('Basic_Details_Form_Submitted__c', False),
                    'upload_document_form_submitted': data.get('Upload_Document_Form_Submitted__c', False),
                    'registration_form_submitted': data.get('Registration_Form_Submitted__c', False),
                    'sop_form_submitted': data.get('SOP_Form_Submitted__c', False),
                    'nsdc_form_submitted': data.get('NSDC_Form_Submitted__c', False),

                    'cohort_name': data.get('Cohort_Name__c', ''),
                    'cohort_program_parent_account': data.get('CohortProgramParentAccount__c', ''),
                    'cohort_program': data.get('CohortProgram__c', ''),
                    'cohort_applied': data.get('Cohort_Applied__c', ''),

                    'program': data.get('Program__c', ''),
                    'program_and_location': data.get('Program_and_Location__c', ''),
                    'landing_page': data.get('Landing_Page__c', ''),

                    'comment': data.get('Statement_of_Purpose__c', ''),
                    'status': data.get('Status', ''),

                    'student_academic': [(6, 0, lst_student_academic)],
                    'student_employer': [(6, 0, lst_student_employer)]
                })
            else:
                student.student_academic = [(6, 0, lst_student_academic)]
                student.student_employer = [(6, 0, lst_student_employer)]

        return http.request.redirect('/web')