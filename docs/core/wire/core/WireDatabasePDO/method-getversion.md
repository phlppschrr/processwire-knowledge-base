# $wireDatabasePDO->getVersion($getNumberOnly = false): string

Source: `wire/core/WireDatabasePDO.php`

Get MySQL/MariaDB version

Example return values:
Example return values:

 - 5.7.23
 - 10.1.34-MariaDB

## Usage

~~~~~
// basic usage
$string = $wireDatabasePDO->getVersion();

// usage with all arguments
$string = $wireDatabasePDO->getVersion($getNumberOnly = false);
~~~~~

## Arguments

- `$getNumberOnly` (optional) `bool` Get only version number, exclude any vendor specific suffixes? (default=false) 3.0.185+

## Return value

- `string`

## Since

3.0.166
