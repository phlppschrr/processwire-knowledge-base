# $imageSizerEngineGD->supported($action = 'imageformat'): bool

Source: `wire/core/ImageSizerEngineGD.php`

Return whether or not GD can proceed - Is the current image(sub)format supported?

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngineGD->supported();

// usage with all arguments
$bool = $imageSizerEngineGD->supported($action = 'imageformat');
~~~~~

## Arguments

- `$action` (optional) `string`

## Return value

- `bool`
