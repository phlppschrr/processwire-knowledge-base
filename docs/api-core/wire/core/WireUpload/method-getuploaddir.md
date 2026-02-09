# $wireUpload->getUploadDir(): string

Source: `wire/core/WireUpload.php`

Get the directory where files should upload to

## Usage

~~~~~
// basic usage
$string = $wireUpload->getUploadDir();
~~~~~

## Return value

- `string`

## Exceptions

- `WireException` If no suitable upload directory can be found
