# $fileCompiler->__construct($sourcePath, array $options = array())

Source: `wire/core/FileCompiler.php`

Construct

## Usage

~~~~~
// basic usage
$result = $fileCompiler->__construct($sourcePath);

// usage with all arguments
$result = $fileCompiler->__construct($sourcePath, array $options = array());
~~~~~

## Arguments

- `$sourcePath` `string` Path where source files are located
- `$options` (optional) `array` Indicate which compilations should be performed (default='includes' and 'namespace')
