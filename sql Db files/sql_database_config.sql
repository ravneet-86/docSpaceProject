-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: docSpace
-- ------------------------------------------------------
-- Server version	8.0.26

-- Create Main DataBase file

-- drop database DocSpace;

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
							clinic_address varchar(50) not null
							);

select * from DocSpace.doctor_info;

insert into DocSpace.doctor_info (name, email, password, contact_no, mobile_no, clinic_name, clinic_address) values
("Ravneet Singh", "ravne1986@gmail.com", "megadeth", "8297192121", "8297192121", "Homeopathy", "Dehradun");

insert into DocSpace.doctor_info (name, email, password, contact_no, mobile_no, clinic_name, clinic_address) values
("ravneet", "r@gmail.com", "m", "8297192121", "8297192121", "Homeopathy", "Dehradun");

insert into DocSpace.anand_patient_info (name,gender, age,contact_no, address,city,martial_status,occupation,dob) values
("ra", "g", "10", "8297192121", "DDN", "ddn","u", "none", "STR_TO_DATE('04-09-1986', '%d-%m-%Y')");

select * from anand_patient_info where na
me = 'r%';


select * from anand_patient_info;
show tables;
select * from anand_patient_info;
delete from doctor_info where name = 'Anand malhotra';
drop table dranand_patient_info;
drop table dranand_medical_record;

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