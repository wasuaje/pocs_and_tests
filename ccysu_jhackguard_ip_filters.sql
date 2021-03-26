-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-07-2015 a las 05:32:59
-- Versión del servidor: 5.6.21
-- Versión de PHP: 5.5.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `anunciantes`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ccysu_jhackguard_ip_filters`
--

CREATE TABLE IF NOT EXISTS `ccysu_jhackguard_ip_filters` (
`id` int(11) unsigned NOT NULL,
  `ordering` int(11) NOT NULL,
  `state` tinyint(1) NOT NULL,
  `checked_out` int(11) NOT NULL,
  `checked_out_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(11) NOT NULL,
  `ip` varchar(255) NOT NULL,
  `expires` date NOT NULL,
  `rule_type` varchar(255) NOT NULL
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `ccysu_jhackguard_ip_filters`
--

INSERT INTO `ccysu_jhackguard_ip_filters` (`id`, `ordering`, `state`, `checked_out`, `checked_out_time`, `created_by`, `ip`, `expires`, `rule_type`) VALUES
(2, 1, 1, 0, '0000-00-00 00:00:00', 0, '::1', '0000-00-00', 'wl');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `ccysu_jhackguard_ip_filters`
--
ALTER TABLE `ccysu_jhackguard_ip_filters`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ccysu_jhackguard_ip_filters`
--
ALTER TABLE `ccysu_jhackguard_ip_filters`
MODIFY `id` int(11) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
