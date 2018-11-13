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
-- Table structure for table `gjenstand`
--

CREATE TABLE `gjenstand` (
  `regnr` varchar(10) NOT NULL,
  `navn` varchar(30) DEFAULT NULL,
  `kategori_id` int(11) DEFAULT NULL,
  `regdato` varchar(15) DEFAULT NULL,
  `regav` varchar(50) DEFAULT NULL,
  `inndato` varchar(15) DEFAULT NULL,
  `mottattav` varchar(50) DEFAULT NULL,
  `giver` varchar(300) DEFAULT NULL,
  `plassering` varchar(30) DEFAULT NULL,
  `kommentar` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `gjenstand`
--

INSERT INTO `gjenstand` (`regnr`, `navn`, `kategori_id`, `regdato`, `regav`, `inndato`, `mottattav`, `giver`, `plassering`, `kommentar`) VALUES
('abc', 'test', 2, '12.24.2001', 'test', '12.34.1234', 'test', 'test', 'test', ''),
('ABC.1234', 'Gyngehest', 2, '20.06.2006', 'Assistent Berit', '24.06.2006', 'Anne Elinsen', 'Morten Mortensen', 'H2.24', ''),
('ABC.1235', 'Bamse', 2, '20.06.2006', 'Assistent Berit', '24.06.2006', 'Anne Elinsen', 'Morten Mortensen', 'H2.25', ''),
('ABC.1236', 'Lekehund', 2, '20.06.2006', 'Assistent Berit', '27.06.2006', 'Anne Elinsen', 'Morten Mortensen', 'H2.26', ''),
('ABC.1237', 'Lekebil', 2, '20.06.2006', 'Assistent Berit', '27.06.2006', 'Anne Elinsen', 'Ida Mortensen', 'H2.27', ''),
('ABC.1238', 'Dukkevogn', 2, '20.06.2006', 'Assistent Berit', '27.06.2006', 'Anne Elinsen', 'Ida Mortensen', 'H2.28', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gjenstand`
--
ALTER TABLE `gjenstand`
  ADD PRIMARY KEY (`regnr`),
  ADD KEY `kategori_id` (`kategori_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `gjenstand`
--
ALTER TABLE `gjenstand`
  ADD CONSTRAINT `gjenstand_ibfk_1` FOREIGN KEY (`kategori_id`) REFERENCES `kategori` (`kategori_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
