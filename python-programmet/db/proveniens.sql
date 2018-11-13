-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 03, 2018 at 04:50 PM
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
-- Table structure for table `proveniens`
--

CREATE TABLE `proveniens` (
  `regnr` varchar(10) NOT NULL,
  `produsent` varchar(30) DEFAULT NULL,
  `prod_aar` int(11) DEFAULT NULL,
  `tidl_eiere` varchar(300) DEFAULT NULL,
  `siste_eier` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `proveniens`
--

INSERT INTO `proveniens` (`regnr`, `produsent`, `prod_aar`, `tidl_eiere`, `siste_eier`) VALUES
('abc', 'test', 0, 'testt', 'test'),
('ABC.1234', 'Ida Treskjærer', 1923, 'Morten Mortensen', 'Morten Mortensen'),
('ABC.1235', 'Ukjent', 1800, 'Morten Mortensen', 'Morten Mortensen'),
('ABC.1236', 'Ida Treskjærer', 1928, 'Ida Mortensen', 'Ida Mortensen'),
('ABC.1237', 'Ida Treskjærer', 1920, 'Ida Mortensen', 'Ida Mortensen'),
('ABC.1238', 'Ukjent', 1800, 'Ida Mortensen', 'Ida Mortensen');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `proveniens`
--
ALTER TABLE `proveniens`
  ADD PRIMARY KEY (`regnr`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `proveniens`
--
ALTER TABLE `proveniens`
  ADD CONSTRAINT `proveniens_ibfk_1` FOREIGN KEY (`regnr`) REFERENCES `gjenstand` (`regnr`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
