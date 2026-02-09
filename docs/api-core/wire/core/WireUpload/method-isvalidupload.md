# $wireUpload->isValidUpload($name, $size, $error): bool

Source: `wire/core/WireUpload.php`

Is the given upload information valid?

Also populates $this->errors

## Usage

~~~~~
// basic usage
$bool = $wireUpload->isValidUpload($name, $size, $error);
~~~~~

## Arguments

- `$name` `string` Filename
- `$size` `int` Size in bytes
- `$error` `int` Error code from PHP

## Return value

- `bool`
