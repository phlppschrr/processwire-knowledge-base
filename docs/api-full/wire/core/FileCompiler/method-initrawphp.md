# $fileCompiler->initRawPHP(&$data)

Source: `wire/core/FileCompiler.php`

Populate the $this->rawPHP data which contains only raw php without quoted values

## Usage

~~~~~
// basic usage
$result = $fileCompiler->initRawPHP($data);

// usage with all arguments
$result = $fileCompiler->initRawPHP(&$data);
~~~~~

## Arguments

- `$data` `string`
