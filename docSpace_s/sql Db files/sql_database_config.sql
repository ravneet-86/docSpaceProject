-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: docSpace
-- ------------------------------------------------------
-- Server version	8.0.26

-- Create Main DataBase file

-- drop database DocSpace;

show databases;

select * from reception.userInfo;



use DocSpace;

-- Create remedy table --

-- Commands to run on first time installation 
-- Create DOC Space
create database DocSpace;

-- Create Doctor Information table
create table doctor_info (
							name varchar(20) not null,
							email varchar(30) not null primary key,
                            password varchar(10) not null,
							contact_no varchar(12) not null,
							mobile_no varchar(10) not null,
							clinic_name varchar(20) not null,
							clinic_address varchar(50) not null,
                            index(name, email)
							);

-- Crate remedy db
create database avRemedyDb;

---------------------------------------

use avRemedyDb;
show tables;
 
create table doctor_info_file_i(
							insert_id int not null primary key auto_increment,
							file_name char(200) not null,
                            creation_date date not null,
                            is_backed_up bool not null,
                            back_up_creation_date_time date,
                            file_size int,
                            index (insert_id));

insert into DocSpace.doctor_info_file_i (file_name, creation_date, is_backed_up) values
("doctor_info_file_i_first.csv", CURDATE(), false);
                            
select * from doctor_info;
select * from DocSpace.bhusan_homeo_patient_infoa_joshi_medical_recorda_joshi_medical_record;

insert into DocSpace.doctor_info (name, email, password, contact_no, mobile_no, clinic_name, clinic_address) values
("Ravneet Singh", "ravne1986@gmail.com", "megadeth", "8297192121", "8297192121", "Homeopathy", "Dehradun");

insert into DocSpace.doctor_info (name, email, password, contact_no, mobile_no, clinic_name, clinic_address) values
("ravneet", "r@gmail.com", "m", "8297192121", "8297192121", "Homeopathy", "Dehradun");

insert into DocSpace.anand_patient_info (name,gender, age,contact_no, address,city,martial_status,occupation,dob) values
("ra", "g", "10", "8297192121", "DDN", "ddn","u", "none", "STR_TO_DATE('04-09-1986', '%d-%m-%Y')");

select * from anand_patient_info where name like ('u%') or address like ('%u%') or occupation like ('u%');


update DocSpace.anand_medical_record set patient_id = '1' , record_date = '2022-03-13' , case_type = '1' , symptoms = 'stress and numbness' , symptoms_agg_by = '10' , symptoms_ameol_by = '' , symptoms_since = '6 months' , present_complains = '' , appetite = '' , thirst = '' , urine = '' , stool = '' , sleep = '' , perspiration = '' , addiction = '' , desires = '' , aversions = '' , thermal_reaction = '' , allergy = '' , mental_symptoms = '' , back = '' , chest = '' , ear = '' , eye = '' , face = '' , head = '' , lips = '' , mouth = '' , nose = '' , teeth = '' , throat = '' , tongue = '' , past_history = '' , family_history = '' , menstrual_history = '' , Investigation = 'stress and numbness' , medicine = '%%abcd%%%%%' , dose = '%%1%%%%%' , potency = '%%3%%%%%' , days = '%%10 days%%%%%' , next_visit_date = '2022-03-13' , amount = '%%100%%%%%' where patient_id = 1 and record_date = 2022-03-13;

update anand_patient_info set dob = "1980/3/11" where patient_id = '1';

select * from anand_patient_info;

update DocSpace.anand_patient_info set name = 'sarv' , gender = 'g' , age = '10' , contact_no = '8297192121' , address = 'ajab coloney
near sabji man
ajabpur
' , city = 'ddn' , martial_status = 'u' , occupation = 'none' , dob = '1986-09-04' where patient_id = 1; 


update anand_patient_info set patient_id = '1' , name = 'sarv' , gender = 'g' , age = '10' , contact_no = '8297192121' , address = 'ajab coloney
near sabji mandi
ajabpur
' , city = 'ddn' , martial_status = 'u' , occupation = 'none' , dob = '1986-09-04' where patient_id = 1; 

show tables;
select * from anand_medical_record;

alter table anand_medical_record add amount varchar(50) ;

alter table anand_medical_record modify patient_id int;

 SELECT LAST_INSERT_ID();
 
select * from anand_patient_info where patient_id=(SELECT LAST_INSERT_ID());
 
select * from anand_patient_info;

delete from doctor_info where name = 'Anand malhotra';
-- drop table dranand_patient_info;
-- drop table dranand_medical_record;

select * from docspace.doctor_info;
select * from docspace.dranand_patient_info;

create table ds1_patient_info(
							patient_id varchar(64) not null primary key,
							name varchar(20) not null,
							gender varchar(1) not null,
                            age int not null,
							contact_no varchar(12) not null,
							address varchar(50) not null,
                            city varchar(10) not null,
                            maritial_status varchar(1),
                            occupation varchar(20) not null,
                            dob date not null
							);

create table test( remedy_name varchar(50) not null,
					description1 text(65535),
					description2 text(65535));
show tables;

create table ds1_patient_medical_record(
							patient_id varchar(64) not null,
                            record_date date not null,
                            case_type varchar(2) not null,
                            symtoms varchar(50) not null,
                            symtoms_agg_by varchar(50) not null,
                            symtoms_ameol_by varchar(50) not null,
                            symtoms_since varchar(50) not null,
                            present_complains varchar(50) not null,
                            appetite varchar(50) not null,
                            thirst varchar(50) not null,
                            urine varchar(50) not null,
                            stool varchar(50) not null,
                            sleep varchar(50) not null,
                            perspiration varchar(50) not null,
                            addiction varchar(50) not null,
                            desires varchar(50) not null,
                            aversions varchar(50) not null,
                            thermal_reaction varchar(50) not null,
                            allergy varchar(50) not null,
                            mental_symtoms varchar(50) not null,
                            back varchar(50) not null,
                            chest varchar(50) not null,
                            ear varchar(50) not null,
                            eye varchar(50) not null,
                            face varchar(50) not null,
                            head varchar(50) not null,
                            lips varchar(50) not null,
                            mouth varchar(50) not null,
                            nose varchar(50) not null,
                            teeth varchar(50) not null,
                            throat varchar(50) not null,
                            tongue varchar(50) not null,
                            past_history varchar(50) not null,
                            family_history varchar(50) not null,
                            menstrual_history varchar(50) not null,
                            Investigation varchar(50) not null,
                            medicine varchar(160) not null,
                            dose varchar(100) not null,
                            potency varchar(80) not null,
                            days varchar(80) not null,
                            next_visit_date date not null,
                            primary key (patient_id, record_date)
							);

create table test_patient_info(
							patient_id int not null primary key auto_increment,
							name varchar(20) not null,
							gender varchar(1) not null,
                            age int not null,
							contact_no varchar(12) not null,
							address varchar(50) not null,
                            city varchar(10) not null,
                            maritial_status varchar(1),
                            occupation varchar(20) not null,
                            dob date not null
							);
                            
SELECT * FROM docspace.ansarigupta100_medical_record_file_i ORDER BY creation_date LIMIT 1;
select * from docspace.doctor_info;
show index from docspace.ansarigupta100_medical_record_file_i;
show index from docspace.ansarigupta100_medical_record;
show index from docspace.test_doctor_info_file_i;
show index from docspace.ansarigupta100_medical_record_file_i;
create table test_doctor_info_file_i(
							file_name char(20) not null primary key,
                            creation_date date not null,
                            is_backed_up bool not null,
                            back_up_creation_date_time date,
                            file_size int,
                            index (creation_date));
                            
create table anand_medical_record_file_i(
							file_name char(20) not null primary key,
                            creation_date date not null,
                            is_backed_up bool not null,
                            back_up_creation_date_time date,
                            file_size int,
                            index (creation_date));                            
                            
create table anand_patient_info_file_i(
							file_name char(20) not null primary key,
                            creation_date date not null,
                            is_backed_up bool not null,
                            back_up_creation_date_time date,
                            file_size int,
                            index (creation_date));
select * from doctor_info;


select * from DocSpace.ansari_gupta100_patient_info_file_i;
select last_insert_id();
select * from DocSpace.ansari_gupta100_patient_info_file_i where insert_id = ( select last_insert_id() );

select * from DocSpace.ansari_gupta100_patient_info_file_i where insert_id=(select MAX(insert_id) from DocSpace.ansari_gupta100_patient_info_file_i);

-- Create Remedy Database
-- This Database will be used to store the remedy information, which is like medicine name and then all the symtoms
-- of the medicine
-- It will also contain the repositories which is like symtoms and the medicine name.

create database avRemedyDb;
use  avRemedyDb;
show tables;

select * from _en_materia_medica_james_tyler_kent_index;

select * from avRemedyDb._en_materia_medica_adolf_zur_lippe_index where remedyName like ('%tinnitus%') or Description_1 like ('%tinnitus%') or Description_2 like ('%tinnitus%') or Description_3 like ('%tinnitus%') or Description_4 like ('%tinnitus%') or Description_5 like ('%tinnitus%') or Description_6 like ('%tinnitus%') or Description_7 like ('%tinnitus%') or Description_8 like ('%tinnitus%') or Description_9 like ('%tinnitus%') or Description_10 like ('%tinnitus%') or Description_11 like ('%tinnitus%') or Description_12 like ('%tinnitus%') or Description_13 like ('%tinnitus%') or Description_14 like ('%tinnitus%') or Description_15 like ('%tinnitus%') or Description_16 like ('%tinnitus%') or Description_17 like ('%tinnitus%') or Description_18 like ('%tinnitus%') or Description_19 like ('%tinnitus%') or Description_20 like ('%tinnitus%') or Description_21 like ('%tinnitus%') or Description_22 like ('%tinnitus%') or Description_23 like ('%tinnitus%') or Description_24 like ('%tinnitus%') or Description_25 like ('%tinnitus%') or Description_26 like ('%tinnitus%') or Description_27 like ('%tinnitus%') or Description_28 like ('%tinnitus%') or Description_29 like ('%tinnitus%') or Description_30 like ('%tinnitus%') or Description_31 like ('%tinnitus%') or Description_32 like ('%tinnitus%') or Description_33 like ('%tinnitus%') or Description_34 like ('%tinnitus%') or Description_35 like ('%tinnitus%') or Description_36 like ('%tinnitus%') or Description_37 like ('%tinnitus%') or Description_38 like ('%tinnitus%') or Description_39 like ('%tinnitus%') or Description_40 like ('%tinnitus%') or Description_41 like ('%tinnitus%') or Description_42 like ('%tinnitus%') or Description_43 like ('%tinnitus%') or Description_44 like ('%tinnitus%') or Description_45 like ('%tinnitus%') or Description_46 like ('%tinnitus%') or Description_47 like ('%tinnitus%') or Description_48 like ('%tinnitus%') or Description_49 like ('%tinnitus%') or Description_50 like ('%tinnitus%') or Description_51 like ('%tinnitus%') or Description_52 like ('%tinnitus%') or Description_53 like ('%tinnitus%') or Description_54 like ('%tinnitus%') or Description_55 like ('%tinnitus%') or Description_56 like ('%tinnitus%') or Description_57 like ('%tinnitus%') or Description_58 like ('%tinnitus%') or Description_59 like ('%tinnitus%') or Description_60 like ('%tinnitus%') or Description_61 like ('%tinnitus%') or Description_62 like ('%tinnitus%') or Description_63 like ('%tinnitus%') or Description_64 like ('%tinnitus%') or Description_65 like ('%tinnitus%') or Description_66 like ('%tinnitus%') or Description_67 like ('%tinnitus%') or Description_68 like ('%tinnitus%') or Description_69 like ('%tinnitus%') or Description_70 like ('%tinnitus%') or Description_71 like ('%tinnitus%') or Description_72 like ('%tinnitus%') or Description_73 like ('%tinnitus%') or Description_74 like ('%tinnitus%') or Description_75 like ('%tinnitus%') or Description_76 like ('%tinnitus%') or Description_77 like ('%tinnitus%') or Description_78 like ('%tinnitus%') or Description_79 like ('%tinnitus%') or Description_80 like ('%tinnitus%') or Description_81 like ('%tinnitus%') or Description_82 like ('%tinnitus%') or Description_83 like ('%tinnitus%') or Description_84 like ('%tinnitus%') or Description_85 like ('%tinnitus%') or Description_86 like ('%tinnitus%') or Description_87 like ('%tinnitus%') or Description_88 like ('%tinnitus%') or Description_89 like ('%tinnitus%') or Description_90 like ('%tinnitus%') or Description_91 like ('%tinnitus%') or Description_92 like ('%tinnitus%') or Description_93 like ('%tinnitus%') or Description_94 like ('%tinnitus%') or Description_95 like ('%tinnitus%') or Description_96 like ('%tinnitus%') or Description_97 like ('%tinnitus%') or Description_98 like ('%tinnitus%') or Description_99 like ('%tinnitus%') or Description_100 like ('%tinnitus%') or Description_101 like ('%tinnitus%') or Description_102 like ('%tinnitus%') or Description_103 like ('%tinnitus%') or Description_104 like ('%tinnitus%') or Description_105 like ('%tinnitus%') or Description_106 like ('%tinnitus%') or Description_107 like ('%tinnitus%') or Description_108 like ('%tinnitus%') or Description_109 like ('%tinnitus%') or Description_110 like ('%tinnitus%') or Description_111 like ('%tinnitus%') or Description_112 like ('%tinnitus%') or Description_113 like ('%tinnitus%') or Description_114 like ('%tinnitus%') or Description_115 like ('%tinnitus%') or Description_116 like ('%tinnitus%') or Description_117 like ('%tinnitus%') or Description_118 like ('%tinnitus%') or Description_119 like ('%tinnitus%');  where params  [('remedyName', 'tinnitus'), ('Description_1', 'tinnitus'), ('Description_2', 'tinnitus'), ('Description_3', 'tinnitus'), ('Description_4', 'tinnitus'), ('Description_5', 'tinnitus'), ('Description_6', 'tinnitus'), ('Description_7', 'tinnitus'), ('Description_8', 'tinnitus'), ('Description_9', 'tinnitus'), ('Description_10', 'tinnitus'), ('Description_11', 'tinnitus'), ('Description_12', 'tinnitus'), ('Description_13', 'tinnitus'), ('Description_14', 'tinnitus'), ('Description_15', 'tinnitus'), ('Description_16', 'tinnitus'), ('Description_17', 'tinnitus'), ('Description_18', 'tinnitus'), ('Description_19', 'tinnitus'), ('Description_20', 'tinnitus'), ('Description_21', 'tinnitus'), ('Description_22', 'tinnitus'), ('Description_23', 'tinnitus'), ('Description_24', 'tinnitus'), ('Description_25', 'tinnitus'), ('Description_26', 'tinnitus'), ('Description_27', 'tinnitus'), ('Description_28', 'tinnitus'), ('Description_29', 'tinnitus'), ('Description_30', 'tinnitus'), ('Description_31', 'tinnitus'), ('Description_32', 'tinnitus'), ('Description_33', 'tinnitus'), ('Description_34', 'tinnitus'), ('Description_35', 'tinnitus'), ('Description_36', 'tinnitus'), ('Description_37', 'tinnitus'), ('Description_38', 'tinnitus'), ('Description_39', 'tinnitus'), ('Description_40', 'tinnitus'), ('Description_41', 'tinnitus'), ('Description_42', 'tinnitus'), ('Description_43', 'tinnitus'), ('Description_44', 'tinnitus'), ('Description_45', 'tinnitus'), ('Description_46', 'tinnitus'), ('Description_47', 'tinnitus'), ('Description_48', 'tinnitus'), ('Description_49', 'tinnitus'), ('Description_50', 'tinnitus'), ('Description_51', 'tinnitus'), ('Description_52', 'tinnitus'), ('Description_53', 'tinnitus'), ('Description_54', 'tinnitus'), ('Description_55', 'tinnitus'), ('Description_56', 'tinnitus'), ('Description_57', 'tinnitus'), ('Description_58', 'tinnitus'), ('Description_59', 'tinnitus'), ('Description_60', 'tinnitus'), ('Description_61', 'tinnitus'), ('Description_62', 'tinnitus'), ('Description_63', 'tinnitus'), ('Description_64', 'tinnitus'), ('Description_65', 'tinnitus'), ('Description_66', 'tinnitus'), ('Description_67', 'tinnitus'), ('Description_68', 'tinnitus'), ('Description_69', 'tinnitus'), ('Description_70', 'tinnitus'), ('Description_71', 'tinnitus'), ('Description_72', 'tinnitus'), ('Description_73', 'tinnitus'), ('Description_74', 'tinnitus'), ('Description_75', 'tinnitus'), ('Description_76', 'tinnitus'), ('Description_77', 'tinnitus'), ('Description_78', 'tinnitus'), ('Description_79', 'tinnitus'), ('Description_80', 'tinnitus'), ('Description_81', 'tinnitus'), ('Description_82', 'tinnitus'), ('Description_83', 'tinnitus'), ('Description_84', 'tinnitus'), ('Description_85', 'tinnitus'), ('Description_86', 'tinnitus'), ('Description_87', 'tinnitus'), ('Description_88', 'tinnitus'), ('Description_89', 'tinnitus'), ('Description_90', 'tinnitus'), ('Description_91', 'tinnitus'), ('Description_92', 'tinnitus'), ('Description_93', 'tinnitus'), ('Description_94', 'tinnitus'), ('Description_95', 'tinnitus'), ('Description_96', 'tinnitus'), ('Description_97', 'tinnitus'), ('Description_98', 'tinnitus'), ('Description_99', 'tinnitus'), ('Description_100', 'tinnitus'), ('Description_101', 'tinnitus'), ('Description_102', 'tinnitus'), ('Description_103', 'tinnitus'), ('Description_104', 'tinnitus'), ('Description_105', 'tinnitus'), ('Description_106', 'tinnitus'), ('Description_107', 'tinnitus'), ('Description_108', 'tinnitus'), ('Description_109', 'tinnitus'), ('Description_110', 'tinnitus'), ('Description_111', 'tinnitus'), ('Description_112', 'tinnitus'), ('Description_113', 'tinnitus'), ('Description_114', 'tinnitus'), ('Description_115', 'tinnitus'), ('Description_116', 'tinnitus'), ('Description_117', 'tinnitus'), ('Description_118', 'tinnitus'), ('Description_119', 'tinnitus')]

sql  select * from avRemedyDb._en_materia_medica_adolf_zur_lippe_index where remedyName like ('%tinnitus%') or Description_1 like ('%tinnitus%') or Description_2 like ('%tinnitus%') or Description_3 like ('%tinnitus%') or Description_4 like ('%tinnitus%') or Description_5 like ('%tinnitus%') or Description_6 like ('%tinnitus%') or Description_7 like ('%tinnitus%') or Description_8 like ('%tinnitus%') or Description_9 like ('%tinnitus%') or Description_10 like ('%tinnitus%') or Description_11 like ('%tinnitus%') or Description_12 like ('%tinnitus%') or Description_13 like ('%tinnitus%') or Description_14 like ('%tinnitus%') or Description_15 like ('%tinnitus%') or Description_16 like ('%tinnitus%') or Description_17 like ('%tinnitus%') or Description_18 like ('%tinnitus%') or Description_19 like ('%tinnitus%') or Description_20 like ('%tinnitus%') or Description_21 like ('%tinnitus%') or Description_22 like ('%tinnitus%') or Description_23 like ('%tinnitus%') or Description_24 like ('%tinnitus%') or Description_25 like ('%tinnitus%') or Description_26 like ('%tinnitus%') or Description_27 like ('%tinnitus%') or Description_28 like ('%tinnitus%') or Description_29 like ('%tinnitus%') or Description_30 like ('%tinnitus%') or Description_31 like ('%tinnitus%') or Description_32 like ('%tinnitus%') or Description_33 like ('%tinnitus%') or Description_34 like ('%tinnitus%') or Description_35 like ('%tinnitus%') or Description_36 like ('%tinnitus%') or Description_37 like ('%tinnitus%') or Description_38 like ('%tinnitus%') or Description_39 like ('%tinnitus%') or Description_40 like ('%tinnitus%') or Description_41 like ('%tinnitus%') or Description_42 like ('%tinnitus%') or Description_43 like ('%tinnitus%') or Description_44 like ('%tinnitus%') or Description_45 like ('%tinnitus%') or Description_46 like ('%tinnitus%') or Description_47 like ('%tinnitus%') or Description_48 like ('%tinnitus%') or Description_49 like ('%tinnitus%') or Description_50 like ('%tinnitus%') or Description_51 like ('%tinnitus%') or Description_52 like ('%tinnitus%') or Description_53 like ('%tinnitus%') or Description_54 like ('%tinnitus%') or Description_55 like ('%tinnitus%') or Description_56 like ('%tinnitus%') or Description_57 like ('%tinnitus%') or Description_58 like ('%tinnitus%') or Description_59 like ('%tinnitus%') or Description_60 like ('%tinnitus%') or Description_61 like ('%tinnitus%') or Description_62 like ('%tinnitus%') or Description_63 like ('%tinnitus%') or Description_64 like ('%tinnitus%') or Description_65 like ('%tinnitus%') or Description_66 like ('%tinnitus%') or Description_67 like ('%tinnitus%') or Description_68 like ('%tinnitus%') or Description_69 like ('%tinnitus%') or Description_70 like ('%tinnitus%') or Description_71 like ('%tinnitus%') or Description_72 like ('%tinnitus%') or Description_73 like ('%tinnitus%') or Description_74 like ('%tinnitus%') or Description_75 like ('%tinnitus%') or Description_76 like ('%tinnitus%') or Description_77 like ('%tinnitus%') or Description_78 like ('%tinnitus%') or Description_79 like ('%tinnitus%') or Description_80 like ('%tinnitus%') or Description_81 like ('%tinnitus%') or Description_82 like ('%tinnitus%') or Description_83 like ('%tinnitus%') or Description_84 like ('%tinnitus%') or Description_85 like ('%tinnitus%') or Description_86 like ('%tinnitus%') or Description_87 like ('%tinnitus%') or Description_88 like ('%tinnitus%') or Description_89 like ('%tinnitus%') or Description_90 like ('%tinnitus%') or Description_91 like ('%tinnitus%') or Description_92 like ('%tinnitus%') or Description_93 like ('%tinnitus%') or Description_94 like ('%tinnitus%') or Description_95 like ('%tinnitus%') or Description_96 like ('%tinnitus%') or Description_97 like ('%tinnitus%') or Description_98 like ('%tinnitus%') or Description_99 like ('%tinnitus%') or Description_100 like ('%tinnitus%') or Description_101 like ('%tinnitus%') or Description_102 like ('%tinnitus%') or Description_103 like ('%tinnitus%') or Description_104 like ('%tinnitus%') or Description_105 like ('%tinnitus%') or Description_106 like ('%tinnitus%') or Description_107 like ('%tinnitus%') or Description_108 like ('%tinnitus%') or Description_109 like ('%tinnitus%') or Description_110 like ('%tinnitus%') or Description_111 like ('%tinnitus%') or Description_112 like ('%tinnitus%') or Description_113 like ('%tinnitus%') or Description_114 like ('%tinnitus%') or Description_115 like ('%tinnitus%') or Description_116 like ('%tinnitus%') or Description_117 like ('%tinnitus%') or Description_118 like ('%tinnitus%') or Description_119 like ('%tinnitus%');  where params  [('remedyName', 'tinnitus'), ('Description_1', 'tinnitus'), ('Description_2', 'tinnitus'), ('Description_3', 'tinnitus'), ('Description_4', 'tinnitus'), ('Description_5', 'tinnitus'), ('Description_6', 'tinnitus'), ('Description_7', 'tinnitus'), ('Description_8', 'tinnitus'), ('Description_9', 'tinnitus'), ('Description_10', 'tinnitus'), ('Description_11', 'tinnitus'), ('Description_12', 'tinnitus'), ('Description_13', 'tinnitus'), ('Description_14', 'tinnitus'), ('Description_15', 'tinnitus'), ('Description_16', 'tinnitus'), ('Description_17', 'tinnitus'), ('Description_18', 'tinnitus'), ('Description_19', 'tinnitus'), ('Description_20', 'tinnitus'), ('Description_21', 'tinnitus'), ('Description_22', 'tinnitus'), ('Description_23', 'tinnitus'), ('Description_24', 'tinnitus'), ('Description_25', 'tinnitus'), ('Description_26', 'tinnitus'), ('Description_27', 'tinnitus'), ('Description_28', 'tinnitus'), ('Description_29', 'tinnitus'), ('Description_30', 'tinnitus'), ('Description_31', 'tinnitus'), ('Description_32', 'tinnitus'), ('Description_33', 'tinnitus'), ('Description_34', 'tinnitus'), ('Description_35', 'tinnitus'), ('Description_36', 'tinnitus'), ('Description_37', 'tinnitus'), ('Description_38', 'tinnitus'), ('Description_39', 'tinnitus'), ('Description_40', 'tinnitus'), ('Description_41', 'tinnitus'), ('Description_42', 'tinnitus'), ('Description_43', 'tinnitus'), ('Description_44', 'tinnitus'), ('Description_45', 'tinnitus'), ('Description_46', 'tinnitus'), ('Description_47', 'tinnitus'), ('Description_48', 'tinnitus'), ('Description_49', 'tinnitus'), ('Description_50', 'tinnitus'), ('Description_51', 'tinnitus'), ('Description_52', 'tinnitus'), ('Description_53', 'tinnitus'), ('Description_54', 'tinnitus'), ('Description_55', 'tinnitus'), ('Description_56', 'tinnitus'), ('Description_57', 'tinnitus'), ('Description_58', 'tinnitus'), ('Description_59', 'tinnitus'), ('Description_60', 'tinnitus'), ('Description_61', 'tinnitus'), ('Description_62', 'tinnitus'), ('Description_63', 'tinnitus'), ('Description_64', 'tinnitus'), ('Description_65', 'tinnitus'), ('Description_66', 'tinnitus'), ('Description_67', 'tinnitus'), ('Description_68', 'tinnitus'), ('Description_69', 'tinnitus'), ('Description_70', 'tinnitus'), ('Description_71', 'tinnitus'), ('Description_72', 'tinnitus'), ('Description_73', 'tinnitus'), ('Description_74', 'tinnitus'), ('Description_75', 'tinnitus'), ('Description_76', 'tinnitus'), ('Description_77', 'tinnitus'), ('Description_78', 'tinnitus'), ('Description_79', 'tinnitus'), ('Description_80', 'tinnitus'), ('Description_81', 'tinnitus'), ('Description_82', 'tinnitus'), ('Description_83', 'tinnitus'), ('Description_84', 'tinnitus'), ('Description_85', 'tinnitus'), ('Description_86', 'tinnitus'), ('Description_87', 'tinnitus'), ('Description_88', 'tinnitus'), ('Description_89', 'tinnitus'), ('Description_90', 'tinnitus'), ('Description_91', 'tinnitus'), ('Description_92', 'tinnitus'), ('Description_93', 'tinnitus'), ('Description_94', 'tinnitus'), ('Description_95', 'tinnitus'), ('Description_96', 'tinnitus'), ('Description_97', 'tinnitus'), ('Description_98', 'tinnitus'), ('Description_99', 'tinnitus'), ('Description_100', 'tinnitus'), ('Description_101', 'tinnitus'), ('Description_102', 'tinnitus'), ('Description_103', 'tinnitus'), ('Description_104', 'tinnitus'), ('Description_105', 'tinnitus'), ('Description_106', 'tinnitus'), ('Description_107', 'tinnitus'), ('Description_108', 'tinnitus'), ('Description_109', 'tinnitus'), ('Description_110', 'tinnitus'), ('Description_111', 'tinnitus'), ('Description_112', 'tinnitus'), ('Description_113', 'tinnitus'), ('Description_114', 'tinnitus'), ('Description_115', 'tinnitus'), ('Description_116', 'tinnitus'), ('Description_117', 'tinnitus'), ('Description_118', 'tinnitus'), ('Description_119', 'tinnitus')]

create table avRemedyDb._en_materia_medica_william_boericke_index (remedyName text(65535)  , Description 1 text(65535)  , Description 2 text(65535)  , Description 3 text(65535)  , Description 4 text(65535)  , Description 5 text(65535)  , Description 6 text(65535)  , Description 7 text(65535)  , Description 8 text(65535)  , Description 9 text(65535)  , Description 10 text(65535)  , Description 11 text(65535)  , Description 12 text(65535)  , Description 13 text(65535)  , Description 14 text(65535)  , Description 15 text(65535)  , Description 16 text(65535)  , Description 17 text(65535)  , Description 18 text(65535)  , Description 19 text(65535)  , Description 20 text(65535)  , Description 21 text(65535)  , Description 22 text(65535)  , Description 23 text(65535)  , Description 24 text(65535)  , Description 25 text(65535)  , Description 26 text(65535)  , Description 27 text(65535)  , Description 28 text(65535)  , Description 29 text(65535)  , Description 30 text(65535)  , Description 31 text(65535)  , Description 32 text(65535)  , Description 33 text(65535)  , Description 34 text(65535)  , Description 35 text(65535)  , Description 36 text(65535)  , Description 37 text(65535)  , Description 38 text(65535)  , Description 39 text(65535)  , Description 40 text(65535)  , Description 41 text(65535)  , Description 42 text(65535)  , Description 43 text(65535)  , Description 44 text(65535)  , Description 45 text(65535)  , Description 46 text(65535)  , Description 47 text(65535)  , Description 48 text(65535)  , Description 49 text(65535)  , Description 50 text(65535)  , Description 51 text(65535)  , Description 52 text(65535)  , Description 53 text(65535)  , Description 54 text(65535)  , Description 55 text(65535)  , Description 56 text(65535)  , Description 57 text(65535)  , Description 58 text(65535)  , Description 59 text(65535)  , Description 60 text(65535)  , Description 61 text(65535)  , Description 62 text(65535)  , Description 63 text(65535)  , Description 64 text(65535)  , Description 65 text(65535)  , Description 66 text(65535)  , Description 67 text(65535)  , Description 68 text(65535)  , Description 69 text(65535)  , Description 70 text(65535)  , Description 71 text(65535)  , Description 72 text(65535)  , Description 73 text(65535) );

select * from avRemedyDb._en_materia_medica_william_boericke_index where remedyName like ('%tinnitus%') or Description_1 like ('%tinnitus%')  or Description_2 like ('%tinnitus%') or Description_3 like ('%tinnitus%') or Description_4 like ('%tinnitus%') or Description_5 like ('%tinnitus%') or Description_6 like ('%tinnitus%') or Description_7 like ('%tinnitus%') or Description_8 like ('%tinnitus%') or Description_9 like ('%tinnitus%') or Description_10 like ('%tinnitus%') or Description_11 like ('%tinnitus%') or Description_12 like ('%tinnitus%') or Description_13 like ('%tinnitus%') or Description_14 like ('%tinnitus%') or Description_15 like ('%tinnitus%') or Description_16 like ('%tinnitus%') or Description_17 like ('%tinnitus%') or Description_18 like ('%tinnitus%') or Description_19 like ('%tinnitus%') or Description_20 like ('%tinnitus%') or Description_21 like ('%tinnitus%') or Description_22 like ('%tinnitus%') or Description_23 like ('%tinnitus%') or Description_24 like ('%tinnitus%') or Description_25 like ('%tinnitus%') or Description_26 like ('%tinnitus%') or Description_27 like ('%tinnitus%') or Description_28 like ('%tinnitus%') or Description_29 like ('%tinnitus%') or Description_30 like ('%tinnitus%') or Description_31 like ('%tinnitus%') or Description_32 like ('%tinnitus%');  where params  [('remedyName', 'tinnitus'), ('Description_1', 'tinnitus'), ('Description_2', 'tinnitus'), ('Description_3', 'tinnitus'), ('Description_4', 'tinnitus'), ('Description_5', 'tinnitus'), ('Description_6', 'tinnitus'), ('Description_7', 'tinnitus'), ('Description_8', 'tinnitus'), ('Description_9', 'tinnitus'), ('Description_10', 'tinnitus'), ('Description_11', 'tinnitus'), ('Description_12', 'tinnitus'), ('Description_13', 'tinnitus'), ('Description_14', 'tinnitus'), ('Description_15', 'tinnitus'), ('Description_16', 'tinnitus'), ('Description_17', 'tinnitus'), ('Description_18', 'tinnitus'), ('Description_19', 'tinnitus'), ('Description_20', 'tinnitus'), ('Description_21', 'tinnitus'), ('Description_22', 'tinnitus'), ('Description_23', 'tinnitus'), ('Description_24', 'tinnitus'), ('Description_25', 'tinnitus'), ('Description_26', 'tinnitus'), ('Description_27', 'tinnitus'), ('Description_28', 'tinnitus'), ('Description_29', 'tinnitus'), ('Description_30', 'tinnitus'), ('Description_31', 'tinnitus'), ('Description_32', 'tinnitus')]

select * from _en_materia_medica_william_boericke_index;
select * from _en_materia_medica_william_boericke_index where
				Description_1 like ('%tinnitus%') ;
                
select * from _en_materia_medica_adolf_zur_lippe_index where
				Description_1 like ('%tinnitus%') ;
                


describe _en_materia_medica_william_boericke_index;