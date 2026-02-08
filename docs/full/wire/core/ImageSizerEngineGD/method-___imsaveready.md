# $imageSizerEngineGD->___imSaveReady($im, $filename): bool

Source: `wire/core/ImageSizerEngineGD.php`

Called before saving of image, returns true if save should proceed, false if not

Also Creates a webp file when settings indicate it should.

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngineGD->___imSaveReady($im, $filename);
~~~~~

## Arguments

- `$im` `resource`
- `$filename` `string` Source filename

## Return value

- `bool`
