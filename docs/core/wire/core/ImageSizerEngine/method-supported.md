# $imageSizerEngine->supported($action = 'imageformat'): bool

Source: `wire/core/ImageSizerEngine.php`

Is this ImageSizer class ready only means: does the server / system provide all Requirements!

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngine->supported();

// usage with all arguments
$bool = $imageSizerEngine->supported($action = 'imageformat');
~~~~~

## Arguments

- `$action` (optional) `string` Optional type of action supported.

## Return value

- `bool`
