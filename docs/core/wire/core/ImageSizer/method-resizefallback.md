# $imageSizer->resizeFallback($targetWidth, $targetHeight = 0): bool

Source: `wire/core/ImageSizer.php`

GD is the fallback ImageEngine, it gets invoked if there is no other Engine defined,

or if a defined Engine is not available,
or if an invoked Engine failes with the image manipulation.

## Usage

~~~~~
// basic usage
$bool = $imageSizer->resizeFallback($targetWidth);

// usage with all arguments
$bool = $imageSizer->resizeFallback($targetWidth, $targetHeight = 0);
~~~~~

## Arguments

- `$targetWidth` `mixed`
- `$targetHeight` (optional) `mixed`

## Return value

- `bool`
