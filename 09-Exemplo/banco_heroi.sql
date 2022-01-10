-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 27-Nov-2021 às 18:40
-- Versão do servidor: 10.4.21-MariaDB
-- versão do PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `banco_heroi`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `herois`
--

CREATE TABLE `herois` (
  `nome_heroi` varchar(15) DEFAULT NULL,
  `nome_persona` varchar(20) DEFAULT NULL,
  `afiliacao` varchar(10) DEFAULT NULL,
  `parceiro` varchar(20) DEFAULT NULL,
  `poderes` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `herois`
--

INSERT INTO `herois` (`nome_heroi`, `nome_persona`, `afiliacao`, `parceiro`, `poderes`) VALUES
('Batman', 'Bruce Wayne', 'DC', 'Robin', 'Detetive, 30 lutas, rico'),
('Flash', 'Barry Allen', 'DC', 'Kid flash', 'super velocidade'),
('Mulher Maravilh', 'Diana Prince', 'DC', 'Garota Maravilha', 'Super força, laco verdade'),
('Wolverine', 'Logan', 'Marvel', 'não tem', 'Garras de adamatio, fator cura');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
