-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: docSpace
-- ------------------------------------------------------
-- Server version	8.0.26

-- Create Main DataBase file

-- drop database DocSpace;

select * from reception.userInfo;
create database DocSpace;

use DocSpace;

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

create table doctor_info_file_i(
							insert_id int not null primary key auto_increment,
							file_name char(20) not null primary key,
                            creation_date date not null,
                            is_backed_up bool not null,
                            back_up_creation_date_time date,
                            file_size int,
                            index (creation_date));
                            

select * from DocSpace.doctor_info;

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