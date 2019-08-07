-- MySQL dump 10.16  Distrib 10.1.40-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: unltd
-- ------------------------------------------------------
-- Server version	10.1.40-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `api`
--

DROP TABLE IF EXISTS `api`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `ApiAccessKey` varchar(50) NOT NULL,
  `ApiSecretKey` varchar(50) NOT NULL,
  `ApiName` varchar(50) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `api_UserId_fc2796e9_fk_user_Id` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api`
--

LOCK TABLES `api` WRITE;
/*!40000 ALTER TABLE `api` DISABLE KEYS */;
/*!40000 ALTER TABLE `api` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=221 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add category',1,'add_category'),(2,'Can change category',1,'change_category'),(3,'Can delete category',1,'delete_category'),(4,'Can view category',1,'view_category'),(5,'Can add item',2,'add_item'),(6,'Can change item',2,'change_item'),(7,'Can delete item',2,'delete_item'),(8,'Can view item',2,'view_item'),(9,'Can add languages',3,'add_languages'),(10,'Can change languages',3,'change_languages'),(11,'Can delete languages',3,'delete_languages'),(12,'Can view languages',3,'view_languages'),(13,'Can add orders',4,'add_orders'),(14,'Can change orders',4,'change_orders'),(15,'Can delete orders',4,'delete_orders'),(16,'Can view orders',4,'view_orders'),(17,'Can add packages',5,'add_packages'),(18,'Can change packages',5,'change_packages'),(19,'Can delete packages',5,'delete_packages'),(20,'Can view packages',5,'view_packages'),(21,'Can add qa replies',6,'add_qareplies'),(22,'Can change qa replies',6,'change_qareplies'),(23,'Can delete qa replies',6,'delete_qareplies'),(24,'Can view qa replies',6,'view_qareplies'),(25,'Can add qa support',7,'add_qasupport'),(26,'Can change qa support',7,'change_qasupport'),(27,'Can delete qa support',7,'delete_qasupport'),(28,'Can view qa support',7,'view_qasupport'),(29,'Can add sms packages',8,'add_smspackages'),(30,'Can change sms packages',8,'change_smspackages'),(31,'Can delete sms packages',8,'delete_smspackages'),(32,'Can view sms packages',8,'view_smspackages'),(33,'Can add superadmin',9,'add_superadmin'),(34,'Can change superadmin',9,'change_superadmin'),(35,'Can delete superadmin',9,'delete_superadmin'),(36,'Can view superadmin',9,'view_superadmin'),(37,'Can add user',10,'add_user'),(38,'Can change user',10,'change_user'),(39,'Can delete user',10,'delete_user'),(40,'Can view user',10,'view_user'),(41,'Can add vendor',11,'add_vendor'),(42,'Can change vendor',11,'change_vendor'),(43,'Can delete vendor',11,'delete_vendor'),(44,'Can view vendor',11,'view_vendor'),(45,'Can add venderorders',12,'add_venderorders'),(46,'Can change venderorders',12,'change_venderorders'),(47,'Can delete venderorders',12,'delete_venderorders'),(48,'Can view venderorders',12,'view_venderorders'),(49,'Can add transaction',13,'add_transaction'),(50,'Can change transaction',13,'change_transaction'),(51,'Can delete transaction',13,'delete_transaction'),(52,'Can view transaction',13,'view_transaction'),(53,'Can add tables',14,'add_tables'),(54,'Can change tables',14,'change_tables'),(55,'Can delete tables',14,'delete_tables'),(56,'Can view tables',14,'view_tables'),(57,'Can add subscription',15,'add_subscription'),(58,'Can change subscription',15,'change_subscription'),(59,'Can delete subscription',15,'delete_subscription'),(60,'Can view subscription',15,'view_subscription'),(61,'Can add subcategory',16,'add_subcategory'),(62,'Can change subcategory',16,'change_subcategory'),(63,'Can delete subcategory',16,'delete_subcategory'),(64,'Can view subcategory',16,'view_subcategory'),(65,'Can add staff',17,'add_staff'),(66,'Can change staff',17,'change_staff'),(67,'Can delete staff',17,'delete_staff'),(68,'Can view staff',17,'view_staff'),(69,'Can add selectedlanguage',18,'add_selectedlanguage'),(70,'Can change selectedlanguage',18,'change_selectedlanguage'),(71,'Can delete selectedlanguage',18,'delete_selectedlanguage'),(72,'Can view selectedlanguage',18,'view_selectedlanguage'),(73,'Can add recharge history',19,'add_rechargehistory'),(74,'Can change recharge history',19,'change_rechargehistory'),(75,'Can delete recharge history',19,'delete_rechargehistory'),(76,'Can view recharge history',19,'view_rechargehistory'),(77,'Can add messagesender',20,'add_messagesender'),(78,'Can change messagesender',20,'change_messagesender'),(79,'Can delete messagesender',20,'delete_messagesender'),(80,'Can view messagesender',20,'view_messagesender'),(81,'Can add messages',21,'add_messages'),(82,'Can change messages',21,'change_messages'),(83,'Can delete messages',21,'delete_messages'),(84,'Can view messages',21,'view_messages'),(85,'Can add menu',22,'add_menu'),(86,'Can change menu',22,'change_menu'),(87,'Can delete menu',22,'delete_menu'),(88,'Can view menu',22,'view_menu'),(89,'Can add membership',23,'add_membership'),(90,'Can change membership',23,'change_membership'),(91,'Can delete membership',23,'delete_membership'),(92,'Can view membership',23,'view_membership'),(93,'Can add member',24,'add_member'),(94,'Can change member',24,'change_member'),(95,'Can delete member',24,'delete_member'),(96,'Can view member',24,'view_member'),(97,'Can add location',25,'add_location'),(98,'Can change location',25,'change_location'),(99,'Can delete location',25,'delete_location'),(100,'Can view location',25,'view_location'),(101,'Can add itemorder',26,'add_itemorder'),(102,'Can change itemorder',26,'change_itemorder'),(103,'Can delete itemorder',26,'delete_itemorder'),(104,'Can view itemorder',26,'view_itemorder'),(105,'Can add itemofferoptions',27,'add_itemofferoptions'),(106,'Can change itemofferoptions',27,'change_itemofferoptions'),(107,'Can delete itemofferoptions',27,'delete_itemofferoptions'),(108,'Can view itemofferoptions',27,'view_itemofferoptions'),(109,'Can add itemdisplay',28,'add_itemdisplay'),(110,'Can change itemdisplay',28,'change_itemdisplay'),(111,'Can delete itemdisplay',28,'delete_itemdisplay'),(112,'Can view itemdisplay',28,'view_itemdisplay'),(113,'Can add images',29,'add_images'),(114,'Can change images',29,'change_images'),(115,'Can delete images',29,'delete_images'),(116,'Can view images',29,'view_images'),(117,'Can add developersuse',30,'add_developersuse'),(118,'Can change developersuse',30,'change_developersuse'),(119,'Can delete developersuse',30,'delete_developersuse'),(120,'Can view developersuse',30,'view_developersuse'),(121,'Can add booking',31,'add_booking'),(122,'Can change booking',31,'change_booking'),(123,'Can delete booking',31,'delete_booking'),(124,'Can view booking',31,'view_booking'),(125,'Can add api',32,'add_api'),(126,'Can change api',32,'change_api'),(127,'Can delete api',32,'delete_api'),(128,'Can view api',32,'view_api'),(129,'Can add log entry',33,'add_logentry'),(130,'Can change log entry',33,'change_logentry'),(131,'Can delete log entry',33,'delete_logentry'),(132,'Can view log entry',33,'view_logentry'),(133,'Can add permission',34,'add_permission'),(134,'Can change permission',34,'change_permission'),(135,'Can delete permission',34,'delete_permission'),(136,'Can view permission',34,'view_permission'),(137,'Can add group',35,'add_group'),(138,'Can change group',35,'change_group'),(139,'Can delete group',35,'delete_group'),(140,'Can view group',35,'view_group'),(141,'Can add user',36,'add_user'),(142,'Can change user',36,'change_user'),(143,'Can delete user',36,'delete_user'),(144,'Can view user',36,'view_user'),(145,'Can add content type',37,'add_contenttype'),(146,'Can change content type',37,'change_contenttype'),(147,'Can delete content type',37,'delete_contenttype'),(148,'Can view content type',37,'view_contenttype'),(149,'Can add session',38,'add_session'),(150,'Can change session',38,'change_session'),(151,'Can delete session',38,'delete_session'),(152,'Can view session',38,'view_session'),(153,'Can add currency',39,'add_currency'),(154,'Can change currency',39,'change_currency'),(155,'Can delete currency',39,'delete_currency'),(156,'Can view currency',39,'view_currency'),(157,'Can add general setting',40,'add_generalsetting'),(158,'Can change general setting',40,'change_generalsetting'),(159,'Can delete general setting',40,'delete_generalsetting'),(160,'Can view general setting',40,'view_generalsetting'),(161,'Can add sms subscription',41,'add_smssubscription'),(162,'Can change sms subscription',41,'change_smssubscription'),(163,'Can delete sms subscription',41,'delete_smssubscription'),(164,'Can view sms subscription',41,'view_smssubscription'),(165,'Can add broad cast event messages',42,'add_broadcasteventmessages'),(166,'Can change broad cast event messages',42,'change_broadcasteventmessages'),(167,'Can delete broad cast event messages',42,'delete_broadcasteventmessages'),(168,'Can view broad cast event messages',42,'view_broadcasteventmessages'),(169,'Can add group',43,'add_group'),(170,'Can change group',43,'change_group'),(171,'Can delete group',43,'delete_group'),(172,'Can view group',43,'view_group'),(173,'Can add group member',44,'add_groupmember'),(174,'Can change group member',44,'change_groupmember'),(175,'Can delete group member',44,'delete_groupmember'),(176,'Can view group member',44,'view_groupmember'),(177,'Can add item variation',45,'add_itemvariation'),(178,'Can change item variation',45,'change_itemvariation'),(179,'Can delete item variation',45,'delete_itemvariation'),(180,'Can view item variation',45,'view_itemvariation'),(181,'Can add tutorial',46,'add_tutorial'),(182,'Can change tutorial',46,'change_tutorial'),(183,'Can delete tutorial',46,'delete_tutorial'),(184,'Can view tutorial',46,'view_tutorial'),(185,'Can add backup',47,'add_backup'),(186,'Can change backup',47,'change_backup'),(187,'Can delete backup',47,'delete_backup'),(188,'Can view backup',47,'view_backup'),(189,'Can add tutorial type',48,'add_tutorialtype'),(190,'Can change tutorial type',48,'change_tutorialtype'),(191,'Can delete tutorial type',48,'delete_tutorialtype'),(192,'Can view tutorial type',48,'view_tutorialtype'),(193,'Can add vendor staff',49,'add_vendorstaff'),(194,'Can change vendor staff',49,'change_vendorstaff'),(195,'Can delete vendor staff',49,'delete_vendorstaff'),(196,'Can view vendor staff',49,'view_vendorstaff'),(197,'Can add vendor member',50,'add_vendormember'),(198,'Can change vendor member',50,'change_vendormember'),(199,'Can delete vendor member',50,'delete_vendormember'),(200,'Can view vendor member',50,'view_vendormember'),(201,'Can add vendor discount',51,'add_vendordiscount'),(202,'Can change vendor discount',51,'change_vendordiscount'),(203,'Can delete vendor discount',51,'delete_vendordiscount'),(204,'Can view vendor discount',51,'view_vendordiscount'),(205,'Can add itemofferoption',52,'add_itemofferoption'),(206,'Can change itemofferoption',52,'change_itemofferoption'),(207,'Can delete itemofferoption',52,'delete_itemofferoption'),(208,'Can view itemofferoption',52,'view_itemofferoption'),(209,'Can add google_ setup',53,'add_google_setup'),(210,'Can change google_ setup',53,'change_google_setup'),(211,'Can delete google_ setup',53,'delete_google_setup'),(212,'Can view google_ setup',53,'view_google_setup'),(213,'Can add payment_ gateway',54,'add_payment_gateway'),(214,'Can change payment_ gateway',54,'change_payment_gateway'),(215,'Can delete payment_ gateway',54,'delete_payment_gateway'),(216,'Can view payment_ gateway',54,'view_payment_gateway'),(217,'Can add sm s_ setup',55,'add_sms_setup'),(218,'Can change sm s_ setup',55,'change_sms_setup'),(219,'Can delete sm s_ setup',55,'delete_sms_setup'),(220,'Can view sm s_ setup',55,'view_sms_setup');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backup`
--

DROP TABLE IF EXISTS `backup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backup` (
  `db_id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(255) NOT NULL,
  `size` varchar(255) NOT NULL,
  `process` varchar(20) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  PRIMARY KEY (`db_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backup`
--

LOCK TABLES `backup` WRITE;
/*!40000 ALTER TABLE `backup` DISABLE KEYS */;
/*!40000 ALTER TABLE `backup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booking` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `DateTime` datetime(6) NOT NULL,
  `Status` varchar(50) NOT NULL,
  `TableId` int(11) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `booking_TableId_3fa737b6_fk_tables_Id` (`TableId`),
  KEY `booking_UserId_8114e1bf_fk_user_Id` (`UserId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (1,'2019-08-28 20:00:00.000000','True',12,25);
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `broadcasteventmessages`
--

DROP TABLE IF EXISTS `broadcasteventmessages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `broadcasteventmessages` (
  `MessageId` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(255) NOT NULL,
  `Description` longtext NOT NULL,
  `Type` varchar(255) NOT NULL,
  `MessageType` varchar(255) NOT NULL,
  `Status` varchar(255) NOT NULL,
  `SenderId` int(11) NOT NULL,
  PRIMARY KEY (`MessageId`),
  KEY `BroadCastEventMessages_SenderId_a1a5054f_fk_user_Id` (`SenderId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `broadcasteventmessages`
--

LOCK TABLES `broadcasteventmessages` WRITE;
/*!40000 ALTER TABLE `broadcasteventmessages` DISABLE KEYS */;
/*!40000 ALTER TABLE `broadcasteventmessages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `CategoryName` varchar(50) NOT NULL,
  `TimeRange` datetime(6) NOT NULL,
  `CreatedDate` datetime(6) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `category_UserId_98705b45_fk_user_Id` (`UserId`),
  CONSTRAINT `category_UserId_98705b45_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Category 1','2019-08-16 19:00:00.000000','2019-08-02 14:03:24.442508',1),(2,'Hotel','2019-08-08 06:30:00.000000','2019-08-05 05:34:49.428074',1),(3,'Resturant','2019-08-08 06:30:00.000000','2019-08-05 05:35:02.144787',1);
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `currency`
--

DROP TABLE IF EXISTS `currency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `currency` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Currency` varchar(225) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `currency`
--

LOCK TABLES `currency` WRITE;
/*!40000 ALTER TABLE `currency` DISABLE KEYS */;
/*!40000 ALTER TABLE `currency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `developersuse`
--

DROP TABLE IF EXISTS `developersuse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `developersuse` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Tag` longtext NOT NULL,
  `Notes` longtext NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `developersuse_UserId_538ac5d5_fk_user_Id` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `developersuse`
--

LOCK TABLES `developersuse` WRITE;
/*!40000 ALTER TABLE `developersuse` DISABLE KEYS */;
/*!40000 ALTER TABLE `developersuse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (33,'admin','logentry'),(35,'auth','group'),(34,'auth','permission'),(36,'auth','user'),(37,'contenttypes','contenttype'),(38,'sessions','session'),(32,'unltd','api'),(47,'unltd','backup'),(31,'unltd','booking'),(42,'unltd','broadcasteventmessages'),(1,'unltd','category'),(39,'unltd','currency'),(30,'unltd','developersuse'),(40,'unltd','generalsetting'),(53,'unltd','google_setup'),(43,'unltd','group'),(44,'unltd','groupmember'),(29,'unltd','images'),(2,'unltd','item'),(28,'unltd','itemdisplay'),(52,'unltd','itemofferoption'),(27,'unltd','itemofferoptions'),(26,'unltd','itemorder'),(45,'unltd','itemvariation'),(3,'unltd','languages'),(25,'unltd','location'),(24,'unltd','member'),(23,'unltd','membership'),(22,'unltd','menu'),(21,'unltd','messages'),(20,'unltd','messagesender'),(4,'unltd','orders'),(5,'unltd','packages'),(54,'unltd','payment_gateway'),(6,'unltd','qareplies'),(7,'unltd','qasupport'),(19,'unltd','rechargehistory'),(18,'unltd','selectedlanguage'),(8,'unltd','smspackages'),(41,'unltd','smssubscription'),(55,'unltd','sms_setup'),(17,'unltd','staff'),(16,'unltd','subcategory'),(15,'unltd','subscription'),(9,'unltd','superadmin'),(14,'unltd','tables'),(13,'unltd','transaction'),(46,'unltd','tutorial'),(48,'unltd','tutorialtype'),(10,'unltd','user'),(12,'unltd','venderorders'),(11,'unltd','vendor'),(51,'unltd','vendordiscount'),(50,'unltd','vendormember'),(49,'unltd','vendorstaff');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-07-25 07:37:33.092712'),(2,'auth','0001_initial','2019-07-25 07:37:37.249948'),(3,'admin','0001_initial','2019-07-25 07:37:53.983417'),(4,'admin','0002_logentry_remove_auto_add','2019-07-25 07:38:03.824327'),(5,'admin','0003_logentry_add_action_flag_choices','2019-07-25 07:38:04.047154'),(6,'contenttypes','0002_remove_content_type_name','2019-07-25 07:38:06.948693'),(7,'auth','0002_alter_permission_name_max_length','2019-07-25 07:38:07.327299'),(8,'auth','0003_alter_user_email_max_length','2019-07-25 07:38:07.637962'),(9,'auth','0004_alter_user_username_opts','2019-07-25 07:38:07.716097'),(10,'auth','0005_alter_user_last_login_null','2019-07-25 07:38:09.343435'),(11,'auth','0006_require_contenttypes_0002','2019-07-25 07:38:09.405989'),(12,'auth','0007_alter_validators_add_error_messages','2019-07-25 07:38:09.521452'),(13,'auth','0008_alter_user_username_max_length','2019-07-25 07:38:10.624928'),(14,'auth','0009_alter_user_last_name_max_length','2019-07-25 07:38:11.126429'),(15,'auth','0010_alter_group_name_max_length','2019-07-25 07:38:12.028647'),(16,'auth','0011_update_proxy_permissions','2019-07-25 07:38:12.113430'),(17,'sessions','0001_initial','2019-07-25 07:38:12.868983'),(18,'unltd','0001_initial','2019-07-25 07:38:49.246271'),(19,'unltd','0002_auto_20190725_0047','2019-07-25 07:47:45.164222'),(20,'unltd','0003_auto_20190725_0049','2019-07-25 07:49:17.778106'),(21,'unltd','0004_auto_20190725_0245','2019-07-25 09:46:14.234845'),(22,'unltd','0005_auto_20190725_0257','2019-07-25 09:57:14.589968'),(23,'unltd','0006_auto_20190725_0312','2019-07-25 10:12:47.520964'),(24,'unltd','0007_smssubscription','2019-07-25 10:33:26.658363'),(25,'unltd','0008_smspackages_packagecreationdate','2019-07-25 10:55:59.932952'),(26,'unltd','0009_auto_20190725_0425','2019-07-25 11:25:42.471344'),(27,'unltd','0010_auto_20190725_0441','2019-07-25 11:41:17.636768'),(28,'unltd','0011_auto_20190725_0443','2019-07-25 11:44:05.227684'),(29,'unltd','0012_auto_20190725_0453','2019-07-25 11:53:39.025724'),(30,'unltd','0013_item_itemimage','2019-07-26 04:15:35.770754'),(31,'unltd','0014_auto_20190726_0405','2019-07-26 11:06:07.001872'),(32,'unltd','0015_auto_20190726_0408','2019-07-26 11:08:15.509189'),(33,'unltd','0016_broadcasteventmessages_group_groupmember','2019-07-29 05:29:14.330905'),(34,'unltd','0017_auto_20190728_2233','2019-07-29 05:33:51.243310'),(35,'unltd','0018_auto_20190730_0240','2019-07-30 09:40:35.386023'),(36,'unltd','0019_auto_20190730_0331','2019-07-30 10:31:59.267266'),(37,'unltd','0020_auto_20190730_0339','2019-07-30 10:39:32.523555'),(38,'unltd','0021_itemvariation_price','2019-07-30 10:51:02.472672'),(39,'unltd','0022_orders_discount','2019-07-31 07:02:50.776941'),(40,'unltd','0023_itemorder_itemvariation','2019-08-01 07:13:26.644986'),(41,'unltd','0024_itemorder_orderdate','2019-08-01 07:33:36.357247'),(42,'unltd','0002_backup','2019-08-01 12:26:11.453708'),(43,'unltd','0003_auto_20190805_0912','2019-08-05 04:13:29.477751'),(44,'unltd','0004_vendormember_vendorstaff','2019-08-05 04:44:51.211642'),(45,'unltd','0005_auto_20190805_0947','2019-08-05 04:47:50.600216'),(46,'unltd','0006_auto_20190805_1021','2019-08-05 05:22:07.110204'),(47,'unltd','0007_auto_20190806_0914','2019-08-06 04:15:23.829542'),(48,'unltd','0008_google_setup_payment_gateway_sms_setup','2019-08-06 11:25:02.487215');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4676fdv5ja8924yffl56rqk9hboedslw','ZjYxMGI4ZGEyMGNhZjdiNjhjNzRkOGFlOGJkODM2ZGJmNTUxNzI4Yzp7Il9sYW5ndWFnZSI6ImVuIiwiaWQiOjEsIlVzZXJUeXBlIjoiU3VwZXJBZG1pbiIsIlVzZXJJZCI6IlNQMDAwMSIsIkRpc3BsYXlOYW1lIjoiQWZ0YWIgQW5zYXJpIiwidXNlcl90eXBlIjoiU3VwZXJBZG1pbiIsImxhbmd1YWdlIjoiRW5nbGlzaCIsImN1cnJlbmN5IjoiJCIsIkFjdGl2ZSI6IlZpZXdWZW5kb3IiLCJ1c2VybmFtZSI6InN1cGVyYWRtaW4ifQ==','2019-08-19 12:29:15.361478'),('b0kj54c844aojm69wocqzo4f9slp2ox6','OGUyYzQ4NGE3NmJjNDQzZDI5ZDg4MzhmZjcxYjgxZjk5NzUzMTM0Yjp7IkFjdGl2ZSI6IlZpZXdWZW5kb3IifQ==','2019-08-15 05:04:48.903366'),('kmwxp49yvrxbp5o1uzq2r5jy4tc7trm8','OGUyYzQ4NGE3NmJjNDQzZDI5ZDg4MzhmZjcxYjgxZjk5NzUzMTM0Yjp7IkFjdGl2ZSI6IlZpZXdWZW5kb3IifQ==','2019-08-15 10:31:21.139161');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generalsetting`
--

DROP TABLE IF EXISTS `generalsetting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `generalsetting` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Language` varchar(225) NOT NULL,
  `Currency` varchar(225) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `GeneralSetting_UserId_7ec9fbd7_fk_user_Id` (`UserId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generalsetting`
--

LOCK TABLES `generalsetting` WRITE;
/*!40000 ALTER TABLE `generalsetting` DISABLE KEYS */;
INSERT INTO `generalsetting` VALUES (1,'English','$',1);
/*!40000 ALTER TABLE `generalsetting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `google_setup`
--

DROP TABLE IF EXISTS `google_setup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `google_setup` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Map_API` varchar(225) NOT NULL,
  `ReCaptcha_API` varchar(225) NOT NULL,
  `Analytic_Code` varchar(225) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `google_setup`
--

LOCK TABLES `google_setup` WRITE;
/*!40000 ALTER TABLE `google_setup` DISABLE KEYS */;
INSERT INTO `google_setup` VALUES (1,'Google API','1234432','analyticcode'),(2,'Google API_2','12344322','analyticcode_2');
/*!40000 ALTER TABLE `google_setup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group`
--

DROP TABLE IF EXISTS `group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group` (
  `GroupId` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(255) NOT NULL,
  `Description` longtext NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`GroupId`),
  KEY `Group_UserId_847998c0_fk_user_Id` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group`
--

LOCK TABLES `group` WRITE;
/*!40000 ALTER TABLE `group` DISABLE KEYS */;
/*!40000 ALTER TABLE `group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `images` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Source` varchar(50) NOT NULL,
  `ItemId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `images_ItemId_3b669f56_fk_item_Id` (`ItemId`),
  CONSTRAINT `images_ItemId_3b669f56_fk_item_Id` FOREIGN KEY (`ItemId`) REFERENCES `item` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `item` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `ItemName` varchar(225) NOT NULL,
  `Description` varchar(225) NOT NULL,
  `Visible` int(11) NOT NULL,
  `PrepareTime` int(11) NOT NULL,
  `ItemImage` varchar(225) NOT NULL,
  `CreatedDate` datetime(6) NOT NULL,
  `ItemDisplayId` int(11) NOT NULL,
  `SubCategoryId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `item_ItemDisplayId_cfcfd48f_fk_itemdisplay_Id` (`ItemDisplayId`),
  KEY `item_SubCategoryId_f7504282_fk_subcategory_Id` (`SubCategoryId`),
  CONSTRAINT `item_ItemDisplayId_cfcfd48f_fk_itemdisplay_Id` FOREIGN KEY (`ItemDisplayId`) REFERENCES `itemdisplay` (`Id`),
  CONSTRAINT `item_SubCategoryId_f7504282_fk_subcategory_Id` FOREIGN KEY (`SubCategoryId`) REFERENCES `subcategory` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,'Pizza','<p><strong>pizza</strong></p>\r\n',1,30,'2019080510363749057787Y1I3JF0_aftab.ansari.jpeg','2019-08-05 05:36:37.573606',1,1);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itemdisplay`
--

DROP TABLE IF EXISTS `itemdisplay`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itemdisplay` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `DisplayType` varchar(50) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `itemdisplay_UserId_45936e6b_fk_user_Id` (`UserId`),
  CONSTRAINT `itemdisplay_UserId_45936e6b_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itemdisplay`
--

LOCK TABLES `itemdisplay` WRITE;
/*!40000 ALTER TABLE `itemdisplay` DISABLE KEYS */;
INSERT INTO `itemdisplay` VALUES (1,'Fast Food',1);
/*!40000 ALTER TABLE `itemdisplay` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itemofferoption`
--

DROP TABLE IF EXISTS `itemofferoption`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itemofferoption` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `CustomOffer` varchar(225) NOT NULL,
  `Price` int(11) NOT NULL,
  `StartTimeRange` datetime(6) NOT NULL,
  `EndTimeRange` datetime(6) NOT NULL,
  `CreatedDate` datetime(6) NOT NULL,
  `ItemId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `itemofferoption_ItemId_25a03c09_fk_item_Id` (`ItemId`),
  CONSTRAINT `itemofferoption_ItemId_25a03c09_fk_item_Id` FOREIGN KEY (`ItemId`) REFERENCES `item` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itemofferoption`
--

LOCK TABLES `itemofferoption` WRITE;
/*!40000 ALTER TABLE `itemofferoption` DISABLE KEYS */;
/*!40000 ALTER TABLE `itemofferoption` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itemofferoptions`
--

DROP TABLE IF EXISTS `itemofferoptions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itemofferoptions` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `CustomOffer` varchar(225) NOT NULL,
  `Price` int(11) NOT NULL,
  `TimeRange` datetime(6) NOT NULL,
  `ItemId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `itemofferoptions_ItemId_f2058e88_fk_item_Id` (`ItemId`),
  CONSTRAINT `itemofferoptions_ItemId_f2058e88_fk_item_Id` FOREIGN KEY (`ItemId`) REFERENCES `item` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itemofferoptions`
--

LOCK TABLES `itemofferoptions` WRITE;
/*!40000 ALTER TABLE `itemofferoptions` DISABLE KEYS */;
/*!40000 ALTER TABLE `itemofferoptions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itemorder`
--

DROP TABLE IF EXISTS `itemorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itemorder` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `ItemName` varchar(225) NOT NULL,
  `VariationName` varchar(225) NOT NULL,
  `ItemPrice` int(11) NOT NULL,
  `ItemQuantity` int(11) NOT NULL,
  `Total` int(11) NOT NULL,
  `OrderDate` datetime(6) NOT NULL,
  `OderId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `itemorder_OderId_5308a3e8_fk_orders_Id` (`OderId`),
  CONSTRAINT `itemorder_OderId_5308a3e8_fk_orders_Id` FOREIGN KEY (`OderId`) REFERENCES `orders` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itemorder`
--

LOCK TABLES `itemorder` WRITE;
/*!40000 ALTER TABLE `itemorder` DISABLE KEYS */;
/*!40000 ALTER TABLE `itemorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itemvariation`
--

DROP TABLE IF EXISTS `itemvariation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itemvariation` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(255) NOT NULL,
  `Description` varchar(255) NOT NULL,
  `Discount` int(11) NOT NULL,
  `Price` int(11) NOT NULL,
  `ItemId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `ItemVariation_ItemId_c3cccbd3_fk_item_Id` (`ItemId`),
  CONSTRAINT `ItemVariation_ItemId_c3cccbd3_fk_item_Id` FOREIGN KEY (`ItemId`) REFERENCES `item` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itemvariation`
--

LOCK TABLES `itemvariation` WRITE;
/*!40000 ALTER TABLE `itemvariation` DISABLE KEYS */;
INSERT INTO `itemvariation` VALUES (1,'Small','Small',2,22,1),(2,'Medium','medium',3,33,1);
/*!40000 ALTER TABLE `itemvariation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `languages`
--

DROP TABLE IF EXISTS `languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `languages` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `LanguageName` varchar(20) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `languages`
--

LOCK TABLES `languages` WRITE;
/*!40000 ALTER TABLE `languages` DISABLE KEYS */;
/*!40000 ALTER TABLE `languages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Address` varchar(225) NOT NULL,
  `city` varchar(20) NOT NULL,
  `PostCode` int(11) NOT NULL,
  `State` varchar(20) NOT NULL,
  `Country` varchar(20) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `location_UserId_262f05b4_fk_user_Id` (`UserId`),
  CONSTRAINT `location_UserId_262f05b4_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member` (
  `Sr_No` int(11) NOT NULL AUTO_INCREMENT,
  `DateOfBirth` datetime(6) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `QRCode` longtext NOT NULL,
  `UserId` int(11) NOT NULL,
  `VendorId` int(11) NOT NULL,
  PRIMARY KEY (`Sr_No`),
  KEY `member_UserId_06d90b0b_fk_user_Id` (`UserId`),
  KEY `member_VendorId_5a044e0e_fk_VendorStaff_Id` (`VendorId`),
  CONSTRAINT `member_UserId_06d90b0b_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`),
  CONSTRAINT `member_VendorId_5a044e0e_fk_VendorStaff_Id` FOREIGN KEY (`VendorId`) REFERENCES `vendorstaff` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membership`
--

DROP TABLE IF EXISTS `membership`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `membership` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `PackageId` int(11) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `membership_PackageId_ef3ff02c_fk_subscription_Id` (`PackageId`),
  KEY `membership_UserId_ba59db5c_fk_user_Id` (`UserId`),
  CONSTRAINT `membership_PackageId_ef3ff02c_fk_subscription_Id` FOREIGN KEY (`PackageId`) REFERENCES `subscription` (`Id`),
  CONSTRAINT `membership_UserId_ba59db5c_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membership`
--

LOCK TABLES `membership` WRITE;
/*!40000 ALTER TABLE `membership` DISABLE KEYS */;
/*!40000 ALTER TABLE `membership` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `MenuId` int(11) NOT NULL,
  `Name` varchar(225) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `ItemId` int(11) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `menu_ItemId_0b1c9b89_fk_item_Id` (`ItemId`),
  KEY `menu_UserId_678917e0_fk_user_Id` (`UserId`),
  CONSTRAINT `menu_ItemId_0b1c9b89_fk_item_Id` FOREIGN KEY (`ItemId`) REFERENCES `item` (`Id`),
  CONSTRAINT `menu_UserId_678917e0_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `MessageHead` varchar(225) NOT NULL,
  `MessageBody` varchar(225) NOT NULL,
  `EventDate` datetime(6) NOT NULL,
  `Type` varchar(20) NOT NULL,
  `ReceiverId` int(11) NOT NULL,
  `SenderId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `messages_ReceiverId_25496035_fk_user_Id` (`ReceiverId`),
  KEY `messages_SenderId_33be8a86_fk_messagesender_Id` (`SenderId`),
  CONSTRAINT `messages_ReceiverId_25496035_fk_user_Id` FOREIGN KEY (`ReceiverId`) REFERENCES `user` (`Id`),
  CONSTRAINT `messages_SenderId_33be8a86_fk_messagesender_Id` FOREIGN KEY (`SenderId`) REFERENCES `messagesender` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messagesender`
--

DROP TABLE IF EXISTS `messagesender`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messagesender` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `messagesender_UserId_fcc35838_fk_user_Id` (`UserId`),
  CONSTRAINT `messagesender_UserId_fcc35838_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messagesender`
--

LOCK TABLES `messagesender` WRITE;
/*!40000 ALTER TABLE `messagesender` DISABLE KEYS */;
/*!40000 ALTER TABLE `messagesender` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `TotalAmount` int(11) NOT NULL,
  `OrderType` varchar(50) NOT NULL,
  `PaymentStatus` varchar(50) NOT NULL,
  `TotalTime` int(11) NOT NULL,
  `DiscountAmount` int(11) NOT NULL,
  `MemberId` int(11) NOT NULL,
  `VendorId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `orders_MemberId_218b9fea_fk_user_Id` (`MemberId`),
  KEY `orders_VendorId_d9d6f098_fk_venderorders_Id` (`VendorId`),
  CONSTRAINT `orders_MemberId_218b9fea_fk_user_Id` FOREIGN KEY (`MemberId`) REFERENCES `user` (`Id`),
  CONSTRAINT `orders_VendorId_d9d6f098_fk_venderorders_Id` FOREIGN KEY (`VendorId`) REFERENCES `venderorders` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `packages`
--

DROP TABLE IF EXISTS `packages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `packages` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `PackageName` varchar(225) NOT NULL,
  `PackageDetail` varchar(225) NOT NULL,
  `PackageCharges` int(11) NOT NULL,
  `PackageDuration` int(11) NOT NULL,
  `PackageType` varchar(225) NOT NULL,
  `CreatedDate` datetime(6) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `packages`
--

LOCK TABLES `packages` WRITE;
/*!40000 ALTER TABLE `packages` DISABLE KEYS */;
INSERT INTO `packages` VALUES (1,'Gold Berg','<p>THIS IS THE DESCRIPTION OF PACKACKAGE</p>\n',200,3,'Gold','2019-08-06 06:55:55.248240');
/*!40000 ALTER TABLE `packages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_gateway`
--

DROP TABLE IF EXISTS `payment_gateway`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment_gateway` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Paypal_Mail` varchar(225) NOT NULL,
  `Strip_Mail` varchar(225) NOT NULL,
  `Bank_Name` varchar(225) NOT NULL,
  `Account_Name` varchar(225) NOT NULL,
  `Account_Number` varchar(225) NOT NULL,
  `IBAN_Number` varchar(225) NOT NULL,
  `Credit_Card_No` varchar(225) NOT NULL,
  `Type` varchar(225) NOT NULL,
  `Status` varchar(225) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_gateway`
--

LOCK TABLES `payment_gateway` WRITE;
/*!40000 ALTER TABLE `payment_gateway` DISABLE KEYS */;
INSERT INTO `payment_gateway` VALUES (2,'','mystripemail@gmail.com','','','','','','strip','inactive'),(3,'','','HBL','M. Aftab','023034982349','lsfsdl02498348923','','Bank','inactive');
/*!40000 ALTER TABLE `payment_gateway` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qareplies`
--

DROP TABLE IF EXISTS `qareplies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `qareplies` (
  `ReplyId` int(11) NOT NULL AUTO_INCREMENT,
  `QuestionId` int(11) NOT NULL,
  `ReplyText` varchar(250) NOT NULL,
  `ReplyFile` varchar(150) NOT NULL,
  `ReplyBy` varchar(150) NOT NULL,
  `ReplyDate` datetime(6) NOT NULL,
  `ReadReply` int(11) NOT NULL,
  `Userid` int(11) NOT NULL,
  PRIMARY KEY (`ReplyId`),
  KEY `QAReplies_Userid_527909e4_fk_user_Id` (`Userid`),
  CONSTRAINT `QAReplies_Userid_527909e4_fk_user_Id` FOREIGN KEY (`Userid`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qareplies`
--

LOCK TABLES `qareplies` WRITE;
/*!40000 ALTER TABLE `qareplies` DISABLE KEYS */;
/*!40000 ALTER TABLE `qareplies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qasupports`
--

DROP TABLE IF EXISTS `qasupports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `qasupports` (
  `QuestionId` int(11) NOT NULL AUTO_INCREMENT,
  `QuestionTitle` varchar(150) NOT NULL,
  `QuestionText` varchar(250) NOT NULL,
  `QuestionFile` varchar(250) NOT NULL,
  `QuestionBy` varchar(150) NOT NULL,
  `Priority` varchar(50) NOT NULL,
  `Status` varchar(50) NOT NULL,
  `QuestionDate` datetime(6) NOT NULL,
  `ReadQuestion` int(11) NOT NULL,
  `Userid` int(11) NOT NULL,
  PRIMARY KEY (`QuestionId`),
  KEY `QASupports_Userid_b17928b7_fk_user_Id` (`Userid`),
  CONSTRAINT `QASupports_Userid_b17928b7_fk_user_Id` FOREIGN KEY (`Userid`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qasupports`
--

LOCK TABLES `qasupports` WRITE;
/*!40000 ALTER TABLE `qasupports` DISABLE KEYS */;
/*!40000 ALTER TABLE `qasupports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rechargehistory`
--

DROP TABLE IF EXISTS `rechargehistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rechargehistory` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `EventDate` datetime(6) NOT NULL,
  `RechargeType` varchar(225) NOT NULL,
  `Amount` int(11) NOT NULL,
  `RechergePurpose` varchar(225) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `rechargehistory_UserId_543e07e1_fk_user_Id` (`UserId`),
  CONSTRAINT `rechargehistory_UserId_543e07e1_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rechargehistory`
--

LOCK TABLES `rechargehistory` WRITE;
/*!40000 ALTER TABLE `rechargehistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `rechargehistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sms_setup`
--

DROP TABLE IF EXISTS `sms_setup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sms_setup` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `ServiceName` varchar(225) NOT NULL,
  `Api_key` varchar(225) NOT NULL,
  `CostToVendor` int(11) NOT NULL,
  `MinimumRefill` int(11) NOT NULL,
  `RechargeAlert` int(11) NOT NULL,
  `Status` varchar(225) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sms_setup`
--

LOCK TABLES `sms_setup` WRITE;
/*!40000 ALTER TABLE `sms_setup` DISABLE KEYS */;
INSERT INTO `sms_setup` VALUES (1,'SMS PK','apikeylwerjlk2343',20,5,20,'Active');
/*!40000 ALTER TABLE `sms_setup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smspackages`
--

DROP TABLE IF EXISTS `smspackages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smspackages` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `SMSPackageName` varchar(225) NOT NULL,
  `SMSPackageDetail` varchar(225) NOT NULL,
  `PackageCharges` int(11) NOT NULL,
  `SMSPackageDuration` varchar(225) NOT NULL,
  `SMSPackageType` varchar(225) NOT NULL,
  `TotalSMS` int(11) NOT NULL,
  `CreatedDate` datetime(6) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smspackages`
--

LOCK TABLES `smspackages` WRITE;
/*!40000 ALTER TABLE `smspackages` DISABLE KEYS */;
INSERT INTO `smspackages` VALUES (1,'SMS PACKAGE','<p><strong>This is the description of SMS packages</strong></p>\n',200,'3','Goldd',5000,'2019-08-06 07:20:14.191197');
/*!40000 ALTER TABLE `smspackages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smssubscription`
--

DROP TABLE IF EXISTS `smssubscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smssubscription` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `SubscriptionDate` datetime(6) NOT NULL,
  `ExpiryDate` datetime(6) NOT NULL,
  `AutoRenew` int(11) NOT NULL,
  `FreeTrail` int(11) NOT NULL,
  `ExpiryAlert` int(11) NOT NULL,
  `RenewConfirmation` int(11) NOT NULL,
  `PackageId` int(11) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `smssubscription_PackageId_3c555df6_fk_SMSPackages_Id` (`PackageId`),
  KEY `smssubscription_UserId_a245a966_fk_user_Id` (`UserId`),
  CONSTRAINT `smssubscription_PackageId_3c555df6_fk_SMSPackages_Id` FOREIGN KEY (`PackageId`) REFERENCES `smspackages` (`Id`),
  CONSTRAINT `smssubscription_UserId_a245a966_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smssubscription`
--

LOCK TABLES `smssubscription` WRITE;
/*!40000 ALTER TABLE `smssubscription` DISABLE KEYS */;
/*!40000 ALTER TABLE `smssubscription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staff` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Privilege` varchar(20) NOT NULL,
  `Department` varchar(20) NOT NULL,
  `UserId` int(11) NOT NULL,
  `VendorId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `staff_UserId_8937935a_fk_user_Id` (`UserId`),
  KEY `staff_VendorId_9ca8584a_fk_VendorStaff_Id` (`VendorId`),
  CONSTRAINT `staff_UserId_8937935a_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`),
  CONSTRAINT `staff_VendorId_9ca8584a_fk_VendorStaff_Id` FOREIGN KEY (`VendorId`) REFERENCES `vendorstaff` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subcategory`
--

DROP TABLE IF EXISTS `subcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subcategory` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `SubCategoryName` varchar(50) NOT NULL,
  `TimeRange` datetime(6) NOT NULL,
  `CreatedDate` datetime(6) NOT NULL,
  `CategoryId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `subcategory_CategoryId_d843adc9_fk_category_Id` (`CategoryId`),
  CONSTRAINT `subcategory_CategoryId_d843adc9_fk_category_Id` FOREIGN KEY (`CategoryId`) REFERENCES `category` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subcategory`
--

LOCK TABLES `subcategory` WRITE;
/*!40000 ALTER TABLE `subcategory` DISABLE KEYS */;
INSERT INTO `subcategory` VALUES (1,'Sarina','2019-08-28 10:55:00.000000','2019-08-05 05:35:29.741919',2),(2,'Habib','2019-08-28 10:55:00.000000','2019-08-05 05:35:35.578937',2);
/*!40000 ALTER TABLE `subcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription`
--

DROP TABLE IF EXISTS `subscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `SubscriptionDate` datetime(6) NOT NULL,
  `ExpiryDate` datetime(6) NOT NULL,
  `AutoRenew` int(11) NOT NULL,
  `FreeTrail` int(11) NOT NULL,
  `ExpiryAlert` int(11) NOT NULL,
  `RenewConfirmation` int(11) NOT NULL,
  `PackageId` int(11) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `subscription_PackageId_5e700a56_fk_packages_Id` (`PackageId`),
  KEY `subscription_UserId_1ce2b39a_fk_user_Id` (`UserId`),
  CONSTRAINT `subscription_PackageId_5e700a56_fk_packages_Id` FOREIGN KEY (`PackageId`) REFERENCES `packages` (`Id`),
  CONSTRAINT `subscription_UserId_1ce2b39a_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription`
--

LOCK TABLES `subscription` WRITE;
/*!40000 ALTER TABLE `subscription` DISABLE KEYS */;
/*!40000 ALTER TABLE `subscription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `superadmin`
--

DROP TABLE IF EXISTS `superadmin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `superadmin` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `UserName` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `superadmin`
--

LOCK TABLES `superadmin` WRITE;
/*!40000 ALTER TABLE `superadmin` DISABLE KEYS */;
/*!40000 ALTER TABLE `superadmin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tables`
--

DROP TABLE IF EXISTS `tables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tables` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `TableType` varchar(50) NOT NULL,
  `TableDescription` varchar(225) NOT NULL,
  `TableCapacity` int(11) NOT NULL,
  `Availible` varchar(50) NOT NULL,
  `QRCode` varchar(225) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `tables_UserId_2886d3f8` (`UserId`),
  CONSTRAINT `tables_UserId_2886d3f8_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tables`
--

LOCK TABLES `tables` WRITE;
/*!40000 ALTER TABLE `tables` DISABLE KEYS */;
/*!40000 ALTER TABLE `tables` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaction` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Mode` varchar(225) NOT NULL,
  `Amount` int(11) NOT NULL,
  `Date` datetime(6) NOT NULL,
  `Member` int(11) NOT NULL,
  `Waiter` int(11) NOT NULL,
  `Cashier` int(11) NOT NULL,
  `Discount` varchar(225) NOT NULL,
  `OrderId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `transaction_OrderId_1cf128ae_fk_orders_Id` (`OrderId`),
  CONSTRAINT `transaction_OrderId_1cf128ae_fk_orders_Id` FOREIGN KEY (`OrderId`) REFERENCES `orders` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tutorial`
--

DROP TABLE IF EXISTS `tutorial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tutorial` (
  `tutorial_id` int(11) NOT NULL AUTO_INCREMENT,
  `long_text` longtext NOT NULL,
  `feature_image` longtext NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_by` int(11) NOT NULL,
  `group` varchar(30) NOT NULL,
  `type` int(11) NOT NULL,
  PRIMARY KEY (`tutorial_id`),
  KEY `tutorial_created_by_8b10d41d_fk_user_Id` (`created_by`),
  KEY `tutorial_type_c0c5b2a7_fk_tutorialtype_id` (`type`),
  CONSTRAINT `tutorial_created_by_8b10d41d_fk_user_Id` FOREIGN KEY (`created_by`) REFERENCES `user` (`Id`),
  CONSTRAINT `tutorial_type_c0c5b2a7_fk_tutorialtype_id` FOREIGN KEY (`type`) REFERENCES `tutorialtype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tutorial`
--

LOCK TABLES `tutorial` WRITE;
/*!40000 ALTER TABLE `tutorial` DISABLE KEYS */;
INSERT INTO `tutorial` VALUES (1,'<p><strong>This is the dummy tutorials descriptions.&nbsp;</strong></p>\r\n','20190805092338457081SXN8LAZ87.png','2019-08-05 09:23:38.460081','2019-08-05 09:24:35.251008','This tutorials is tutorial ',1,'vendor',1),(2,'<p><strong>Customer</strong></p>\r\n','20190805100500321013YCJ56DDYX.jpeg','2019-08-05 10:05:00.328022','2019-08-05 10:05:00.328022','Customer Tutorial',1,'customer',1),(3,'<p><em>dsfdsf</em></p>\r\n','20190805100742267453HYYOUD2ZV.jpeg','2019-08-05 10:07:42.279448','2019-08-05 10:07:42.279448','sdfgsdfsdfsdf',1,'customer',1);
/*!40000 ALTER TABLE `tutorial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tutorialtype`
--

DROP TABLE IF EXISTS `tutorialtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tutorialtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tutorialtype`
--

LOCK TABLES `tutorialtype` WRITE;
/*!40000 ALTER TABLE `tutorialtype` DISABLE KEYS */;
INSERT INTO `tutorialtype` VALUES (1,'General');
/*!40000 ALTER TABLE `tutorialtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `UserId` varchar(225) NOT NULL,
  `DisplayName` varchar(225) NOT NULL,
  `Email` varchar(225) NOT NULL,
  `Mobile` varchar(30) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Image` varchar(50) NOT NULL,
  `RegisterDate` datetime(6) NOT NULL,
  `LastUpdatedDate` datetime(6) NOT NULL,
  `Status` varchar(20) NOT NULL,
  `ForgotPassword` varchar(10) NOT NULL,
  `UserType` varchar(50) NOT NULL,
  `Balance` int(11) NOT NULL,
  `ExpiryDate` datetime(6) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=177 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'SP0001','Aftab Ansari','superadmin','+5212321828','admin','','2019-07-04 21:04:07.020730','2019-07-04 21:04:07.020730','','','SuperAdmin',100,'2019-07-22 23:10:43.000000'),(2,'VQE0000001P','kyfwue','kyfwue@gmail.com','+210662310586','123456789','','2019-07-04 21:04:07.067604','2019-07-04 21:04:07.067604','','','Vendor',100,'2019-07-22 23:10:43.000000'),(3,'VEI0000002M','bjisnf','bjisnf@gmail.com','+1466365119','123456789','','2019-07-04 21:04:07.130104','2019-07-04 21:04:07.130104','','','Vendor',100,'2019-07-22 23:10:43.000000'),(4,'VFC0000003G','niyang','niyang@gmail.com','+8312369428','123456789','','2019-07-04 21:04:07.176979','2019-07-04 21:04:07.176979','','','Vendor',100,'2019-07-22 23:10:43.000000'),(5,'VEW0000004L','publfv','publfv@gmail.com','+313579101077','123456789','','2019-07-04 21:04:07.255096','2019-07-04 21:04:07.255096','','','Vendor',100,'2019-07-22 23:10:43.000000'),(6,'VSA0000005C','helqdi','helqdi@gmail.com','+3142331635','123456789','','2019-07-04 21:04:07.317593','2019-07-04 21:04:07.317593','','','Vendor',100,'2019-07-22 23:10:43.000000'),(7,'VYK0000006I','bqpisn','bqpisn@gmail.com','+7164917814','123456789','','2019-07-04 21:04:07.364456','2019-07-04 21:04:07.364456','','','Vendor',100,'2019-07-22 23:10:43.000000'),(8,'VAD0000007Q','qfwzuf','qfwzuf@gmail.com','+10881856935','123456789','','2019-07-04 21:04:07.489448','2019-07-04 21:04:07.489448','','','Vendor',100,'2019-07-22 23:10:43.000000'),(9,'VCC0000008K','oxcdsq','oxcdsq@gmail.com','+107129311046','123456789','','2019-07-04 21:04:07.567567','2019-07-04 21:04:07.567567','','','Vendor',100,'2019-07-22 23:10:43.000000'),(10,'VBE0000009T','rnhehh','rnhehh@gmail.com','+36892241097','123456789','','2019-07-04 21:04:07.630063','2019-07-04 21:04:07.630063','','','Vendor',100,'2019-07-22 23:10:43.000000'),(11,'VXZ0000010M','mdjvfr','mdjvfr@gmail.com','+11038826748','123456789','','2019-07-04 21:04:44.998187','2019-07-04 21:04:44.998187','','','Vendor',100,'2019-07-22 23:10:43.000000'),(12,'VLF0000011A','gasmqa','gasmqa@gmail.com','+106471101133','123456789','','2019-07-04 21:04:45.091933','2019-07-04 21:04:45.091933','','','Vendor',100,'2019-07-22 23:10:43.000000'),(13,'VQE0000012T','qnowpx','qnowpx@gmail.com','+19231068114','123456789','','2019-07-04 21:04:45.123178','2019-07-04 21:04:45.123178','','','Vendor',100,'2019-07-22 23:10:43.000000'),(14,'VHP0000013V','eydoyb','eydoyb@gmail.com','+10596514325','123456789','','2019-07-04 21:04:45.216926','2019-07-04 21:04:45.216926','','','Vendor',100,'2019-07-22 23:10:43.000000'),(15,'VKT0000014T','kadvqn','kadvqn@gmail.com','+104105944615','123456789','','2019-07-04 21:04:45.373162','2019-07-04 21:04:45.373162','','','Vendor',100,'2019-07-22 23:10:43.000000'),(16,'VPO0000015A','nmlgmw','nmlgmw@gmail.com','+72102213572','123456789','','2019-07-04 21:04:45.466905','2019-07-04 21:04:45.466905','','','Vendor',100,'2019-07-22 23:10:43.000000'),(17,'VPS0000016D','wgcblp','wgcblp@gmail.com','+4792735121','123456789','','2019-07-04 21:04:45.650080','2019-07-04 21:04:45.650080','','','Vendor',100,'2019-07-22 23:10:43.000000'),(18,'VEC0000017D','izaokm','izaokm@gmail.com','+5834267959','123456789','','2019-07-04 21:04:45.738230','2019-07-04 21:04:45.738230','','','Vendor',100,'2019-07-22 23:10:43.000000'),(19,'VFD0000018W','qelrln','qelrln@gmail.com','+51061118856','123456789','','2019-07-04 21:04:45.931843','2019-07-04 21:04:45.931843','','','Vendor',100,'2019-07-22 23:10:43.000000'),(20,'VXE0000019I','rxmfoq','rxmfoq@gmail.com','+3897921352','123456789','','2019-07-04 21:04:46.055884','2019-07-04 21:04:46.055884','','','Vendor',100,'2019-07-22 23:10:43.000000'),(21,'VGZ0000020B','ABC','jpxcvh@gmail.com','+948101043526','danian','','2019-07-04 21:04:46.208496','2019-07-11 10:02:23.648434','Suspended','','Vendor',100,'2019-07-22 23:10:43.000000'),(22,'VVZ0000021I','cjtukp','cjtukp@gmail.com','+68102387674','123456789','','2019-07-04 21:04:46.299722','2019-07-04 21:04:46.299722','','','Vendor',100,'2019-07-22 23:10:43.000000'),(23,'VNT0000022H','fjgtpj','fjgtpj@gmail.com','+269341021014','123456789','','2019-07-04 21:04:46.395923','2019-07-04 21:04:46.395923','','','Vendor',100,'2019-07-22 23:10:43.000000'),(24,'VCM0000023W','foadtc','foadtc@gmail.com','+888101910315','123456789','','2019-07-04 21:04:46.496227','2019-07-04 21:04:46.496227','','','Vendor',100,'2019-07-22 23:10:43.000000'),(25,'VLS0000024U','qammlh','qammlh@gmail.com','+3826446925','123456789','','2019-07-04 21:04:46.596523','2019-07-04 21:04:46.596523','','','Vendor',100,'2019-07-22 23:10:43.000000'),(26,'VKV0000025T','shfhoq','shfhoq@gmail.com','+683101059552','123456789','','2019-07-04 21:04:46.696803','2019-07-04 21:04:46.696803','','','Vendor',100,'2019-07-22 23:10:43.000000'),(27,'VDI0000026B','ojmggl','ojmggl@gmail.com','+41187102143','123456789','','2019-07-04 21:04:46.781499','2019-07-04 21:04:46.781499','','','Vendor',100,'2019-07-22 23:10:43.000000'),(28,'VZN0000027W','Danian','danian123@gmail.com','+92348863568','12345','','2019-07-04 21:04:46.882013','2019-07-10 04:06:29.775674','','','Vendor',100,'2019-07-22 23:10:43.000000'),(29,'VSQ0000028F','jwfeme','jwfeme@gmail.com','+8721256939','123456789','','2019-07-04 21:04:47.035339','2019-07-04 21:04:47.035339','','','Vendor',100,'2019-07-22 23:10:43.000000'),(30,'VHL0000029B','tfgxrm','tfgxrm@gmail.com','+2634358936','123456789','','2019-07-04 21:04:47.235538','2019-07-04 21:04:47.235538','','','Vendor',100,'2019-07-22 23:10:43.000000'),(31,'VUW0000030Z','qivfcz','qivfcz@gmail.com','+1269282859','123456789','','2019-07-04 21:04:47.320168','2019-07-04 21:04:47.320168','','','Vendor',100,'2019-07-22 23:10:43.000000'),(32,'VSD0000031D','yxrxgl','yxrxgl@gmail.com','+7896613881','123456789','','2019-07-04 21:04:47.451697','2019-07-04 21:04:47.451697','','','Vendor',100,'2019-07-22 23:10:43.000000'),(33,'VWM0000032V','jtgsvx','jtgsvx@gmail.com','+10179195354','123456789','','2019-07-04 21:04:47.614544','2019-07-04 21:04:47.614544','','','Vendor',100,'2019-07-22 23:10:43.000000'),(34,'VOA0000033V','ooxmxw','ooxmxw@gmail.com','+5327991235','123456789','','2019-07-04 21:04:47.699281','2019-07-04 21:04:47.699281','','','Vendor',100,'2019-07-22 23:10:43.000000'),(35,'VSY0000034I','hdiozr','hdiozr@gmail.com','+3741899643','123456789','','2019-07-04 21:04:47.783883','2019-07-04 21:04:47.783883','','','Vendor',100,'2019-07-22 23:10:43.000000'),(36,'VJG0000035X','mhremp','mhremp@gmail.com','+45110522493','123456789','','2019-07-04 21:04:47.899809','2019-07-04 21:04:47.899809','','','Vendor',100,'2019-07-22 23:10:43.000000'),(37,'VUW0000036S','joqkkb','joqkkb@gmail.com','+6838938724','123456789','','2019-07-04 21:04:47.984472','2019-07-04 21:04:47.984472','','','Vendor',100,'2019-07-22 23:10:43.000000'),(38,'VQO0000037Y','wruzln','wruzln@gmail.com','+7163753257','123456789','','2019-07-04 21:04:48.254148','2019-07-04 21:04:48.254148','','','Vendor',100,'2019-07-22 23:10:43.000000'),(39,'VQM0000038B','nnwjfu','nnwjfu@gmail.com','+55751072387','123456789','','2019-07-04 21:04:48.470338','2019-07-04 21:04:48.470338','','','Vendor',100,'2019-07-22 23:10:43.000000'),(40,'VHJ0000039L','crffzd','crffzd@gmail.com','+931076261099','123456789','','2019-07-04 21:04:48.570628','2019-07-04 21:04:48.570628','','','Vendor',100,'2019-07-22 23:10:43.000000'),(41,'VXD0000040N','apvygh','apvygh@gmail.com','+86682105565','123456789','','2019-07-04 21:04:48.702172','2019-07-04 21:04:48.702172','','','Vendor',100,'2019-07-22 23:10:43.000000'),(42,'VRT0000041X','ujyejl','ujyejl@gmail.com','+10382937259','123456789','','2019-07-04 21:04:48.802472','2019-07-04 21:04:48.802472','','','Vendor',100,'2019-07-22 23:10:43.000000'),(43,'VBP0000042X','nxupfn','nxupfn@gmail.com','+4566659861','123456789','','2019-07-04 21:04:48.871488','2019-07-04 21:04:48.871488','','','Vendor',100,'2019-07-22 23:10:43.000000'),(44,'VIH0000043F','hgbjpw','hgbjpw@gmail.com','+10955513963','123456789','','2019-07-04 21:04:48.956190','2019-07-04 21:04:48.956190','','','Vendor',100,'2019-07-22 23:10:43.000000'),(45,'VLS0000044O','ncclsv','ncclsv@gmail.com','+24955976910','123456789','','2019-07-04 21:04:49.056582','2019-07-04 21:04:49.056582','','','Vendor',100,'2019-07-22 23:10:43.000000'),(46,'VUH0000045T','qakuau','qakuau@gmail.com','+1097481089106','123456789','','2019-07-04 21:04:49.203725','2019-07-04 21:04:49.203725','','','Vendor',100,'2019-07-22 23:10:43.000000'),(47,'VWV0000046J','okgelq','okgelq@gmail.com','+9110381011096','123456789','','2019-07-04 21:04:49.288459','2019-07-04 21:04:49.288459','','','Vendor',100,'2019-07-22 23:10:43.000000'),(48,'VXE0000047M','qdhudq','qdhudq@gmail.com','+21083677431','123456789','','2019-07-04 21:04:49.426594','2019-07-04 21:04:49.426594','','','Vendor',100,'2019-07-22 23:10:43.000000'),(49,'VCK0000048N','uovwea','uovwea@gmail.com','+10941123325','123456789','','2019-07-04 21:04:49.573832','2019-07-04 21:04:49.573832','','','Vendor',100,'2019-07-22 23:10:43.000000'),(50,'VXE0000049Z','noczof','noczof@gmail.com','+55695361106','123456789','','2019-07-04 21:04:49.689731','2019-07-04 21:04:49.689731','','','Vendor',100,'2019-07-22 23:10:43.000000'),(51,'VJK0000050W','ghyvui','ghyvui@gmail.com','+10986825479','123456789','','2019-07-04 21:04:49.774540','2019-07-04 21:04:49.774540','','','Vendor',100,'2019-07-22 23:10:43.000000'),(52,'VXD0000051J','uahpoj','uahpoj@gmail.com','+56862261610','123456789','','2019-07-04 21:04:49.890489','2019-07-04 21:04:49.890489','','','Vendor',100,'2019-07-22 23:10:43.000000'),(53,'VSY0000052J','jzwvsc','jzwvsc@gmail.com','+4398653436','123456789','','2019-07-04 21:04:50.206989','2019-07-04 21:04:50.206989','','','Vendor',100,'2019-07-22 23:10:43.000000'),(54,'VCD0000053G','Jawad','jawadrana2015@gmail.com','3007687453','123456789','','2019-07-04 21:04:50.345075','2019-07-25 02:38:43.121220','Active','','Vendor',100,'2019-07-22 23:10:43.000000'),(55,'VJJ0000054K','rqcnzm','rqcnzm@gmail.com','+2261289528','123456789','','2019-07-04 21:04:50.507890','2019-07-04 21:04:50.507890','','','Vendor',100,'2019-07-22 23:10:43.000000'),(56,'VCM0000055H','yjunqp','yjunqp@gmail.com','+7271115728','123456789','','2019-07-04 21:04:50.661537','2019-07-04 21:04:50.661537','','','Vendor',100,'2019-07-22 23:10:43.000000'),(57,'VVJ0000056K','nzceyq','nzceyq@gmail.com','+15510243331','123456789','','2019-07-04 21:04:50.882423','2019-07-04 21:04:50.882423','','','Vendor',100,'2019-07-22 23:10:43.000000'),(58,'VGP0000057A','mitzrl','mitzrl@gmail.com','+1289134178','123456789','','2019-07-04 21:04:50.982714','2019-07-04 21:04:50.982714','','','Vendor',100,'2019-07-22 23:10:43.000000'),(59,'VCA0000058Y','zauvel','zauvel@gmail.com','+69841013812','123456789','','2019-07-04 21:04:51.267561','2019-07-04 21:04:51.267561','','','Vendor',100,'2019-07-22 23:10:43.000000'),(60,'VXQ0000059V','axpbgu','axpbgu@gmail.com','+18288195510','123456789','','2019-07-04 21:04:51.483786','2019-07-04 21:04:51.483786','','','Vendor',100,'2019-07-22 23:10:43.000000'),(61,'VAE0000060X','dhddup','dhddup@gmail.com','+61053846885','123456789','','2019-07-04 21:04:51.552793','2019-07-04 21:04:51.552793','','','Vendor',100,'2019-07-22 23:10:43.000000'),(62,'VZY0000061D','ujsrkv','ujsrkv@gmail.com','+171048537102','123456789','','2019-07-04 21:04:51.630925','2019-07-04 21:04:51.630925','','','Vendor',100,'2019-07-22 23:10:43.000000'),(63,'VEM0000062R','ajusxu','ajusxu@gmail.com','+78567231033','123456789','','2019-07-04 21:04:51.746912','2019-07-04 21:04:51.746912','','','Vendor',100,'2019-07-22 23:10:43.000000'),(64,'VTT0000063G','wpysbl','wpysbl@gmail.com','+7159355217','123456789','','2019-07-04 21:04:51.969110','2019-07-04 21:04:51.969110','','','Vendor',100,'2019-07-22 23:10:43.000000'),(65,'VWE0000064N','qglkcb','qglkcb@gmail.com','+610878857610','123456789','','2019-07-04 21:04:52.285549','2019-07-04 21:04:52.285549','','','Vendor',100,'2019-07-22 23:10:43.000000'),(66,'VJY0000065D','yomzwn','yomzwn@gmail.com','+3483673223','123456789','','2019-07-04 21:04:52.454851','2019-07-04 21:04:52.454851','','','Vendor',100,'2019-07-22 23:10:43.000000'),(67,'VPF0000066V','gyqqsp','gyqqsp@gmail.com','+63910656525','123456789','','2019-07-04 21:04:52.532990','2019-07-04 21:04:52.532990','','','Vendor',100,'2019-07-22 23:10:43.000000'),(68,'VTT0000067B','otoghf','otoghf@gmail.com','+41466228410','123456789','','2019-07-04 21:04:52.671051','2019-07-04 21:04:52.671051','','','Vendor',100,'2019-07-22 23:10:43.000000'),(69,'VMZ0000068W','izxtqg','izxtqg@gmail.com','+11086958473','123456789','','2019-07-04 21:04:52.755722','2019-07-04 21:04:52.755722','','','Vendor',100,'2019-07-22 23:10:43.000000'),(70,'VWZ0000069M','oooyar','oooyar@gmail.com','+2264123391','123456789','','2019-07-04 21:04:53.147953','2019-07-04 21:04:53.147953','','','Vendor',100,'2019-07-22 23:10:43.000000'),(71,'VBH0000070J','dtshbf','dtshbf@gmail.com','+12110297532','123456789','','2019-07-04 21:04:53.214981','2019-07-04 21:04:53.214981','','','Vendor',100,'2019-07-22 23:10:43.000000'),(72,'VQJ0000071Q','XYZ','psayqd@gmail.com','13892568','ansari','','2019-07-04 21:04:53.299608','2019-07-17 04:09:01.286869','Cancled','','Vendor',100,'2019-07-22 23:10:43.000000'),(73,'VJF0000072K','zvdkib','zvdkib@gmail.com','+31013529729','123456789','','2019-07-04 21:04:53.384412','2019-07-04 21:04:53.384412','','','Vendor',100,'2019-07-22 23:10:43.000000'),(74,'VYT0000073L','ddwuxl','ddwuxl@gmail.com','+816353641010','123456789','','2019-07-04 21:04:53.547417','2019-07-04 21:04:53.547417','','','Vendor',100,'2019-07-22 23:10:43.000000'),(75,'VHZ0000074P','kcymvk','kcymvk@gmail.com','+821810131031','123456789','','2019-07-04 21:04:53.632170','2019-07-04 21:04:53.632170','','','Vendor',100,'2019-07-22 23:10:43.000000'),(76,'VBX0000075R','qebzcf','qebzcf@gmail.com','+4392522184','123456789','','2019-07-04 21:04:53.716767','2019-07-04 21:04:53.716767','','','Vendor',100,'2019-07-22 23:10:43.000000'),(77,'VNH0000076Q','kcinix','kcinix@gmail.com','+65561019157','123456789','','2019-07-04 21:04:54.001602','2019-07-04 21:04:54.001602','','','Vendor',100,'2019-07-22 23:10:43.000000'),(78,'VWX0000077L','hxwjcf','hxwjcf@gmail.com','+8635442552','123456789','','2019-07-04 21:04:54.133303','2019-07-04 21:04:54.133303','','','Vendor',100,'2019-07-22 23:10:43.000000'),(79,'VUZ0000078E','njhxjo','njhxjo@gmail.com','+68110816337','123456789','','2019-07-04 21:04:54.217972','2019-07-04 21:04:54.217972','','','Vendor',100,'2019-07-22 23:10:43.000000'),(80,'VVG0000079N','ujemnr','ujemnr@gmail.com','+7979991689','123456789','','2019-07-04 21:04:54.302635','2019-07-04 21:04:54.302635','','','Vendor',100,'2019-07-22 23:10:43.000000'),(81,'VCN0000080R','yhaaca','yhaaca@gmail.com','+10435288567','123456789','','2019-07-04 21:04:54.434150','2019-07-04 21:04:54.434150','','','Vendor',100,'2019-07-22 23:10:43.000000'),(82,'VBN0000081F','rdtgap','rdtgap@gmail.com','+459732109104','123456789','','2019-07-04 21:04:54.503236','2019-07-04 21:04:54.503236','','','Vendor',100,'2019-07-22 23:10:43.000000'),(83,'VWH0000082Z','engjkv','engjkv@gmail.com','+7912586958','123456789','','2019-07-04 21:04:54.734994','2019-07-04 21:04:54.734994','','','Vendor',100,'2019-07-22 23:10:43.000000'),(84,'VPL0000083P','tqfrws','tqfrws@gmail.com','+891011066195','123456789','','2019-07-04 21:04:54.888676','2019-07-04 21:04:54.888676','','','Vendor',100,'2019-07-22 23:10:43.000000'),(85,'VYZ0000084I','dnrcvq','dnrcvq@gmail.com','+4625654899','123456789','','2019-07-04 21:04:54.973315','2019-07-04 21:04:54.973315','','','Vendor',100,'2019-07-22 23:10:43.000000'),(86,'VGI0000085S','byfdip','byfdip@gmail.com','+109106983444','123456789','','2019-07-04 21:04:55.236543','2019-07-04 21:04:55.236543','','','Vendor',100,'2019-07-22 23:10:43.000000'),(87,'VOS0000086M','dnsjou','dnsjou@gmail.com','+65109651513','123456789','','2019-07-04 21:04:55.452753','2019-07-04 21:04:55.452753','','','Vendor',100,'2019-07-22 23:10:43.000000'),(88,'VEP0000087F','oysnxg','oysnxg@gmail.com','+615321010564','123456789','','2019-07-04 21:04:56.092324','2019-07-04 21:04:56.092324','','','Vendor',100,'2019-07-22 23:10:43.000000'),(89,'VSD0000088G','eyjugv','eyjugv@gmail.com','+23834771097','123456789','','2019-07-04 21:04:56.481340','2019-07-04 21:04:56.481340','','','Vendor',100,'2019-07-22 23:10:43.000000'),(90,'VLU0000089C','oayarg','oayarg@gmail.com','+6331435733','123456789','','2019-07-04 21:04:56.570668','2019-07-04 21:04:56.570668','','','Vendor',100,'2019-07-22 23:10:43.000000'),(91,'VQR0000090Y','ybblvt','ybblvt@gmail.com','+79114101658','123456789','','2019-07-04 21:04:56.651933','2019-07-04 21:04:56.651933','','','Vendor',100,'2019-07-22 23:10:43.000000'),(92,'VJD0000091I','wtdfdn','wtdfdn@gmail.com','+474153910106','123456789','','2019-07-04 21:04:56.755540','2019-07-04 21:04:56.755540','','','Vendor',100,'2019-07-22 23:10:43.000000'),(93,'VDH0000092N','rksoex','rksoex@gmail.com','+5323713112','123456789','','2019-07-04 21:04:56.867350','2019-07-04 21:04:56.867350','','','Vendor',100,'2019-07-22 23:10:43.000000'),(94,'VQO0000093W','vjfsvw','vjfsvw@gmail.com','+61796963410','123456789','','2019-07-04 21:04:56.936379','2019-07-04 21:04:56.936379','','','Vendor',100,'2019-07-22 23:10:43.000000'),(95,'VSP0000094X','pmfgyo','pmfgyo@gmail.com','+10263976749','123456789','','2019-07-04 21:04:57.036673','2019-07-04 21:04:57.036673','','','Vendor',100,'2019-07-22 23:10:43.000000'),(96,'VVJ0000095T','ghjper','ghjper@gmail.com','+109996105651','123456789','','2019-07-04 21:04:57.190093','2019-07-04 21:04:57.190093','','','Vendor',100,'2019-07-22 23:10:43.000000'),(97,'VTR0000096O','ohanwf','ohanwf@gmail.com','+435510611047','123456789','','2019-07-04 21:04:57.290374','2019-07-04 21:04:57.290374','','','Vendor',100,'2019-07-22 23:10:43.000000'),(98,'VCO0000097S','idxtvz','idxtvz@gmail.com','+7849692458','123456789','','2019-07-04 21:04:57.390593','2019-07-04 21:04:57.390593','','','Vendor',100,'2019-07-22 23:10:43.000000'),(99,'VGO0000098S','izvpqq','izvpqq@gmail.com','+81956210865','123456789','','2019-07-04 21:04:57.591011','2019-07-04 21:04:57.591011','','','Vendor',100,'2019-07-22 23:10:43.000000'),(100,'VUA0000099D','kxrofd','kxrofd@gmail.com','+5759319398','123456789','','2019-07-04 21:04:57.822889','2019-07-04 21:04:57.822889','','','Vendor',100,'2019-07-22 23:10:43.000000'),(101,'SWS00000100J','usixtc','usixtc@gmail.com','+7874665338','123456789','','2019-07-04 21:07:13.590619','2019-07-04 21:07:13.590619','','','Staff',100,'2019-07-22 23:10:43.000000'),(102,'SRK00000101A','fqqemk','fqqemk@gmail.com','+110710799748','123456789','','2019-07-04 21:07:13.653156','2019-07-04 21:07:13.653156','','','Staff',100,'2019-07-22 23:10:43.000000'),(103,'SCG00000102J','psjsjv','psjsjv@gmail.com','+726110103765','123456789','','2019-07-04 21:07:13.690915','2019-07-04 21:07:13.690915','','','Staff',100,'2019-07-22 23:10:43.000000'),(104,'SMU00000103X','egwttb','egwttb@gmail.com','+8848615869','123456789','','2019-07-04 21:07:13.722173','2019-07-04 21:07:13.722173','','','Staff',100,'2019-07-22 23:10:43.000000'),(105,'SVO00000104D','tuulrx','tuulrx@gmail.com','+54109568123','123456789','','2019-07-04 21:07:13.753423','2019-07-04 21:07:13.753423','','','Staff',100,'2019-07-22 23:10:43.000000'),(106,'SCC00000105L','jpyxpl','jpyxpl@gmail.com','+2892164791','123456789','','2019-07-04 21:07:13.891482','2019-07-04 21:07:13.891482','','','Staff',100,'2019-07-22 23:10:43.000000'),(107,'SRF00000106V','iyxdbr','iyxdbr@gmail.com','+6251973653','123456789','','2019-07-04 21:07:13.991749','2019-07-04 21:07:13.991749','','','Staff',100,'2019-07-22 23:10:43.000000'),(108,'SMF00000107U','pgtqar','pgtqar@gmail.com','+856310610789','123456789','','2019-07-04 21:07:14.023014','2019-07-04 21:07:14.023014','','','Staff',100,'2019-07-22 23:10:43.000000'),(109,'SFR00000108L','ebzefo','ebzefo@gmail.com','+3874857698','123456789','','2019-07-04 21:07:14.069882','2019-07-04 21:07:14.069882','','','Staff',100,'2019-07-22 23:10:43.000000'),(110,'SUH00000109I','gkiicf','gkiicf@gmail.com','+1525477995','123456789','','2019-07-04 21:07:14.154535','2019-07-04 21:07:14.154535','','','Staff',100,'2019-07-22 23:10:43.000000'),(111,'STN00000110C','jqmjnv','jqmjnv@gmail.com','+22665316108','123456789','','2019-07-04 21:07:14.207940','2019-07-04 21:07:14.207940','','','Staff',100,'2019-07-22 23:10:43.000000'),(112,'SWS00000111L','tmbost','tmbost@gmail.com','+88256731053','123456789','','2019-07-04 21:07:14.239189','2019-07-04 21:07:14.239189','','','Staff',100,'2019-07-22 23:10:43.000000'),(113,'SSL00000112V','zdygnt','zdygnt@gmail.com','+5235938322','123456789','','2019-07-04 21:07:14.292574','2019-07-04 21:07:14.292574','','','Staff',100,'2019-07-22 23:10:43.000000'),(114,'SUV00000113G','ondlxs','ondlxs@gmail.com','+84933825710','123456789','','2019-07-04 21:07:14.323853','2019-07-04 21:07:14.323853','','','Staff',100,'2019-07-22 23:10:43.000000'),(115,'SVA00000114Y','kudvcc','kudvcc@gmail.com','+2324107610101','123456789','','2019-07-04 21:07:14.408496','2019-07-04 21:07:14.408496','','','Staff',100,'2019-07-22 23:10:43.000000'),(116,'SYJ00000115X','ykxzvf','ykxzvf@gmail.com','+4738373493','123456789','','2019-07-04 21:07:14.524389','2019-07-04 21:07:14.524389','','','Staff',100,'2019-07-22 23:10:43.000000'),(117,'SKY00000116R','khyate','khyate@gmail.com','+6271134929','123456789','','2019-07-04 21:07:14.586886','2019-07-04 21:07:14.586886','','','Staff',100,'2019-07-22 23:10:43.000000'),(118,'SVX00000117S','ejmqnm','ejmqnm@gmail.com','+74895108913','123456789','','2019-07-04 21:07:14.624662','2019-07-04 21:07:14.624662','','','Staff',100,'2019-07-22 23:10:43.000000'),(119,'SQH00000118W','ntqanp','ntqanp@gmail.com','+2245632956','123456789','','2019-07-04 21:07:14.671534','2019-07-04 21:07:14.671534','','','Staff',100,'2019-07-22 23:10:43.000000'),(120,'SST00000119I','qzatbd','qzatbd@gmail.com','+2457226357','123456789','','2019-07-04 21:07:14.693669','2019-07-04 21:07:14.693669','','','Staff',100,'2019-07-22 23:10:43.000000'),(121,'SHM00000120Z','swokni','swokni@gmail.com','+61251810434','123456789','','2019-07-04 21:07:14.740557','2019-07-04 21:07:14.740557','','','Staff',100,'2019-07-22 23:10:43.000000'),(122,'SYY00000121Q','sqxyen','sqxyen@gmail.com','+210103673827','123456789','','2019-07-04 21:07:14.793947','2019-07-04 21:07:14.793947','','','Staff',100,'2019-07-22 23:10:43.000000'),(123,'SGQ00000122K','bnchii','bnchii@gmail.com','+4276193861','123456789','','2019-07-04 21:07:14.840835','2019-07-04 21:07:14.840835','','','Staff',100,'2019-07-22 23:10:43.000000'),(124,'SBB00000123W','axdxjd','axdxjd@gmail.com','+1862884658','123456789','','2019-07-04 21:07:14.887706','2019-07-04 21:07:14.887706','','','Staff',100,'2019-07-22 23:10:43.000000'),(125,'SMR00000124S','qytwoj','qytwoj@gmail.com','+8526623971','123456789','','2019-07-04 21:07:14.972350','2019-07-04 21:07:14.972350','','','Staff',100,'2019-07-22 23:10:43.000000'),(126,'STM00000125F','ewpwkj','ewpwkj@gmail.com','+2327636823','123456789','','2019-07-04 21:07:14.994491','2019-07-04 21:07:14.994491','','','Staff',100,'2019-07-22 23:10:43.000000'),(127,'SEI00000126E','zrqvkk','zrqvkk@gmail.com','+93481105363','sohail','','2019-07-04 21:07:15.041407','2019-07-04 21:07:15.041407','Active','','Staff',100,'2019-07-22 23:10:43.000000'),(128,'SEJ00000127I','dwqdcq','dwqdcq@gmail.com','+91339102153','123456789','','2019-07-04 21:07:15.072630','2019-07-04 21:07:15.072630','','','Staff',100,'2019-07-22 23:10:43.000000'),(129,'SAF00000128Y','hpchxw','hpchxw@gmail.com','+34444108519','123456789','','2019-07-04 21:07:15.226456','2019-07-04 21:07:15.226456','','','Staff',100,'2019-07-22 23:10:43.000000'),(130,'SSW00000129Z','vhqxhj','vhqxhj@gmail.com','+4754289779','123456789','','2019-07-04 21:07:15.257619','2019-07-04 21:07:15.257619','','','Staff',100,'2019-07-22 23:10:43.000000'),(131,'SAX00000130Y','nerykh','nerykh@gmail.com','+37216373410','123456789','','2019-07-04 21:07:15.295409','2019-07-04 21:07:15.295409','','','Staff',100,'2019-07-22 23:10:43.000000'),(132,'SWS00000131J','otutqy','otutqy@gmail.com','+69582598610','123456789','','2019-07-04 21:07:15.326667','2019-07-04 21:07:15.326667','','','Staff',100,'2019-07-22 23:10:43.000000'),(133,'SXP00000132Q','eohrvw','eohrvw@gmail.com','+77526656102','123456789','','2019-07-04 21:07:15.373540','2019-07-04 21:07:15.373540','','','Staff',100,'2019-07-22 23:10:43.000000'),(134,'SSO00000133T','lkdpui','lkdpui@gmail.com','+7542510101110','123456789','','2019-07-04 21:07:15.442621','2019-07-04 21:07:15.442621','','','Staff',100,'2019-07-22 23:10:43.000000'),(135,'SGL00000134F','ococcp','ococcp@gmail.com','+66942843103','123456789','','2019-07-04 21:07:15.496059','2019-07-04 21:07:15.496059','','','Staff',100,'2019-07-22 23:10:43.000000'),(136,'SVK00000135I','hpskgc','hpskgc@gmail.com','+87451738108','123456789','','2019-07-04 21:07:15.527404','2019-07-04 21:07:15.527404','','','Staff',100,'2019-07-22 23:10:43.000000'),(137,'SAT00000136I','tozmna','tozmna@gmail.com','+38724167103','123456789','','2019-07-04 21:07:15.558650','2019-07-04 21:07:15.558650','','','Staff',100,'2019-07-22 23:10:43.000000'),(138,'SJF00000137E','tnlnvt','tnlnvt@gmail.com','+439761091066','123456789','','2019-07-04 21:07:15.596335','2019-07-04 21:07:15.596335','','','Staff',100,'2019-07-22 23:10:43.000000'),(139,'SBW00000138Q','nuisgk','nuisgk@gmail.com','+3415962443','123456789','','2019-07-04 21:07:15.627677','2019-07-04 21:07:15.627677','','','Staff',100,'2019-07-22 23:10:43.000000'),(140,'SQH00000139V','vhztyn','vhztyn@gmail.com','+23710453561','123456789','','2019-07-04 21:07:15.658925','2019-07-04 21:07:15.658925','','','Staff',100,'2019-07-22 23:10:43.000000'),(141,'SFD00000140I','iixqnt','iixqnt@gmail.com','+3985269135','123456789','','2019-07-04 21:07:15.696683','2019-07-04 21:07:15.696683','','','Staff',100,'2019-07-22 23:10:43.000000'),(142,'STM00000141V','myyefs','myyefs@gmail.com','+1987491974','123456789','','2019-07-04 21:07:15.728025','2019-07-04 21:07:15.728025','','','Staff',100,'2019-07-22 23:10:43.000000'),(143,'SKA00000142A','yleeok','yleeok@gmail.com','+48973959102','123456789','','2019-07-04 21:07:15.759272','2019-07-04 21:07:15.759272','','','Staff',100,'2019-07-22 23:10:43.000000'),(144,'SVL00000143K','tppksp','tppksp@gmail.com','+6516338593','123456789','','2019-07-04 21:07:15.796960','2019-07-04 21:07:15.796960','','','Staff',100,'2019-07-22 23:10:43.000000'),(145,'SUZ00000144K','msnfcq','msnfcq@gmail.com','+21035767633','123456789','','2019-07-04 21:07:15.859551','2019-07-04 21:07:15.859551','','','Staff',100,'2019-07-22 23:10:43.000000'),(146,'SJM00000145O','rivpjn','rivpjn@gmail.com','+910672563810','123456789','','2019-07-04 21:07:15.897340','2019-07-04 21:07:15.897340','','','Staff',100,'2019-07-22 23:10:43.000000'),(147,'SFK00000146R','urelqn','urelqn@gmail.com','+27108392897','123456789','','2019-07-04 21:07:15.928603','2019-07-04 21:07:15.928603','','','Staff',100,'2019-07-22 23:10:43.000000'),(148,'SVL00000147E','rxdwfe','rxdwfe@gmail.com','+4310781071057','123456789','','2019-07-04 21:07:15.959853','2019-07-04 21:07:15.959853','','','Staff',100,'2019-07-22 23:10:43.000000'),(149,'SSZ00000148D','dnepqq','dnepqq@gmail.com','+89444108726','123456789','','2019-07-04 21:07:15.997716','2019-07-04 21:07:15.997716','','','Staff',100,'2019-07-22 23:10:43.000000'),(150,'SOQ00000149T','eaxkvd','eaxkvd@gmail.com','+366910641015','123456789','','2019-07-04 21:07:16.029059','2019-07-04 21:07:16.029059','','','Staff',100,'2019-07-22 23:10:43.000000'),(151,'SRZ00000150L','qgngqd','qgngqd@gmail.com','+659175102103','123456789','','2019-07-04 21:07:16.060305','2019-07-04 21:07:16.060305','','','Staff',100,'2019-07-22 23:10:43.000000'),(152,'SZN00000151N','mfipef','mfipef@gmail.com','+49748638108','123456789','','2019-07-04 21:07:16.098063','2019-07-04 21:07:16.098063','','','Staff',100,'2019-07-22 23:10:43.000000'),(153,'SFE00000152E','ieunsi','ieunsi@gmail.com','+4247441574','123456789','','2019-07-04 21:07:16.198328','2019-07-04 21:07:16.198328','','','Staff',100,'2019-07-22 23:10:43.000000'),(154,'SKC00000153H','rvzvyz','rvzvyz@gmail.com','+44285868110','123456789','','2019-07-04 21:07:16.229587','2019-07-04 21:07:16.229587','','','Staff',100,'2019-07-22 23:10:43.000000'),(155,'SJF00000154S','ybxeqr','ybxeqr@gmail.com','+23325891097','123456789','','2019-07-04 21:07:16.260866','2019-07-04 21:07:16.260866','','','Staff',100,'2019-07-22 23:10:43.000000'),(156,'SEW00000155F','gzhgqc','gzhgqc@gmail.com','+9257484885','123456789','','2019-07-04 21:07:16.298595','2019-07-04 21:07:16.298595','','','Staff',100,'2019-07-22 23:10:43.000000'),(157,'SNG00000156D','xhswxq','xhswxq@gmail.com','+44574310243','123456789','','2019-07-04 21:07:16.329864','2019-07-04 21:07:16.329864','','','Staff',100,'2019-07-22 23:10:43.000000'),(158,'SEI00000157P','qgottu','qgottu@gmail.com','+34824419104','123456789','','2019-07-04 21:07:16.361102','2019-07-04 21:07:16.361102','','','Staff',100,'2019-07-22 23:10:43.000000'),(159,'SOD00000158U','zaownu','zaownu@gmail.com','+6466288291','123456789','','2019-07-04 21:07:16.398871','2019-07-04 21:07:16.398871','','','Staff',100,'2019-07-22 23:10:43.000000'),(160,'SDX00000159S','pzhxgq','pzhxgq@gmail.com','+73358168210','123456789','','2019-07-04 21:07:16.430142','2019-07-04 21:07:16.430142','','','Staff',100,'2019-07-22 23:10:43.000000'),(161,'SGL00000160R','ssfyho','ssfyho@gmail.com','+4732139698','123456789','','2019-07-04 21:07:16.461380','2019-07-04 21:07:16.461380','','','Staff',100,'2019-07-22 23:10:43.000000'),(162,'SHF00000161V','qyfucb','qyfucb@gmail.com','+63656451078','123456789','','2019-07-04 21:07:16.499142','2019-07-04 21:07:16.499142','','','Staff',100,'2019-07-22 23:10:43.000000'),(163,'SUG00000162K','soeuhi','soeuhi@gmail.com','+2636799586','123456789','','2019-07-04 21:07:16.592929','2019-07-04 21:07:16.592929','','','Staff',100,'2019-07-22 23:10:43.000000'),(164,'SCF00000163E','oidmzo','oidmzo@gmail.com','+4111421934','123456789','','2019-07-04 21:07:16.630739','2019-07-04 21:07:16.630739','','','Staff',100,'2019-07-22 23:10:43.000000'),(165,'SSJ00000164P','fciysy','fciysy@gmail.com','+73810654793','123456789','','2019-07-04 21:07:16.661980','2019-07-04 21:07:16.661980','','','Staff',100,'2019-07-22 23:10:43.000000'),(166,'SYD00000165W','sqcpvm','sqcpvm@gmail.com','+592281094810','123456789','','2019-07-04 21:07:16.746682','2019-07-04 21:07:16.746682','','','Staff',100,'2019-07-22 23:10:43.000000'),(167,'SNU00000166F','duftlb','duftlb@gmail.com','+81058221246','123456789','','2019-07-04 21:07:16.777961','2019-07-04 21:07:16.777961','','','Staff',100,'2019-07-22 23:10:43.000000'),(168,'SGB00000167S','sixltp','sixltp@gmail.com','+436106810899','123456789','','2019-07-04 21:07:16.815752','2019-07-04 21:07:16.815752','','','Staff',100,'2019-07-22 23:10:43.000000'),(169,'SGH00000168S','AliShan','sohailshan@gmail.com','','123456789','','2019-07-04 21:07:16.846993','2019-07-23 22:10:25.397580','','','Staff',100,'2019-07-22 23:10:43.000000'),(170,'SKO00000169S','hzpoez','hzpoez@gmail.com','+152725810105','123456789','','2019-07-04 21:07:16.878219','2019-07-04 21:07:16.878219','','','Staff',100,'2019-07-22 23:10:43.000000'),(171,'SIW00000170F','rvwyac','rvwyac@gmail.com','+14951104225','123456789','','2019-07-04 21:07:16.915994','2019-07-04 21:07:16.915994','','','Staff',100,'2019-07-22 23:10:43.000000'),(172,'SFE00000171C','bxrest','bxrest@gmail.com','+81035574262','123456789','','2019-07-04 21:07:16.947272','2019-07-04 21:07:16.947272','','','Staff',100,'2019-07-22 23:10:43.000000'),(173,'SMU00000172Y','ewxarx','ewxarx@gmail.com','+2971725612','123456789','','2019-07-04 21:07:16.978520','2019-07-04 21:07:16.978520','','','Staff',100,'2019-07-22 23:10:43.000000'),(174,'SSR00000173G','bojtsb','bojtsb@gmail.com','+22105498813','123456789','','2019-07-04 21:07:17.016303','2019-07-04 21:07:17.016303','','','Staff',100,'2019-07-22 23:10:43.000000'),(175,'STE00000174V','nefjrh','nefjrh@gmail.com','+3836144282','123456789','','2019-07-04 21:07:17.047530','2019-07-04 21:07:17.047530','','','Staff',100,'2019-07-22 23:10:43.000000'),(176,'SHD00000175T','wpzdxb','wpzdxb@gmail.com','+61093138136','123456789','','2019-07-04 21:07:17.078798','2019-07-04 21:07:17.078798','','','Staff',100,'2019-07-22 23:10:43.000000');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venderorders`
--

DROP TABLE IF EXISTS `venderorders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `venderorders` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `venderorders_UserId_7a0d84b2_fk_user_Id` (`UserId`),
  CONSTRAINT `venderorders_UserId_7a0d84b2_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venderorders`
--

LOCK TABLES `venderorders` WRITE;
/*!40000 ALTER TABLE `venderorders` DISABLE KEYS */;
/*!40000 ALTER TABLE `venderorders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendor`
--

DROP TABLE IF EXISTS `vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendor` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `BusinessName` varchar(50) NOT NULL,
  `BusinessEmail` varchar(225) NOT NULL,
  `BusinessContact` varchar(225) NOT NULL,
  `Industry` varchar(225) NOT NULL,
  `SystemName` varchar(225) NOT NULL,
  `BusinessAddress` longtext NOT NULL,
  `BusinessLogo` longtext NOT NULL,
  `BusinessIcon` longtext NOT NULL,
  `HeroIcon` longtext NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `vendor_UserId_03f6ffae_fk_user_Id` (`UserId`),
  CONSTRAINT `vendor_UserId_03f6ffae_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor`
--

LOCK TABLES `vendor` WRITE;
/*!40000 ALTER TABLE `vendor` DISABLE KEYS */;
/*!40000 ALTER TABLE `vendor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendordiscount`
--

DROP TABLE IF EXISTS `vendordiscount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendordiscount` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(225) NOT NULL,
  `Discount` int(11) NOT NULL,
  `CreatedDate` datetime(6) NOT NULL,
  `ExpiryDate` datetime(6) NOT NULL,
  `UserId` int(11) NOT NULL,
  `Type` varchar(225) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `unltd_vendordiscount_UserId_03d5e47f_fk_user_Id` (`UserId`),
  CONSTRAINT `unltd_vendordiscount_UserId_03d5e47f_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendordiscount`
--

LOCK TABLES `vendordiscount` WRITE;
/*!40000 ALTER TABLE `vendordiscount` DISABLE KEYS */;
INSERT INTO `vendordiscount` VALUES (1,'discoutn',12,'2019-08-06 04:28:16.621102','2019-08-06 09:25:00.000000',4,'FixedAmount'),(2,'discount 1',10,'2019-08-06 04:28:55.600933','2019-08-07 06:30:00.000000',4,'PercentageAmount');
/*!40000 ALTER TABLE `vendordiscount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendormember`
--

DROP TABLE IF EXISTS `vendormember`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendormember` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `VendorMember_UserId_42cab4d8_fk_user_Id` (`UserId`),
  CONSTRAINT `VendorMember_UserId_42cab4d8_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendormember`
--

LOCK TABLES `vendormember` WRITE;
/*!40000 ALTER TABLE `vendormember` DISABLE KEYS */;
/*!40000 ALTER TABLE `vendormember` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendorstaff`
--

DROP TABLE IF EXISTS `vendorstaff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendorstaff` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `VendorStaff_UserId_5624208c_fk_user_Id` (`UserId`),
  CONSTRAINT `VendorStaff_UserId_5624208c_fk_user_Id` FOREIGN KEY (`UserId`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendorstaff`
--

LOCK TABLES `vendorstaff` WRITE;
/*!40000 ALTER TABLE `vendorstaff` DISABLE KEYS */;
/*!40000 ALTER TABLE `vendorstaff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-06 16:44:24
