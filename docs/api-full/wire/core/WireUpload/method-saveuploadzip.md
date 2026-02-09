# $wireUpload->saveUploadZip($zipFile): array|bool

Source: `wire/core/WireUpload.php`

Save and process an uploaded ZIP file

## Usage

~~~~~
// basic usage
$array = $wireUpload->saveUploadZip($zipFile);
~~~~~

## Arguments

- `$zipFile` `string`

## Return value

- `array|bool` Array of files in the ZIP or boolean false on fail

## Exceptions

- `WireException` If ZIP is empty
