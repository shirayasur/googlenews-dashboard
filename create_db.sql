

--
-- Table structure for table `news_table`
--

DROP TABLE IF EXISTS `news_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `news_table` (
  `Competitor` varchar(50) DEFAULT NULL,
  `Title` varchar(300) NOT NULL,
  `Desc` text,
  `Date` datetime DEFAULT NULL,
  `Link` text,
  `Site` text,
  PRIMARY KEY (`Title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

