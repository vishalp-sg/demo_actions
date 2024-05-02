# -*- coding: utf-8 -*-

from odoo import exceptions, fields, models
from datetime import datetime
import json
import ast


class WebhookLeads(models.Model):
    _name = 'webhook.leads'
    _rec_name = "leadId"
    _description = 'Webhook Leads'

    method = fields.Selection([
        ('POST', 'POST'),
        ('GET', 'GET'),
    ])
    leadId = fields.Char('Lead ID')
    request = fields.Char('Request')
    params = fields.Text('Params')
    response = fields.Char('Response')
    status = fields.Selection([
        ('success', 'Success'),
        ('failed', 'Failed')
    ], 'Status')
    is_store = fields.Boolean('Is Store', default=False)
    crm_lead = fields.Many2one('crm.lead', 'Lead')

    def execute(self):
        objCrmLead = self.env['crm.lead']
        objResPartner = self.env['res.partner']
        objStudentAcademic = self.env['student.academic']
        objStudentEmployer = self.env['student.employer']
        objCountry = self.env['res.country']
        objState = self.env['res.country.state']
        objCohorts = self.env['cohorts.cohorts']

        for rec in self.filtered(lambda r: not r.is_store and r.status == 'success'):
            if rec.id == 5:
                import json
                vals = json.loads(rec.response)
            else:
                vals = ast.literal_eval(rec.response)

            lst_student_academic = []
            for academic in vals.get('academicData'):
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
            for employer in vals.get('employerData'):
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

            data = vals.get('data', False)

            student_name = ''
            FirstName = data.get('FirstName', False)
            LastName = data.get('LastName', False)
            if FirstName and LastName:
                student_name = ' '.join([FirstName, LastName])
            elif FirstName and not LastName:
                student_name = FirstName
            elif LastName and not FirstName:
                student_name = LastName

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

                        'application_fee_form_submitted' : data.get('Application_Fee_Form_Submitted__c', False),
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

                if student:
                    cohorts = objCohorts.search([])
                    cohorts.write({
                        'students': [(4, student.id)]
                    })
                    # lead = objCrmLead.create({
                    #     'leadId': data.get('LeadId', ''),
                    #     'partner_id': student.id,

                    #     'ownerId': data.get('OwnerId', ''),
                    #     'lead_owner_name': data.get('Lead_Owner_Name__c', ''),
                    #     'linkedin': data.get('LinkedIn__c', ''),

                    #     'cohort_name': data.get('Cohort_Name__c', ''),
                    #     'cohort_program_parent_account': data.get('CohortProgramParentAccount__c', ''),
                    #     'cohort_program': data.get('CohortProgram__c', ''),
                    #     'cohort_applied': data.get('Cohort_Applied__c', ''),

                    #     'program': data.get('Program__c', ''),
                    #     'program_and_location': data.get('Program_and_Location__c', ''),
                    #     'landing_page': data.get('Landing_Page__c', ''),

                    #     'description': data.get('Statement_of_Purpose__c', ''),
                    #     'status': data.get('Status', ''),

                    #     'name': student.name + "'s opportunity",
                    #     'partner_name': student.name,
                    #     'type': 'opportunity'
                    # })
                    # if lead:
                    #     rec.write({'is_store': True, 'crm_lead': lead.id})

                    objUser = self.env['res.users']
                    user = objUser.search([('login', '=', student.email)], limit=1)
                    if not user:
                        objUser.create({
                            'name': student.name,
                            'login': student.email,
                            'partner_id': student.id,
                            'email': student.email,
                            'groups_id': [(6, 0, [self.env.ref('base.group_portal').id])]
                        })

                    rec.write({'is_store': True})
                    # if user:
                    #     user.action_reset_password()


