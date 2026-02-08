# $pageimage->webp(array $webpOptions = array()): PagefileExtra

Source: `wire/core/Pageimage.php`

Get WebP "extra" version of this Pageimage

## Usage

~~~~~
// basic usage
$pagefileExtra = $pageimage->webp();

// usage with all arguments
$pagefileExtra = $pageimage->webp(array $webpOptions = array());
~~~~~

## Arguments

- `$webpOptions` (optional) `array` Optionally override certain defaults from `$config->webpOptions` (requires 3.0.229+): - `useSrcUrlOnSize` (bool): Fallback to source file URL when webp file is larger than source? (default=true) - `useSrcUrlOnFail` (bool): Fallback to source file URL when webp file fails for some reason? (default=true) - `quality' (int): Quality setting of 1-100 where higher is better but larger in file size (default=90) Note that his quality setting is only used if the .webp file does not already exist.

## Return value

- `PagefileExtra`

## Since

3.0.132
