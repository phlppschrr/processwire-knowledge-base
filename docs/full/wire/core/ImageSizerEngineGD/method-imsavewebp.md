# $imageSizerEngineGD->imSaveWebP($im, $filename, $quality = 90): boolean

Source: `wire/core/ImageSizerEngineGD.php`

Create WebP image (@horst)
Is requested by image options: ["webpAdd" => true] OR ["webpOnly" => true]

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngineGD->imSaveWebP($im, $filename);

// usage with all arguments
$bool = $imageSizerEngineGD->imSaveWebP($im, $filename, $quality = 90);
~~~~~

## Arguments

- `$im` `resource`
- `$filename` `string`
- `$quality` (optional) `int`

## Return value

- `boolean` true | false
