# $imageSizerEngineGD->_processActionFlip(&$img, $flipType): bool|resource

Source: `wire/core/ImageSizerEngineGD.php`

Process flip action (internal)

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngineGD->_processActionFlip($img, $flipType);

// usage with all arguments
$bool = $imageSizerEngineGD->_processActionFlip(&$img, $flipType);
~~~~~

## Arguments

- `$img` `resource`
- `$flipType` `string` vertical, horizontal or both

## Return value

- `bool|resource`
