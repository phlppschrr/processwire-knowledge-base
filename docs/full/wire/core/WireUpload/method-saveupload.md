# $wireUpload->saveUpload($tmp_name, $filename, $ajax = false): array|bool|string

Source: `wire/core/WireUpload.php`

Save the uploaded file

## Usage

~~~~~
// basic usage
$array = $wireUpload->saveUpload($tmp_name, $filename);

// usage with all arguments
$array = $wireUpload->saveUpload($tmp_name, $filename, $ajax = false);
~~~~~

## Arguments

- `$tmp_name` `string` Temporary filename (full path and filename)
- `$filename` `string` Actual filename (basename)
- `$ajax` (optional) `bool` Is this an AJAX upload?

## Return value

- `array|bool|string` Boolean false on fail, array of multiple filenames, or string of filename if maxFiles=1
