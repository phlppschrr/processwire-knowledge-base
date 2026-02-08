# $wireUpload->addUploadedFilename($completedFilename, $originalFilename)

Source: `wire/core/WireUpload.php`

Add a completed upload file name and its original name

## Usage

~~~~~
// basic usage
$result = $wireUpload->addUploadedFilename($completedFilename, $originalFilename);
~~~~~

## Arguments

- `$completedFilename` `string` Sanitized filename or basename that was used for saved file
- `$originalFilename` `string` Unsanitized filename as uploaded
