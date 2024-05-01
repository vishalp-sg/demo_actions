# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(string='Is Student', default=False)
    student_academic = fields.One2many('student.academic', 'student', string='Student Academics')
    student_employer = fields.One2many('student.employer', 'student', string='Student Employers')

    nationality = fields.Char(string='Nationality')
    district = fields.Char(string='District')

    permanent_street = fields.Char(string='Permanent Street')
    permanent_city = fields.Char(string='Permanent City')
    permanent_district = fields.Char(string='Permanent District')
    permanent_state = fields.Char(string='Permanent State')
    permanent_zip = fields.Char(string='Permanent Zip')
    permanent_country = fields.Char(string='Permanent Country')

    family_member_name = fields.Char(string='Family Member Name')
    gender = fields.Char(string='Gender')
    aadhaar_number = fields.Char(string='Aadhaar Number')
    age_group = fields.Char(string='Age Group')
    birth_date = fields.Char(string='Birth Date')
    caste_category = fields.Char(string='Caste Category')
    organisation = fields.Char(string='Organisation')

    highest_qualification = fields.Char(string='Highest Qualification')
    education_details_form_submitted = fields.Boolean(string='Education Details Form Submitted')
    education_documents_uploaded = fields.Boolean(string='Education Documents Uploaded')

    total_experience = fields.Char(string='Total Experience')
    marketing_qualification = fields.Char(string='Marketing Qualification')
    experience_details_form_submitted = fields.Char(string='Experience Details Form Submitted')
    experience_documents_uploaded = fields.Char(string='Experience Documents Uploaded')

    disability = fields.Char(string='Disability')
    converted = fields.Boolean(string='Is Converted')
    do_not_call = fields.Boolean(string='Do Not Call')
    do_not_sms = fields.Boolean(string='Do Not SMS')
    do_not_email = fields.Boolean(string='Do Not Email')

    application_fee_form_submitted = fields.Boolean(string='Application Fee Form Submitted')
    application_fee_paid_date = fields.Char(string='Application Fee Paid Date')
    application_fee = fields.Float(string='Application Fee')
    application_order_id = fields.Char(string='Application Order ID')
    application_pdf_link = fields.Char(string='Application PDF Link')
    application_process_status = fields.Char(string='Application Process Status')

    basic_details_form_submitted = fields.Boolean(string='Basic Details Form Submitted')
    upload_document_form_submitted = fields.Boolean(string='Upload Document Form Submitted')
    registration_form_submitted = fields.Boolean(string='Registration Form Submitted')
    sop_form_submitted = fields.Boolean(string='SOP Form Submitted')
    nsdc_form_submitted = fields.Boolean(string='NSDC Form Submitted')

    cohort_name = fields.Char(string='Cohort Name')
    cohort_program_parent_account = fields.Char(string='Cohort Program Parent Account')
    cohort_program = fields.Char(string='Cohort Program')
    cohort_applied = fields.Char(string='Cohort Applied')

    program = fields.Char(string='Program')
    program_and_location = fields.Char(string='Program and Location')
    landing_page = fields.Char(string='Landing Page')
    status = fields.Char(string='Status')
