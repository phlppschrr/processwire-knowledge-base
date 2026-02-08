# $wireUpload->getTargetFilename($filename): string

Source: `wire/core/WireUpload.php`

Get target filename updated for extension

Given a filename, takes its extension and combines it with that if the targetFilename (if set).
Otehrwise returns the filename you gave it.

## Usage

~~~~~
// basic usage
$string = $wireUpload->getTargetFilename($filename);
~~~~~

## Arguments

- `$filename` `string`

## Return value

- `string`
