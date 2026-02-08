# $imageSizerEngineGD->imSaveReady($im, $filename): bool

Source: `wire/core/ImageSizerEngineGD.php`

Called before saving of image, returns true if save should proceed, false if not

Also Creates a webp file when settings indicate it should.

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngineGD->imSaveReady($im, $filename);
~~~~~

## Hookable

- Hookable method name: `imSaveReady`
- Implementation: `___imSaveReady`
- Hook with: `$imageSizerEngineGD->imSaveReady()`

## Arguments

- `$im` `resource`
- `$filename` `string` Source filename

## Return value

- `bool`
