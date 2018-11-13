-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 03, 2018 at 04:49 PM
-- Server version: 5.7.23-0ubuntu0.18.04.1
-- PHP Version: 7.2.10-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `beritgud`
--

-- --------------------------------------------------------

--
-- Table structure for table `egenskaper`
--

CREATE TABLE `egenskaper` (
  `regnr` varchar(10) NOT NULL,
  `materiale` varchar(30) DEFAULT NULL,
  `maal` varchar(30) DEFAULT NULL,
  `tilstand` varchar(15) DEFAULT NULL,
  `fys_egenskap` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `egenskaper`
--

INSERT INTO `egenskaper` (`regnr`, `materiale`, `maal`, `tilstand`, `fys_egenskap`) VALUES
('abc', 'test', 'test', 'test', 'test'),
('ABC.1234', 'Tre', '120 cm', 'Slitt', '7'),
('ABC.1235', 'Bomull', '30 cm', 'Slitt', 'Fargen er lysebrun, mangler et øre'),
('ABC.1236', 'Tre', '12 cm', 'Slitt', 'Liten rødmalt trehund, slitt maling. '),
('ABC.1237', 'Tre', '8 cm', 'God', ''),
('ABC.1238', 'Metall', '80 cm', 'Slitt', 'Falmet og slitt med merker på stoffet bak.');
('ABC.1244','Tre Gran','L:90 cm, H:60 cm, D:42 cm','God','Malt kiste');
('ABC.1245','Keramikk','L:30 cm, B:30 cm, D:15 cm','God','Keramikk Bolle');
('ABC.1246','Keramikk','L:32 cm, B:32 cm, D:15 cm','God','Keramikk Bolle');
('ABC.1246','Pipeleire','L:32 cm, B:5 cm','God','Krittpipe');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `egenskaper`
--
ALTER TABLE `egenskaper`
  ADD PRIMARY KEY (`regnr`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `egenskaper`
--
ALTER TABLE `egenskaper`
  ADD CONSTRAINT `egenskaper_ibfk_1` FOREIGN KEY (`regnr`) REFERENCES `gjenstand` (`regnr`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
