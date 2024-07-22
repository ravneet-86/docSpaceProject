-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: DocSpace
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `a_joshi_medical_record`
--

DROP TABLE IF EXISTS `a_joshi_medical_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `a_joshi_medical_record` (
  `patient_id` int NOT NULL,
  `record_date` date NOT NULL,
  `case_type` varchar(2) NOT NULL,
  `symptoms` varchar(200) NOT NULL,
  `symptoms_agg_by` varchar(100) NOT NULL,
  `symptoms_ameol_by` varchar(50) NOT NULL,
  `symptoms_since` varchar(50) NOT NULL,
  `present_complains` varchar(200) NOT NULL,
  `appetite` varchar(50) NOT NULL,
  `thirst` varchar(50) NOT NULL,
  `urine` varchar(50) NOT NULL,
  `stool` varchar(50) NOT NULL,
  `sleep` varchar(50) NOT NULL,
  `perspiration` varchar(50) NOT NULL,
  `addiction` varchar(50) NOT NULL,
  `desires` varchar(50) NOT NULL,
  `aversions` varchar(50) NOT NULL,
  `thermal_reaction` varchar(50) NOT NULL,
  `allergy` varchar(50) NOT NULL,
  `mental_symptoms` varchar(50) NOT NULL,
  `back` varchar(50) NOT NULL,
  `chest` varchar(50) NOT NULL,
  `ear` varchar(50) NOT NULL,
  `eye` varchar(50) NOT NULL,
  `face` varchar(50) NOT NULL,
  `head` varchar(50) NOT NULL,
  `lips` varchar(50) NOT NULL,
  `mouth` varchar(50) NOT NULL,
  `nose` varchar(50) NOT NULL,
  `teeth` varchar(50) NOT NULL,
  `throat` varchar(50) NOT NULL,
  `tongue` varchar(50) NOT NULL,
  `past_history` varchar(50) NOT NULL,
  `family_history` varchar(50) NOT NULL,
  `menstrual_history` varchar(50) NOT NULL,
  `Investigation` varchar(200) NOT NULL,
  `medicine` varchar(160) NOT NULL,
  `dose` varchar(100) NOT NULL,
  `potency` varchar(80) NOT NULL,
  `days` varchar(80) NOT NULL,
  `next_visit_date` date NOT NULL,
  `amount` varchar(80) NOT NULL,
  PRIMARY KEY (`patient_id`,`record_date`),
  KEY `patient_id` (`patient_id`,`record_date`,`symptoms`,`Investigation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `a_joshi_medical_record`
--

LOCK TABLES `a_joshi_medical_record` WRITE;
/*!40000 ALTER TABLE `a_joshi_medical_record` DISABLE KEYS */;
INSERT INTO `a_joshi_medical_record` VALUES (1,'2022-04-08','','pain','','','20 days','','','','','','','','','','','','','','pain','heavy','','','','','','','','','','','','','','back and chest pain','tumani|m12||||||','1|2||||||','30|30||||||','30 days|2 d ays||||||','2022-04-23','100|130||||||');
/*!40000 ALTER TABLE `a_joshi_medical_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `a_joshi_medical_record_file_i`
--

DROP TABLE IF EXISTS `a_joshi_medical_record_file_i`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `a_joshi_medical_record_file_i` (
  `insert_id` int NOT NULL AUTO_INCREMENT,
  `file_name` char(200) NOT NULL,
  `creation_date` date NOT NULL,
  `is_backed_up` tinyint(1) NOT NULL,
  `back_up_creation_date_time` date DEFAULT NULL,
  `file_size` int DEFAULT NULL,
  PRIMARY KEY (`insert_id`),
  KEY `insert_id` (`insert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `a_joshi_medical_record_file_i`
--

LOCK TABLES `a_joshi_medical_record_file_i` WRITE;
/*!40000 ALTER TABLE `a_joshi_medical_record_file_i` DISABLE KEYS */;
INSERT INTO `a_joshi_medical_record_file_i` VALUES (1,'a_joshi_medical_record_file_i_2022-04-08-10-24-12.csv','2022-04-08',0,NULL,NULL);
/*!40000 ALTER TABLE `a_joshi_medical_record_file_i` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `a_joshi_patient_info`
--

DROP TABLE IF EXISTS `a_joshi_patient_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `a_joshi_patient_info` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `age` int NOT NULL,
  `contact_no` varchar(12) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(10) NOT NULL,
  `martial_status` varchar(10) NOT NULL,
  `occupation` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  PRIMARY KEY (`patient_id`),
  KEY `name` (`name`,`city`,`occupation`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `a_joshi_patient_info`
--

LOCK TABLES `a_joshi_patient_info` WRITE;
/*!40000 ALTER TABLE `a_joshi_patient_info` DISABLE KEYS */;
INSERT INTO `a_joshi_patient_info` VALUES (1,'divya','female',23,'','','','unmarried','student','2022-12-04');
/*!40000 ALTER TABLE `a_joshi_patient_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `a_joshi_patient_info_file_i`
--

DROP TABLE IF EXISTS `a_joshi_patient_info_file_i`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `a_joshi_patient_info_file_i` (
  `insert_id` int NOT NULL AUTO_INCREMENT,
  `file_name` char(200) NOT NULL,
  `creation_date` date NOT NULL,
  `is_backed_up` tinyint(1) NOT NULL,
  `back_up_creation_date_time` date DEFAULT NULL,
  `file_size` int DEFAULT NULL,
  PRIMARY KEY (`insert_id`),
  KEY `insert_id` (`insert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `a_joshi_patient_info_file_i`
--

LOCK TABLES `a_joshi_patient_info_file_i` WRITE;
/*!40000 ALTER TABLE `a_joshi_patient_info_file_i` DISABLE KEYS */;
INSERT INTO `a_joshi_patient_info_file_i` VALUES (1,'a_joshi_patient_info_file_i_2022-04-08-10-24-12.csv','2022-04-08',0,NULL,NULL);
/*!40000 ALTER TABLE `a_joshi_patient_info_file_i` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anand_medical_record`
--

DROP TABLE IF EXISTS `anand_medical_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `anand_medical_record` (
  `patient_id` int NOT NULL,
  `record_date` date NOT NULL,
  `case_type` varchar(2) NOT NULL,
  `symptoms` varchar(50) NOT NULL,
  `symptoms_agg_by` varchar(50) NOT NULL,
  `symptoms_ameol_by` varchar(50) NOT NULL,
  `symptoms_since` varchar(50) NOT NULL,
  `present_complains` varchar(50) NOT NULL,
  `appetite` varchar(50) NOT NULL,
  `thirst` varchar(50) NOT NULL,
  `urine` varchar(50) NOT NULL,
  `stool` varchar(50) NOT NULL,
  `sleep` varchar(50) NOT NULL,
  `perspiration` varchar(50) NOT NULL,
  `addiction` varchar(50) NOT NULL,
  `desires` varchar(50) NOT NULL,
  `aversions` varchar(50) NOT NULL,
  `thermal_reaction` varchar(50) NOT NULL,
  `allergy` varchar(50) NOT NULL,
  `mental_symptoms` varchar(50) NOT NULL,
  `back` varchar(50) NOT NULL,
  `chest` varchar(50) NOT NULL,
  `ear` varchar(50) NOT NULL,
  `eye` varchar(50) NOT NULL,
  `face` varchar(50) NOT NULL,
  `head` varchar(50) NOT NULL,
  `lips` varchar(50) NOT NULL,
  `mouth` varchar(50) NOT NULL,
  `nose` varchar(50) NOT NULL,
  `teeth` varchar(50) NOT NULL,
  `throat` varchar(50) NOT NULL,
  `tongue` varchar(50) NOT NULL,
  `past_history` varchar(50) NOT NULL,
  `family_history` varchar(50) NOT NULL,
  `menstrual_history` varchar(50) NOT NULL,
  `Investigation` varchar(50) NOT NULL,
  `medicine` varchar(160) NOT NULL,
  `dose` varchar(100) NOT NULL,
  `potency` varchar(80) NOT NULL,
  `days` varchar(80) NOT NULL,
  `next_visit_date` date NOT NULL,
  `amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`patient_id`,`record_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anand_medical_record`
--

LOCK TABLES `anand_medical_record` WRITE;
/*!40000 ALTER TABLE `anand_medical_record` DISABLE KEYS */;
INSERT INTO `anand_medical_record` VALUES (1,'2022-03-13','2','stress, numbness and pain','10','','6 months','stress, numb','','','','','distrubed','','','','','','','','pain','fine','fine','fine','fine','headache frequent','fine','','','','sore','pink','','','','stress, tension and numbness','abcd,efg,xyz,,,,,','1,3,3 times a day,,,,,','29,30,10,,,,,','30 days,10 days,60 days,,,,,','2022-03-13','100,111,1000,,,,,'),(12,'2022-03-13','3','shoulder pain','20','','2 weeks','pain','loss','fine','fine','fine','not good','sweety','none','normal','none','none','paracetamol','stress','fine','fine','fine','swelling','fine','fine','fine','fine','fine','fin','fine','fine','no pain history','fine','NA','shoulder pain, take medicine lower the stress.','debplo,pigo,,,,,,','3 time a day,1 time a week,,,,,,','20 potency,10 potency,,,,,,','15 days,10 days,,,,,,','2022-03-13','100,200,,,,,,');
/*!40000 ALTER TABLE `anand_medical_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anand_patient_info`
--

DROP TABLE IF EXISTS `anand_patient_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `anand_patient_info` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `age` int NOT NULL,
  `contact_no` varchar(12) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(10) NOT NULL,
  `martial_status` varchar(10) NOT NULL,
  `occupation` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anand_patient_info`
--

LOCK TABLES `anand_patient_info` WRITE;
/*!40000 ALTER TABLE `anand_patient_info` DISABLE KEYS */;
INSERT INTO `anand_patient_info` VALUES (1,'sarv','g',10,'8297192121','ajab coloney\nnear sabji mandi\najabpur\n\n','ddn','u','none','1980-03-11'),(2,'sandeep','g',10,'8297192121','flat 2 near hanuman\nmandir\nprem nagar\n','ddn','u','none','1986-09-04'),(3,'Ravneet Singh','Male',34,'8297192121','389, Shivalik Enclave\nRace Course\nDehradun','Dehradun','Married','Software Engineer','1986-10-04'),(4,'Rupind','male',12,'1234567890','Houes No 44 Gobind nagar \nRace Course\nDehradun','Dehradun','Unmarried','Student','1990-12-12'),(5,'radeep','male',23,'4312344345','Flat no 120 Kricecnt Apartments\nDwarka vihar\ndelhi','delhi','Unmarried','unemployed','1992-04-03'),(6,'udeep','male',34,'123456789','Race Course','dehradun','married','train','1986-08-07'),(7,'r','male',0,'1234567898','House no 1\nrajpur road\nNear diversion\n\n','Rajpur','unmarried','student','1996-09-09'),(10,'preet','female',20,'1234567890','gobind nagar','paonta','unmarried','student','1990-12-03'),(11,'devom','male',50,'83972193231','house no 5\ngari cantt\nnear patrol pump','Haridwar','married','retired','1965-09-20'),(12,'deep','male',20,'312345678954','Rishekesh degree college, Risikesh dehradun highwa','Risikesh','single','college','1996-02-02');
/*!40000 ALTER TABLE `anand_patient_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ansari_gupta100_medical_record`
--

DROP TABLE IF EXISTS `ansari_gupta100_medical_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ansari_gupta100_medical_record` (
  `patient_id` int NOT NULL,
  `record_date` date NOT NULL,
  `case_type` varchar(2) NOT NULL,
  `symptoms` varchar(50) NOT NULL,
  `symptoms_agg_by` varchar(50) NOT NULL,
  `symptoms_ameol_by` varchar(50) NOT NULL,
  `symptoms_since` varchar(50) NOT NULL,
  `present_complains` varchar(50) NOT NULL,
  `appetite` varchar(50) NOT NULL,
  `thirst` varchar(50) NOT NULL,
  `urine` varchar(50) NOT NULL,
  `stool` varchar(50) NOT NULL,
  `sleep` varchar(50) NOT NULL,
  `perspiration` varchar(50) NOT NULL,
  `addiction` varchar(50) NOT NULL,
  `desires` varchar(50) NOT NULL,
  `aversions` varchar(50) NOT NULL,
  `thermal_reaction` varchar(50) NOT NULL,
  `allergy` varchar(50) NOT NULL,
  `mental_symptoms` varchar(50) NOT NULL,
  `back` varchar(50) NOT NULL,
  `chest` varchar(50) NOT NULL,
  `ear` varchar(50) NOT NULL,
  `eye` varchar(50) NOT NULL,
  `face` varchar(50) NOT NULL,
  `head` varchar(50) NOT NULL,
  `lips` varchar(50) NOT NULL,
  `mouth` varchar(50) NOT NULL,
  `nose` varchar(50) NOT NULL,
  `teeth` varchar(50) NOT NULL,
  `throat` varchar(50) NOT NULL,
  `tongue` varchar(50) NOT NULL,
  `past_history` varchar(50) NOT NULL,
  `family_history` varchar(50) NOT NULL,
  `menstrual_history` varchar(50) NOT NULL,
  `Investigation` varchar(50) NOT NULL,
  `medicine` varchar(160) NOT NULL,
  `dose` varchar(100) NOT NULL,
  `potency` varchar(80) NOT NULL,
  `days` varchar(80) NOT NULL,
  `next_visit_date` date NOT NULL,
  `amount` varchar(80) NOT NULL,
  PRIMARY KEY (`patient_id`,`record_date`),
  KEY `patient_id` (`patient_id`,`record_date`,`symptoms`,`Investigation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ansari_gupta100_medical_record`
--

LOCK TABLES `ansari_gupta100_medical_record` WRITE;
/*!40000 ALTER TABLE `ansari_gupta100_medical_record` DISABLE KEYS */;
INSERT INTO `ansari_gupta100_medical_record` VALUES (1,'2022-04-06','2','tinnitus','sound pollution','','2013 (9 years)','ringing in ear, \nsound sensitivity','','','','','','','','','','','','','fine','fine','ringing sound hurts','fine','fine','fine','fine','fin','fine','fine','soar','fine','','','','tinnitus and hyperacusis','tinnius,zorax,,,,,,','3,4 times a day,,,,,,','1,2,,,,,,','15 days,30 days,,,,,,','2022-04-06','200,500,,,,,,'),(1,'2022-04-07','','tinnitus still present','','','10 years','tinnitus and sensitivity to sound is still present','','less','','','','','','','','','','','','','senstive to sound','','','','','','','','still sore','','','','','no ch nge in tinnitus sound and hypercrusis presen',',,,,,,,',',,,,,,,',',,,,,,,',',,,,,,,','2022-05-17',',,,,,,,'),(2,'2022-04-06','3','numbness','standing','','10 years','numbness, \npain','fine','','','','two times a day','','','','','','','','pain','','','','','stuffy','','','','','','','','','','stress, numbness\nanexity','numbfee,bpfree,,,,,,','2,4,,,,,,','12,14,,,,,,','3,10,,,,,,','2022-04-06','500,50,,,,,,'),(2,'2022-04-07','','no change','','','','','','','','','','','','','','','','','pain as it is','','','','','','','','','','','','','','','','repeat same,,,,,,,','3,,,,,,,','12,,,,,,,','30 days,,,,,,,','2022-04-22','100,,,,,,,'),(3,'2022-04-06','3','back ache, headache','sitting, running fast','','20 days','back pain, headache','','','','','','','','','','','','','pain lower back','','','','','','','','','','','','','','','vitamin deficency, back pain and migraine','orthoGel,painKill,vitamin12,,,,,','3 times a day,Once,3 times a day,,,,,','0,1,4,,,,,','7 days,10 days,15 days,,,,,','2022-05-03','200,100,600,,,,,'),(3,'2022-04-07','','problem is still present','samve aggrevations are present','','2 months','same complains','','','','','','','','','','','','','','','','','','','','','','','','','anexity','','','still the problem is present.','repeat,,,,,,,',',,,,,,,',',,,,,,,',',,,,,,,','2022-04-22',',,,,,,,'),(4,'2022-04-06','2','arm problem','rotating','','20 days','pain in arm','','','','','','','','','','','','','','','','','','','','','','','','','','','','arm shoulder pain','armRest,,,,,,,','2 times a day,,,,,,,','12,,,,,,,','4,,,,,,,','2022-04-16','600,,,,,,,'),(5,'2022-04-07','2','anxiety stress','','','present condition','lots of anxiety stress and sleeping problem','','','','','','','','','','','','','','','','','','','','','','','','','','','','anxiety and stree','anxietyplus|calplus|becasul|med2||||','1|2|3|||||','|||||||','15 days|15 days|30 days|||||','2022-04-22','200|333|400|500||||'),(6,'2022-04-07','1','shoulder pain','excerise','','20 days','should pain on particular postures','','','','','','','','','','','','','','','','','','','','','','','','','','','','Shoulder pain on rotation etc','shoulderFix|pain relief||||||','3 times a day|4 times a day||||||','3|10||||||','4|10 days||||||','2022-04-22','600|800||||||');
/*!40000 ALTER TABLE `ansari_gupta100_medical_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ansari_gupta100_medical_record_file_i`
--

DROP TABLE IF EXISTS `ansari_gupta100_medical_record_file_i`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ansari_gupta100_medical_record_file_i` (
  `insert_id` int NOT NULL AUTO_INCREMENT,
  `file_name` char(200) NOT NULL,
  `creation_date` date NOT NULL,
  `is_backed_up` tinyint(1) NOT NULL,
  `back_up_creation_date_time` date DEFAULT NULL,
  `file_size` int DEFAULT NULL,
  PRIMARY KEY (`insert_id`),
  KEY `insert_id` (`insert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ansari_gupta100_medical_record_file_i`
--

LOCK TABLES `ansari_gupta100_medical_record_file_i` WRITE;
/*!40000 ALTER TABLE `ansari_gupta100_medical_record_file_i` DISABLE KEYS */;
INSERT INTO `ansari_gupta100_medical_record_file_i` VALUES (1,'ansari_gupta100_medical_record_file_i_2022-04-05-21-08-31.csv','2022-04-05',0,NULL,NULL);
/*!40000 ALTER TABLE `ansari_gupta100_medical_record_file_i` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ansari_gupta100_patient_info`
--

DROP TABLE IF EXISTS `ansari_gupta100_patient_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ansari_gupta100_patient_info` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `age` int NOT NULL,
  `contact_no` varchar(12) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(10) NOT NULL,
  `martial_status` varchar(10) NOT NULL,
  `occupation` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  PRIMARY KEY (`patient_id`),
  KEY `name` (`name`,`city`,`occupation`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ansari_gupta100_patient_info`
--

LOCK TABLES `ansari_gupta100_patient_info` WRITE;
/*!40000 ALTER TABLE `ansari_gupta100_patient_info` DISABLE KEYS */;
INSERT INTO `ansari_gupta100_patient_info` VALUES (1,'ravneet','male',32,'8297192121','389, Shivalik Enclave\nRace Course','Dehradun','Married','Software Engineer','1986-04-09'),(2,'Sarvajeet Singh','male',70,'9412962432','389, Shivalik Enclave\nRace Course','Dehradun','Married','Retired','1952-04-09'),(3,'meeta','female',30,'8297192121','House# 2 Dwarka nagar chowki near dalanwala','Haridwar','married','engineer','1990-04-05'),(4,'divanshu','male',8,'9389883020','gobind nagar house no 10 near gurdwara','paonta','unmarried','student','2003-01-01'),(5,'rakhul singh','male',10,'8297192121','ddn','ddn','unmarried','student','2020-11-01'),(6,'kavani singh','female',20,'9412962432','ponta','paonta','unmarried','student','1996-12-02'),(7,'deepu','mail',12,'','','','','','0000-00-00');
/*!40000 ALTER TABLE `ansari_gupta100_patient_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ansari_gupta100_patient_info_file_i`
--

DROP TABLE IF EXISTS `ansari_gupta100_patient_info_file_i`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ansari_gupta100_patient_info_file_i` (
  `insert_id` int NOT NULL AUTO_INCREMENT,
  `file_name` char(200) NOT NULL,
  `creation_date` date NOT NULL,
  `is_backed_up` tinyint(1) NOT NULL,
  `back_up_creation_date_time` date DEFAULT NULL,
  `file_size` int DEFAULT NULL,
  PRIMARY KEY (`insert_id`),
  KEY `insert_id` (`insert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ansari_gupta100_patient_info_file_i`
--

LOCK TABLES `ansari_gupta100_patient_info_file_i` WRITE;
/*!40000 ALTER TABLE `ansari_gupta100_patient_info_file_i` DISABLE KEYS */;
INSERT INTO `ansari_gupta100_patient_info_file_i` VALUES (1,'ansari_gupta100_patient_info_file_i_2022-04-05-21-08-31.csv','2022-04-05',0,NULL,NULL);
/*!40000 ALTER TABLE `ansari_gupta100_patient_info_file_i` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bhusan_homeo_medical_record`
--

DROP TABLE IF EXISTS `bhusan_homeo_medical_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bhusan_homeo_medical_record` (
  `patient_id` int NOT NULL,
  `record_date` date NOT NULL,
  `case_type` varchar(2) NOT NULL,
  `symptoms` varchar(50) NOT NULL,
  `symptoms_agg_by` varchar(50) NOT NULL,
  `symptoms_ameol_by` varchar(50) NOT NULL,
  `symptoms_since` varchar(50) NOT NULL,
  `present_complains` varchar(50) NOT NULL,
  `appetite` varchar(50) NOT NULL,
  `thirst` varchar(50) NOT NULL,
  `urine` varchar(50) NOT NULL,
  `stool` varchar(50) NOT NULL,
  `sleep` varchar(50) NOT NULL,
  `perspiration` varchar(50) NOT NULL,
  `addiction` varchar(50) NOT NULL,
  `desires` varchar(50) NOT NULL,
  `aversions` varchar(50) NOT NULL,
  `thermal_reaction` varchar(50) NOT NULL,
  `allergy` varchar(50) NOT NULL,
  `mental_symptoms` varchar(50) NOT NULL,
  `back` varchar(50) NOT NULL,
  `chest` varchar(50) NOT NULL,
  `ear` varchar(50) NOT NULL,
  `eye` varchar(50) NOT NULL,
  `face` varchar(50) NOT NULL,
  `head` varchar(50) NOT NULL,
  `lips` varchar(50) NOT NULL,
  `mouth` varchar(50) NOT NULL,
  `nose` varchar(50) NOT NULL,
  `teeth` varchar(50) NOT NULL,
  `throat` varchar(50) NOT NULL,
  `tongue` varchar(50) NOT NULL,
  `past_history` varchar(50) NOT NULL,
  `family_history` varchar(50) NOT NULL,
  `menstrual_history` varchar(50) NOT NULL,
  `Investigation` varchar(50) NOT NULL,
  `medicine` varchar(160) NOT NULL,
  `dose` varchar(100) NOT NULL,
  `potency` varchar(80) NOT NULL,
  `days` varchar(80) NOT NULL,
  `next_visit_date` date NOT NULL,
  `amount` varchar(80) NOT NULL,
  PRIMARY KEY (`patient_id`,`record_date`),
  KEY `patient_id` (`patient_id`,`record_date`,`symptoms`,`Investigation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bhusan_homeo_medical_record`
--

LOCK TABLES `bhusan_homeo_medical_record` WRITE;
/*!40000 ALTER TABLE `bhusan_homeo_medical_record` DISABLE KEYS */;
INSERT INTO `bhusan_homeo_medical_record` VALUES (1,'2022-04-06','','leg pain','moving','','','','less','less','yellow','consipation','','','','','','','','','back to leg pain','','','','','','','','','','','','','','','leg pain due to sciteica','painreleif,,,,,,,','3 times a day,,,,,,,','4,,,,,,,','30 days,,,,,,,','2022-05-06','441,,,,,,,'),(1,'2022-04-07','1','back pain','seating','','15 days','back pain','','','','','','','','','','','','','pain','','','','','','','','','','','','','','','back pain','backRelief,,,,,,,','3 days,,,,,,,','30,,,,,,,','15 days,,,,,,,','2022-04-17','400,,,,,,,'),(2,'2022-04-06','','hair fall','during bathing etc','','','','','','','','','','','','','','','anxiety','','','','','pimples','pain','','','','','sometimes sore','whitish','','','','Hair problem','harifixer,hairshapoo,,,,,,','5 times a day,once a week,,,,,,','1,,,,,,,','23,60 days,,,,,,','2022-06-13','300,900,,,,,,'),(3,'2022-04-07','','play','','','from birth','none','','','','','','','','','','','','','good','','','','','','','','','','','','','','','no problem','vitamins,,,,,,,','2,,,,,,,','23,,,,,,,','30days,,,,,,,','2022-04-07','1000,,,,,,,'),(4,'2022-04-07','2','scitica, back pain','','','10 years','back pain, leg pain specially in the mornings','','','','','difficult sometimes','','','','','','','','leg back pain','','','','','','','','','','','','','','','scitica, neck and back pain','mb|second med|third med|||||','2||3 time sa day|||||','4|||||||','df days|||||||','2022-04-22','300|333|500|||||'),(5,'2022-04-07','3','stomach pain','','','food','food posining','','','','','','','','','','','','','','','','','','','','','','','','','','','','loose motion due to food poisining','posinFree|||||||','2|||||||','1|||||||','12 days|||||||','2022-12-22','300|||||||');
/*!40000 ALTER TABLE `bhusan_homeo_medical_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bhusan_homeo_medical_record_file_i`
--

DROP TABLE IF EXISTS `bhusan_homeo_medical_record_file_i`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bhusan_homeo_medical_record_file_i` (
  `insert_id` int NOT NULL AUTO_INCREMENT,
  `file_name` char(200) NOT NULL,
  `creation_date` date NOT NULL,
  `is_backed_up` tinyint(1) NOT NULL,
  `back_up_creation_date_time` date DEFAULT NULL,
  `file_size` int DEFAULT NULL,
  PRIMARY KEY (`insert_id`),
  KEY `insert_id` (`insert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bhusan_homeo_medical_record_file_i`
--

LOCK TABLES `bhusan_homeo_medical_record_file_i` WRITE;
/*!40000 ALTER TABLE `bhusan_homeo_medical_record_file_i` DISABLE KEYS */;
INSERT INTO `bhusan_homeo_medical_record_file_i` VALUES (1,'bhusan_homeo_medical_record_file_i_2022-04-05-22-39-01.csv','2022-04-05',0,NULL,NULL);
/*!40000 ALTER TABLE `bhusan_homeo_medical_record_file_i` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bhusan_homeo_patient_info`
--

DROP TABLE IF EXISTS `bhusan_homeo_patient_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bhusan_homeo_patient_info` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `age` int NOT NULL,
  `contact_no` varchar(12) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(10) NOT NULL,
  `martial_status` varchar(10) NOT NULL,
  `occupation` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  PRIMARY KEY (`patient_id`),
  KEY `name` (`name`,`city`,`occupation`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bhusan_homeo_patient_info`
--

LOCK TABLES `bhusan_homeo_patient_info` WRITE;
/*!40000 ALTER TABLE `bhusan_homeo_patient_info` DISABLE KEYS */;
INSERT INTO `bhusan_homeo_patient_info` VALUES (1,'dibu','male',12,'8297192121','bankar road house no 2 near tutorials','chennai','unmarried','student','2000-12-01'),(2,'bhawana','female',18,'9389883020','bhisan nagar house no 23 near tower','rishikesh','unmarried','student','1998-01-01'),(3,'avreet','female',4,'8297192121','nagar diwarka near ongce','paonta','NA','NA','2020-09-02'),(4,'mandeep kaur','female',65,'9412962432','389, Shivalik Enclave\nRace Course','Dehradun','married','house wife','1956-02-02'),(5,'varundita','',0,'','','','','','2000-12-01');
/*!40000 ALTER TABLE `bhusan_homeo_patient_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bhusan_homeo_patient_info_file_i`
--

DROP TABLE IF EXISTS `bhusan_homeo_patient_info_file_i`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bhusan_homeo_patient_info_file_i` (
  `insert_id` int NOT NULL AUTO_INCREMENT,
  `file_name` char(200) NOT NULL,
  `creation_date` date NOT NULL,
  `is_backed_up` tinyint(1) NOT NULL,
  `back_up_creation_date_time` date DEFAULT NULL,
  `file_size` int DEFAULT NULL,
  PRIMARY KEY (`insert_id`),
  KEY `insert_id` (`insert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bhusan_homeo_patient_info_file_i`
--

LOCK TABLES `bhusan_homeo_patient_info_file_i` WRITE;
/*!40000 ALTER TABLE `bhusan_homeo_patient_info_file_i` DISABLE KEYS */;
INSERT INTO `bhusan_homeo_patient_info_file_i` VALUES (1,'bhusan_homeo_patient_info_file_i_2022-04-05-22-39-01.csv','2022-04-05',0,NULL,NULL);
/*!40000 ALTER TABLE `bhusan_homeo_patient_info_file_i` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_info`
--

DROP TABLE IF EXISTS `doctor_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_info` (
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(10) NOT NULL,
  `contact_no` varchar(12) NOT NULL,
  `mobile_no` varchar(10) NOT NULL,
  `clinic_name` varchar(20) NOT NULL,
  `clinic_address` varchar(50) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_info`
--

LOCK TABLES `doctor_info` WRITE;
/*!40000 ALTER TABLE `doctor_info` DISABLE KEYS */;
INSERT INTO `doctor_info` VALUES ('Dr anurag joshi','a_joshi@gmail.com','joshi','8297192121','','',''),('Dr Anand Malhotra','anand@gmail.com','anand','8297192121','8297192121','Anand Malhotra','Shop # 3 Gobind Nagar Race Course Dehradun'),('Dr Ansari Gupta','ansari_gupta100@gmail.com','ansari','8297192121','8297192121','Homepathy for cure','Shop # 12, Kamla market near fountain Dehradun.'),('bhusan singh dawar','bhusan_homeo@gmail.com','bhusan','8297192121','8297192121','Bhusan Homeopathy','clinic no 2 lingampally near relience hyderabad'),('Dr Rajan Mahajan','mahajan@gmail.com','mahajan','8297192121','','','');
/*!40000 ALTER TABLE `doctor_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_info_file_i`
--

DROP TABLE IF EXISTS `doctor_info_file_i`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_info_file_i` (
  `insert_id` int NOT NULL AUTO_INCREMENT,
  `file_name` char(200) NOT NULL,
  `creation_date` date NOT NULL,
  `is_backed_up` tinyint(1) NOT NULL,
  `back_up_creation_date_time` date DEFAULT NULL,
  `file_size` int DEFAULT NULL,
  PRIMARY KEY (`insert_id`),
  KEY `insert_id` (`insert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_info_file_i`
--

LOCK TABLES `doctor_info_file_i` WRITE;
/*!40000 ALTER TABLE `doctor_info_file_i` DISABLE KEYS */;
INSERT INTO `doctor_info_file_i` VALUES (1,'doctor_info_file_i_first.csv','2022-04-06',0,NULL,NULL);
/*!40000 ALTER TABLE `doctor_info_file_i` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mahajan_medical_record`
--

DROP TABLE IF EXISTS `mahajan_medical_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mahajan_medical_record` (
  `patient_id` int NOT NULL,
  `record_date` date NOT NULL,
  `case_type` varchar(2) NOT NULL,
  `symptoms` varchar(200) NOT NULL,
  `symptoms_agg_by` varchar(100) NOT NULL,
  `symptoms_ameol_by` varchar(50) NOT NULL,
  `symptoms_since` varchar(50) NOT NULL,
  `present_complains` varchar(200) NOT NULL,
  `appetite` varchar(50) NOT NULL,
  `thirst` varchar(50) NOT NULL,
  `urine` varchar(50) NOT NULL,
  `stool` varchar(50) NOT NULL,
  `sleep` varchar(50) NOT NULL,
  `perspiration` varchar(50) NOT NULL,
  `addiction` varchar(50) NOT NULL,
  `desires` varchar(50) NOT NULL,
  `aversions` varchar(50) NOT NULL,
  `thermal_reaction` varchar(50) NOT NULL,
  `allergy` varchar(50) NOT NULL,
  `mental_symptoms` varchar(50) NOT NULL,
  `back` varchar(50) NOT NULL,
  `chest` varchar(50) NOT NULL,
  `ear` varchar(50) NOT NULL,
  `eye` varchar(50) NOT NULL,
  `face` varchar(50) NOT NULL,
  `head` varchar(50) NOT NULL,
  `lips` varchar(50) NOT NULL,
  `mouth` varchar(50) NOT NULL,
  `nose` varchar(50) NOT NULL,
  `teeth` varchar(50) NOT NULL,
  `throat` varchar(50) NOT NULL,
  `tongue` varchar(50) NOT NULL,
  `past_history` varchar(50) NOT NULL,
  `family_history` varchar(50) NOT NULL,
  `menstrual_history` varchar(50) NOT NULL,
  `Investigation` varchar(200) NOT NULL,
  `medicine` varchar(160) NOT NULL,
  `dose` varchar(100) NOT NULL,
  `potency` varchar(80) NOT NULL,
  `days` varchar(80) NOT NULL,
  `next_visit_date` date NOT NULL,
  `amount` varchar(80) NOT NULL,
  PRIMARY KEY (`patient_id`,`record_date`),
  KEY `patient_id` (`patient_id`,`record_date`,`symptoms`,`Investigation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mahajan_medical_record`
--

LOCK TABLES `mahajan_medical_record` WRITE;
/*!40000 ALTER TABLE `mahajan_medical_record` DISABLE KEYS */;
INSERT INTO `mahajan_medical_record` VALUES (2,'2022-04-08','2','headche','','','pc working','headche and migraine when working on PC','','','','','','','','','','','','','','','','','','','','','','','sore','','history of heaachees','','','headache and migranes','migrfill|vitamin||||||','2|1||||||','12|||||||','15 days|30 days||||||','2022-04-23','100|330||||||');
/*!40000 ALTER TABLE `mahajan_medical_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mahajan_medical_record_file_i`
--

DROP TABLE IF EXISTS `mahajan_medical_record_file_i`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mahajan_medical_record_file_i` (
  `insert_id` int NOT NULL AUTO_INCREMENT,
  `file_name` char(200) NOT NULL,
  `creation_date` date NOT NULL,
  `is_backed_up` tinyint(1) NOT NULL,
  `back_up_creation_date_time` date DEFAULT NULL,
  `file_size` int DEFAULT NULL,
  PRIMARY KEY (`insert_id`),
  KEY `insert_id` (`insert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mahajan_medical_record_file_i`
--

LOCK TABLES `mahajan_medical_record_file_i` WRITE;
/*!40000 ALTER TABLE `mahajan_medical_record_file_i` DISABLE KEYS */;
INSERT INTO `mahajan_medical_record_file_i` VALUES (1,'mahajan_medical_record_file_i_2022-04-08-08-22-16.csv','2022-04-08',0,NULL,NULL);
/*!40000 ALTER TABLE `mahajan_medical_record_file_i` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mahajan_patient_info`
--

DROP TABLE IF EXISTS `mahajan_patient_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mahajan_patient_info` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `age` int NOT NULL,
  `contact_no` varchar(12) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(10) NOT NULL,
  `martial_status` varchar(10) NOT NULL,
  `occupation` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  PRIMARY KEY (`patient_id`),
  KEY `name` (`name`,`city`,`occupation`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mahajan_patient_info`
--

LOCK TABLES `mahajan_patient_info` WRITE;
/*!40000 ALTER TABLE `mahajan_patient_info` DISABLE KEYS */;
INSERT INTO `mahajan_patient_info` VALUES (1,'deepika','female',23,'','','','unmarried','student','0000-00-00'),(2,'radhika','female',32,'8297192121','dehradun','DDN','married','working','1986-11-02');
/*!40000 ALTER TABLE `mahajan_patient_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mahajan_patient_info_file_i`
--

DROP TABLE IF EXISTS `mahajan_patient_info_file_i`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mahajan_patient_info_file_i` (
  `insert_id` int NOT NULL AUTO_INCREMENT,
  `file_name` char(200) NOT NULL,
  `creation_date` date NOT NULL,
  `is_backed_up` tinyint(1) NOT NULL,
  `back_up_creation_date_time` date DEFAULT NULL,
  `file_size` int DEFAULT NULL,
  PRIMARY KEY (`insert_id`),
  KEY `insert_id` (`insert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mahajan_patient_info_file_i`
--

LOCK TABLES `mahajan_patient_info_file_i` WRITE;
/*!40000 ALTER TABLE `mahajan_patient_info_file_i` DISABLE KEYS */;
INSERT INTO `mahajan_patient_info_file_i` VALUES (1,'mahajan_patient_info_file_i_2022-04-08-08-22-16.csv','2022-04-08',0,NULL,NULL);
/*!40000 ALTER TABLE `mahajan_patient_info_file_i` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-23 21:37:14
