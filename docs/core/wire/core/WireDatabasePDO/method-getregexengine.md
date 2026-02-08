# $wireDatabasePDO->getRegexEngine(): string

Source: `wire/core/WireDatabasePDO.php`

Get the regular expression engine used by database

Returns one of 'ICU' (MySQL 8.0.4+) or 'HenrySpencer' (earlier versions and MariaDB)

## Return value

string

## Since

3.0.166

## Details

- @todo this will need to be updated when/if MariaDB adds version that uses ICU engine
