# $imageSizerEngineGD->processAction($srcFilename, $dstFilename, $action, $value): bool

Source: `wire/core/ImageSizerEngineGD.php`

Process a rotate or flip action

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngineGD->processAction($srcFilename, $dstFilename, $action, $value);
~~~~~

## Arguments

- `$srcFilename` `string`
- `$dstFilename` `string`
- `$action` `string` One of 'rotate' or 'flip'
- `$value` `int|string` If rotate, specify int of degrees. If flip, specify one of 'vertical', 'horizontal' or 'both'.

## Return value

- `bool`

## Exceptions

- `WireException`
