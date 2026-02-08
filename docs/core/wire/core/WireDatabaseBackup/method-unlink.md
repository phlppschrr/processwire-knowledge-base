# $wireDatabaseBackup->unlink($file): bool

Source: `wire/core/WireDatabaseBackup.php`

Unlink file using PW if available or PHP if not

## Usage

~~~~~
// basic usage
$bool = $wireDatabaseBackup->unlink($file);
~~~~~

## Arguments

- `$file` `string`

## Return value

- `bool`

## Exceptions

- `WireException`
