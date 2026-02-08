# $sanitizer->validateFile($filename, array $options = array()): bool|array|null

Source: `wire/core/Sanitizer.php`

Validate and sanitize a file using FileValidator modules

This is intended for validating file data, not file names. Depending on the FileValidator
modules that are used, they may sanitize the file in order ot make it valid.

IMPORTANT: This method returns NULL if it can’t find a validator for the file. This does
not mean the file is invalid, just that it didn't have the tools to validate it. If the
getArray option is specified then it would return a blank array rather than null.

**getArray option** (3.0.167+):
When specifying true for the `getArray` option this method will return an associative array
of validation results indexed by module name. The values for each module name will be either
true (file validates as-is), 1 (file valid after it was sanitized), or false (file not valid
and cannot be sanitized). A blank array is returned if no modules could perform the validation.

**dryrun option** (3.0.167+):
When specifying true for the `dryrun` option please note that no validation is performed and
instead the method returns true or false as to whether or not the file can be validated. It
only looks at the file extension, so the file need not exist. Meaning it’s also okay to specify
filename like “test.jpg” without path, when using this option. If using the dryrun option with
the `getArray` option then it will return an array of module names that would perform the
validation for the given file type (or blank array if none).

## Arguments

- string $filename Full path and filename to validate
- array $options When available, provide array with any one or all of the following: - `page` (Page): Page object associated with $filename. (default=null) - `field` (Field): Field object associated with $filename. (default=null) - `pagefile` (Pagefile): Pagefile object associated with $filename. (default=null) - `getArray` (bool): Return array of results rather than a boolean? (default=false) Added 3.0.167 - `dryrun` (bool|int): Specify true to only return if the file can be validated with this method, without actually performing any validation. (default=false). Added 3.0.167

## Return value

bool|array|null Returns one of the following, depending on use of dryrun and getArray options: - Boolean true if valid, false if not. - NULL if no validator available for given file type or file does not exist. - If dryrun option is used, returns boolean (or array of strings if getArray option is true). - If getArray option is used, returns associative array of results or blank array if no validators.
