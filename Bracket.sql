-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema BracketDb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema BracketDb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `BracketDb` DEFAULT CHARACTER SET utf8 ;
USE `BracketDb` ;

-- -----------------------------------------------------
-- Table `BracketDb`.`Team`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BracketDb`.`Team` (
  `teamName` CHAR(50) NOT NULL,
  `teamID` INT NOT NULL,
  `Record` INT NULL,
  `teamLeader` INT NOT NULL,
  PRIMARY KEY (`teamID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BracketDb`.`Player`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BracketDb`.`Player` (
  `playerID` INT NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `age` DATE NOT NULL,
  `gender` VARCHAR(50) NULL,
  `userID_fk` INT NOT NULL,
  PRIMARY KEY (`playerID`, `userID_fk`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BracketDb`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BracketDb`.`User` (
  `userID` INT NOT NULL,
  `userName` VARCHAR(50) NULL,
  `password` VARCHAR(200) NULL,
  `privileges` TINYINT NOT NULL,
  `playerID` INT NULL,
  `playerID_fk` INT NOT NULL,
  PRIMARY KEY (`userID`, `playerID_fk`),
  INDEX `fk_User_Player1_idx` (`playerID_fk` ASC) VISIBLE,
  CONSTRAINT `fk_User_Player1`
    FOREIGN KEY (`playerID_fk`)
    REFERENCES `BracketDb`.`Player` (`playerID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BracketDb`.`Round`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BracketDb`.`Round` (
  `roundID` INT NOT NULL,
  `tournamentID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`roundID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BracketDb`.`Match`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BracketDb`.`Match` (
  `matchID` INT NOT NULL,
  `roundID` INT NOT NULL,
  `roundID_fk` INT NOT NULL,
  PRIMARY KEY (`matchID`, `roundID_fk`),
  INDEX `fk_Match_Round1_idx` (`roundID_fk` ASC) VISIBLE,
  CONSTRAINT `roundID_fk`
    FOREIGN KEY (`roundID_fk`)
    REFERENCES `BracketDb`.`Round` (`roundID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BracketDb`.`TournamentType`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BracketDb`.`TournamentType` (
  `tournamentID` INT NOT NULL,
  `numberOfRounds` INT NOT NULL,
  `gamesPlayed` INT NOT NULL,
  `typeOfBbracket` VARCHAR(50) NOT NULL,
  `roundID_fk` INT NOT NULL,
  PRIMARY KEY (`tournamentID`, `roundID_fk`),
  INDEX `roundID_fk` (`roundID_fk` ASC) VISIBLE,
  CONSTRAINT `roundID_fk`
    FOREIGN KEY (`roundID_fk`)
    REFERENCES `BracketDb`.`Round` (`roundID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BracketDb`.`Can Be On`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BracketDb`.`Can Be On` (
  `playerID` INT NOT NULL,
  `teamID` INT NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BracketDb`.`Can be on`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BracketDb`.`Can be on` (
  `Player_playerID` INT NOT NULL,
  `Team_teamID` INT NOT NULL,
  INDEX `fk_Player_has_Team_Player1_idx` (`Player_playerID` ASC) VISIBLE,
  INDEX `teamID_fk_idx` (`Team_teamID` ASC, `Player_playerID` ASC) VISIBLE,
  CONSTRAINT `playerID_fk`
    FOREIGN KEY (`Player_playerID`)
    REFERENCES `BracketDb`.`Player` (`playerID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `teamID_fk`
    FOREIGN KEY (`Team_teamID` , `Player_playerID`)
    REFERENCES `BracketDb`.`Team` (`teamID` , `teamID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BracketDb`.`participates`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BracketDb`.`participates` (
  `Team_teamID` INT NOT NULL,
  `Match_matchID` INT NOT NULL,
  INDEX `fk_Team_has_Match1_Match1_idx` (`Match_matchID` ASC) VISIBLE,
  INDEX `fk_Team_has_Match1_Team1_idx` (`Team_teamID` ASC) VISIBLE,
  CONSTRAINT `teamID_fk`
    FOREIGN KEY (`Team_teamID`)
    REFERENCES `BracketDb`.`Team` (`teamID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `matchID_fk`
    FOREIGN KEY (`Match_matchID`)
    REFERENCES `BracketDb`.`Match` (`matchID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BracketDb`.`participates`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BracketDb`.`participates` (
  `Team_teamID` INT NOT NULL,
  `Match_matchID` INT NOT NULL,
  INDEX `fk_Team_has_Match1_Match1_idx` (`Match_matchID` ASC) VISIBLE,
  INDEX `fk_Team_has_Match1_Team1_idx` (`Team_teamID` ASC) VISIBLE,
  CONSTRAINT `teamID_fk`
    FOREIGN KEY (`Team_teamID`)
    REFERENCES `BracketDb`.`Team` (`teamID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `matchID_fk`
    FOREIGN KEY (`Match_matchID`)
    REFERENCES `BracketDb`.`Match` (`matchID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
