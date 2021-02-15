import numpy as np

"""
IMPORTANT STUFF
1) I have ignored unsigned ints because some of the int columns
have missing values, so im using -1 and it's not unsigned compatible

2) Dates are all objects because np.datetime64 is out of bounds with 
the dates in the future that are set un this datasets due to anonymizing process
"""

mimic4_types = {
    'admissions': {
        'subject_id': np.int32,
        'hadm_id': np.int32,
        'admittime': np.dtype(object),
        'dischtime': np.dtype(object),
        'deathtime': np.dtype(object),
        'admission_type': np.dtype(str),
        'admission_location': np.dtype(str),
        'discharge_location': np.dtype(str),
        'insurance': np.dtype(str),
        'language': np.dtype(str),
        'marital_status': np.dtype(str),
        'ethnicity': np.dtype(str),
        'edregtime': np.dtype(object),
        'edouttime': np.dtype(object),
        'hospital_expire_flag': np.dtype(bool)
    },
    'chartevents': {
        'subject_id': np.int32,
        'hadm_id': np.int32,
        'stay_id': np.int32,
        'charttime': np.dtype(object),
        'storetime': np.dtype(object),
        'itemid': np.int32,
        'value': np.dtype(object),
        'valuenum': np.float32,
        'valueuom': np.dtype(str),
        'warning': np.dtype(bool)
    },

    'd_hcpcs': {
        'code': np.dtype(str),
        'category': np.int16,
        'long_description': np.dtype(str),
        'short_description': np.dtype(str),
    },

    'd_icd_diagnoses': {
        'icd_code': np.dtype(str),
        'icd_version': np.uint8,
        'long_title': np.dtype(str)
    },

    'd_icd_procedures': {
        'icd_code': np.dtype(str),
        'icd_version': np.uint8,
        'long_title': np.dtype(str)
    },

    'd_items': {
        'itemid': np.int32,
        'label': np.dtype(str),
        'abbreviation': np.dtype(str),
        'linksto': np.dtype(str),
        'category': np.dtype(str),
        'unitname': np.dtype(str),
        'param_type': np.dtype(str),
        'lownormalvalue': np.int16,
        'highnormalvalue': np.float32
    },

    'd_labitems': {
        'itemid': np.int32,
        'label': np.dtype(str),
        'fluid': np.dtype(str),
        'category': np.dtype(str),
        'loinc_code': np.dtype(str),
    },

    'datetimeevents': {
        'subject_id': np.int32,
        'hadm_id': np.int32,
        'stay_id': np.int32,
        'charttime': np.dtype(object),
        'storetime': np.dtype(object),
        'itemid': np.int32,
        #: datetime64 generates out of bounds error
        'value': np.dtype(object),
        'valueuom': np.dtype(str),
        'warning': np.dtype(bool)
    },

    'diagnoses_icd': {
        'subject_id': np.int64,
        'hadm_id': np.int64,
        'seq_num': np.int16,
        'icd_code': np.dtype(str),
        'icd_version': np.int16,
    },

    'drgcodes': {
        'subject_id': np.int32,
        'hadm_id': np.int32,
        'drg_type': np.dtype(str),
        'drg_code': np.dtype(str),
        'description': np.dtype(str),
        'drg_severity': np.int16,
        'drg_mortality': np.int16,
    },

    'emar': {
        'subject_id': np.int32,
        'hadm_id': np.int32,
        'emar_id': np.dtype(str),
        'emar_seq': np.int16,
        'poe_id': np.dtype(str),
        'pharmacy_id': np.int32,
        'charttime': np.dtype(object),
        'medication': np.dtype(str),
        'event_txt': np.dtype(str),
        'scheduletime': np.dtype(object),
        'storetime': np.dtype(object)
    },

    'emar_detail': {
        'subject_id': np.int32,
        'emar_id': np.dtype(str),
        'emar_seq': np.int32,
        'parent_field_ordinal': np.float64,
        'administration_type': np.dtype(str),
        'pharmacy_id': np.int32,
        'barcode_type': np.dtype(str),
        'reason_for_no_barcode': np.dtype(str),
        'complete_dose_not_given': np.dtype(str),
        'dose_due': np.dtype(str),
        'dose_due_unit': np.dtype(str),
        'dose_given': np.dtype(str),
        'dose_given_unit': np.dtype(str),
        'will_remainder_of_dose_be_given': np.dtype(str),
        'product_amount_given': np.dtype(str),
        'product_unit': np.dtype(str),
        'product_code': np.dtype(str),
        'product_description': np.dtype(str),
        'product_description_other': np.dtype(str),
        'prior_infusion_rate': np.dtype(str),
        'infusion_rate': np.dtype(str),
        'infusion_rate_adjustment': np.dtype(str),
        'infusion_rate_adjustment_amount': np.dtype(str),
        'infusion_rate_unit': np.dtype(str),
        'route': np.dtype(str),
        'infusion_complete': np.dtype(str),
        'completion_interval': np.dtype(str),
        'new_iv_bag_hung': np.dtype(str),
        'continued_infusion_in_other_location': np.dtype(str),
        'restart_interval': np.dtype(str),
        'side': np.dtype(str),
        'site': np.dtype(str),
        'non_formulary_visual_verification': np.dtype(str),
    },

    'hcpcsevents': {

        'subject_id': np.int32,
        'hadm_id': np.int32,
        'hcpcs_cd': np.dtype(str),
        'seq_num': np.int16,
        'short_description': np.dtype(str)
    },

    'icustays': {
        'subject_id': np.int64,
        'hadm_id': np.int64,
        'stay_id': np.int64,
        'first_careunit': np.dtype(str),
        'last_careunit': np.dtype(str),
        'intime': np.dtype(object),
        'outtime': np.dtype(object),
        'los': np.float64,
    },

    'inputevents': {
        'subject_id': np.int32,
        'hadm_id': np.int32,
        'stay_id': np.int32,
        'starttime': np.dtype(object),
        'endtime': np.dtype(object),
        'storetime': np.dtype(object),
        'itemid': np.int32,
        'amount': np.float64,
        'amountuom': np.dtype(str),
        'rate': np.float64,
        'rateuom':  np.dtype(str),
        'orderid': np.int32,
        'linkorderid': np.int32,
        'ordercategoryname': np.dtype(str),
        'secondaryordercategoryname': np.dtype(str),
        'ordercomponenttypedescription': np.dtype(str),
        'ordercategorydescription': np.dtype(str),
        'patientweight': np.float64,
        'totalamount': np.float64,
        'totalamountuom': np.dtype(str),
        'isopenbag': np.dtype(bool),
        'continueinnextdept': np.dtype(bool),
        'cancelreason': np.int16,
        'statusdescription': np.dtype(str),
        'originalamount': np.float64,
        'originalrate': np.float64,
    },

    'labevents': {
        'labevent_id':  np.int64,
        'subject_id':  np.int64,
        'hadm_id':  np.int64,
        'specimen_id':  np.int64,
        'itemid':  np.int64,
        'charttime': np.dtype(object),
        'storetime': np.dtype(object),
        'value': np.dtype(str),
        'valuenum': np.float64,
        'valueuom': np.dtype(str),
        'ref_range_lower': np.float64,
        'ref_range_upper': np.float64,
        'flag': np.dtype(str),
        'priority': np.dtype(str),
        'comments': np.dtype(str)
    },

    'microbiologyevents': {
        'microevent_id':  np.int32,
        'subject_id':  np.int64,
        'hadm_id':  np.int64,
        'micro_specimen_id':  np.int32,
        'chartdate': np.dtype(object),
        'charttime': np.dtype(object),
        'spec_itemid':  np.int32,
        'spec_type_desc': np.dtype(str),
        'test_seq':  np.int16,
        'storedate': np.dtype(object),
        'storetime': np.dtype(object),
        'test_itemid':  np.int32,
        'test_name': np.dtype(str),
        'org_itemid':  np.int32,
        'org_name': np.dtype(str),
        'isolate_num':  np.int16,
        'quantity': np.dtype(str),
        'ab_itemid':  np.int32,
        'ab_name': np.dtype(str),
        'dilution_text': np.dtype(str),
        'dilution_comparison': np.dtype(str),
        'dilution_value': np.float64,
        'interpretation': np.dtype(str),
        'comments': np.dtype(str)
    },

    'outputevents': {
        'subject_id':  np.int64,
        'hadm_id':  np.int64,
        'stay_id':  np.int64,
        'charttime': np.dtype(object),
        'storetime': np.dtype(object),
        'itemid':  np.int32,
        'value': np.float64,
        'valueuom': np.dtype(str)
    },

    'patients': {
        'subject_id':  np.int64,
        'gender': np.dtype(str),
        'anchor_age':  np.int16,
        'anchor_year':  np.int64,
        'anchor_year_group': np.dtype(str),
        'dod': np.dtype(str)
    },

    'pharmacy': {
        'subject_id':  np.int64,
        'hadm_id':  np.int64,
        'pharmacy_id':  np.int64,
        'poe_id': np.dtype(str),
        'starttime': np.dtype(object),
        'stoptime': np.dtype(object),
        'medication': np.dtype(str),
        'proc_type': np.dtype(str),
        'status': np.dtype(str),
        'entertime': np.dtype(object),
        'verifiedtime': np.dtype(object),
        'route': np.dtype(str),
        'frequency': np.dtype(str),
        'disp_sched': np.dtype(str),
        'infusion_type': np.dtype(str),
        'sliding_scale': np.dtype(str),
        'lockout_interval': np.dtype(str),
        'basal_rate': np.float64,
        'one_hr_max': np.dtype(str),
        'doses_per_24_hrs':  np.int16,
        'duration': np.float64,
        'duration_interval': np.dtype(str),
        'expiration_value': np.int64,
        'expiration_unit': np.dtype(str),
        'expirationdate': np.dtype(object),
        'dispensation': np.dtype(str),
        'fill_quantity': np.dtype(str)
    },

    'poe': {
        'poe_id': np.dtype(str),
        'poe_seq':  np.int64,
        'subject_id':  np.int64,
        'hadm_id':  np.int64,
        'ordertime': np.dtype(object),
        'order_type': np.dtype(str),
        'order_subtype': np.dtype(str),
        'transaction_type': np.dtype(str),
        'discontinue_of_poe_id': np.dtype(str),
        'discontinued_by_poe_id': np.dtype(str),
        'order_status': np.dtype(str)
    },

    'poe_detail': {
        'poe_id': np.dtype(str),
        'poe_seq': np.int64,
        'subject_id':  np.int64,
        'field_name': np.dtype(str),
        'field_value': np.dtype(str)
    },

    'prescriptions': {
        'subject_id':  np.int64,
        'hadm_id':  np.int64,
        'pharmacy_id':  np.int64,
        'starttime': np.dtype(object),
        'stoptime': np.dtype(object),
        'drug_type': np.dtype(str),
        'drug': np.dtype(str),
        'gsn': np.dtype(str),
        'ndc': np.dtype(str),
        'prod_strength': np.dtype(str),
        'form_rx': np.dtype(str),
        'dose_val_rx': np.dtype(str),
        'dose_unit_rx': np.dtype(str),
        'form_val_disp': np.dtype(str),
        'form_unit_disp': np.dtype(str),
        'doses_per_24_hrs':  np.int16,
        'route': np.dtype(str)
    },

    'procedureevents': {
        'subject_id':  np.int64,
        'hadm_id':  np.int64,
        'stay_id':  np.int64,
        'starttime': np.dtype(object),
        'endtime': np.dtype(object),
        'storetime': np.dtype(object),
        'itemid':  np.int32,
        'value': np.float64,
        'valueuom': np.dtype(str),
        'location': np.dtype(str),
        'locationcategory': np.dtype(str),
        'orderid':  np.int32,
        'linkorderid':  np.int32,
        'ordercategoryname': np.dtype(str),
        'secondaryordercategoryname': np.dtype(str),
        'ordercategorydescription': np.dtype(str),
        'patientweight': np.float64,
        'totalamount': np.dtype(str),
        'totalamountuom': np.dtype(str),
        'isopenbag':  np.dtype(bool),
        'continueinnextdept':  np.int8,
        'cancelreason':  np.int8,
        'statusdescription': np.dtype(str),
        'comments_date': np.dtype(str),
        'originalamount': np.float64,
        'originalrate':  np.dtype(bool),
    },

    'procedures_icd': {
        'subject_id':  np.int64,
        'hadm_id':  np.int64,
        'seq_num':  np.int16,
        'icd_code': np.dtype(str),
        'icd_version':  np.int16
    },

    'services': {
        'subject_id':  np.int64,
        'hadm_id':  np.int64,
        'transfertime': np.dtype(object),
        'prev_service': np.dtype(str),
        'curr_service': np.dtype(str)
    },

    'transfers': {
        'subject_id':  np.int64,
        'hadm_id':  np.int64,
        'transfer_id':  np.int64,
        'eventtype': np.dtype(str),
        'careunit': np.dtype(str),
        'intime': np.dtype(object),
        'outtime': np.dtype(object)
    }


}
