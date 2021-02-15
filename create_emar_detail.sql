use MIMICIV;

CREATE TABLE emar_detail
(
	SUBJECT_ID INT NOT NULL,
	EMAR_ID VARCHAR(25) NOT NULL,
	EMAR_SEQ INT NOT NULL,
	PARENT_FIELD_ORDINAL DOUBLE PRECISION ,
	ADMINISTRATION_TYPE VARCHAR(50) ,
	PHARMACY_ID INT ,
	BARCODE_TYPE VARCHAR(4) ,
	REASON_FOR_NO_BARCODE TEXT ,
	COMPLETE_DOSE_NOT_GIVEN  VARCHAR(5),
	DOSE_DUE VARCHAR(55) ,
	DOSE_DUE_UNIT VARCHAR(30) ,
	DOSE_GIVEN VARCHAR(155) ,
	DOSE_GIVEN_UNIT VARCHAR(30) ,
	WILL_REMAINDER_OF_DOSE_BE_GIVEN VARCHAR(5),
	PRODUCT_AMOUNT_GIVEN VARCHAR(30) ,
	PRODUCT_UNIT VARCHAR(30) ,
	PRODUCT_CODE VARCHAR(30) ,
	PRODUCT_DESCRIPTION VARCHAR(200) ,
	PRODUCT_DESCRIPTION_OTHER VARCHAR(100),
	PRIOR_INFUSION_RATE VARCHAR(25),
	INFUSION_RATE VARCHAR(25) ,
	INFUSION_RATE_ADJUSTMENT VARCHAR(40) ,
	INFUSION_RATE_ADJUSTMENT_AMOUNT VARCHAR(30) ,
	INFUSION_RATE_UNIT VARCHAR(30) ,
	ROUTE VARCHAR(10) ,
	INFUSION_COMPLETE VARCHAR(10) ,
	COMPLETION_INTERVAL VARCHAR(30) ,
	NEW_IV_BAG_HUNG VARCHAR(5) ,
	CONTINUED_INFUSION_IN_OTHER_LOCATION VARCHAR(5) ,
	RESTART_INTERVAL VARCHAR(30) ,
	SIDE VARCHAR(10) ,
	SITE VARCHAR(250) ,
	NON_FORMULARY_VISUAL_VERIFICATION VARCHAR(5)
);
