# $wireUpload->saveUpload($tmp_name, $filename, $ajax = false): array|bool|string

Source: `wire/core/WireUpload.php`

Save the uploaded file

## Arguments

- string $tmp_name Temporary filename (full path and filename)
- string $filename Actual filename (basename)
- bool $ajax Is this an AJAX upload?

## Return value

array|bool|string Boolean false on fail, array of multiple filenames, or string of filename if maxFiles=1
