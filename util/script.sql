CREATE DATABASE IF NOT EXISTS flask_test;

USE flask_test;

CREATE TABLE IF NOT EXISTS indicators (
    id bigint(32) NOT NULL AUTO_INCREMENT,
    location varchar(8) COLLATE utf8_unicode_ci NOT NULL,
    country varchar(24) COLLATE utf8_unicode_ci NOT NULL,
    indicator_code varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
    indicator_full varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
    measure_code varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
    measure_full varchar(24) COLLATE utf8_unicode_ci DEFAULT NULL,
    inequality_code varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
    inequality_full varchar(24) COLLATE utf8_unicode_ci DEFAULT NULL,
    unit_code varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
    unit_full varchar(24) COLLATE utf8_unicode_ci DEFAULT NULL,
    powercode_code varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
    powercode_full varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
    reference_period_code varchar(24) COLLATE utf8_unicode_ci DEFAULT NULL,
    reference_period_full varchar(24) COLLATE utf8_unicode_ci DEFAULT NULL,
    value float(20,2) COLLATE utf8_unicode_ci DEFAULT NULL,
    flag_codes varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
    flags varchar(24) COLLATE utf8_unicode_ci DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

LOAD DATA LOCAL INFILE '/home/mauri/Documents/Flask/aivo_test/BLI_28032019144925238.csv'
INTO TABLE indicators
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS (
    location,
    country,
    indicator_code,
    indicator_full,
    measure_code,
    measure_full,
    inequality_code,
    inequality_full,
    unit_code,
    unit_full,
    powercode_code,
    powercode_full,
    reference_period_code,
    reference_period_full,
    value,
    flag_codes,
    flags
);