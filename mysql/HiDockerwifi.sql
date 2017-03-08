-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: 112.74.171.161    Database: HiDockerwifi
-- ------------------------------------------------------
-- Server version	5.7.17-0ubuntu0.16.04.2

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
-- Table structure for table `equipdb`
--

DROP TABLE IF EXISTS `equipdb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equipdb` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `equip` char(10) NOT NULL,
  `status` tinyint(3) unsigned NOT NULL,
  `signintime` varchar(30) NOT NULL,
  `dockername` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipdb`
--

LOCK TABLES `equipdb` WRITE;
/*!40000 ALTER TABLE `equipdb` DISABLE KEYS */;
INSERT INTO `equipdb` VALUES (1,'bx',1,'123213321','jo/liu'),(2,'bx',1,'1234','jo/mysql'),(3,'bx',0,'1234','jo/mysql'),(4,'bx',0,'1234','jo/mysql'),(5,'bx',0,'1234','jo/mysql'),(6,'bx',0,'1234','resin/armv7hf-debian'),(7,'bx',0,'1234','resin/armv7hf-debian'),(8,'bx',0,'1234','resin/armv7hf-debian'),(9,'bx',0,'1234','resin/armv7hf-debian'),(10,'bx',0,'1234','resin/armv7hf-debian'),(11,'bx',0,'1234','resin/armv7hf-debian'),(12,'bx',0,'1234','resin/armv7hf-debian'),(13,'bx',0,'1234','resin/armv7hf-debian'),(14,'bx',0,'1234','resin/armv7hf-debian'),(15,'bx',0,'1234','resin/armv7hf-debian'),(16,'bx',0,'1234','resin/armv7hf-debian'),(17,'bx',0,'1234','resin/armv7hf-debian'),(18,'bx',0,'1234','resin/armv7hf-debian'),(19,'bx',0,'1234','resin/armv7hf-debian'),(20,'bx',0,'1234','resin/armv7hf-debian'),(21,'bx',0,'1234','resin/armv7hf-debian'),(22,'bx',0,'1234','resin/armv7hf-debian'),(23,'bx',0,'1234','resin/armv7hf-debian'),(24,'bx',0,'1234','resin/armv7hf-debian'),(25,'bx',0,'1234','resin/armv7hf-debian'),(26,'bx',0,'1234','resin/armv7hf-debian'),(27,'bx',0,'1234','resin/armv7hf-debian');
/*!40000 ALTER TABLE `equipdb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portdb`
--

DROP TABLE IF EXISTS `portdb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portdb` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `port` int(8) NOT NULL,
  `status` int(11) DEFAULT '0',
  `equip` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portdb`
--

LOCK TABLES `portdb` WRITE;
/*!40000 ALTER TABLE `portdb` DISABLE KEYS */;
INSERT INTO `portdb` VALUES (1,33333,1,'bx'),(2,33334,1,'bx'),(3,33335,0,NULL),(4,33336,0,NULL),(5,33337,0,NULL),(6,33338,0,NULL),(7,33339,0,NULL),(8,33340,0,NULL),(9,33341,0,NULL),(10,33342,0,NULL),(11,33343,0,NULL),(12,33344,0,NULL),(13,33345,0,NULL),(14,33346,0,NULL),(15,33347,0,NULL),(16,33348,0,NULL),(17,33349,0,NULL),(18,33350,0,NULL),(19,33351,0,NULL),(20,33352,0,NULL);
/*!40000 ALTER TABLE `portdb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-08 16:40:05
