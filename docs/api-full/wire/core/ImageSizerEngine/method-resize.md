# $imageSizerEngine->resize($finalWidth, $finalHeight): bool

Source: `wire/core/ImageSizerEngine.php`

Resize the image

The resize method does all pre and post-processing for the engines + calls the engine's
processResize() method.

Pre-processing is:
  Calculate and set dimensions, create a tempfile.

Post-processing is:
  Copy back and delete tempfile, write IPTC if necessary, reload imageinfo, set the modified flag.

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngine->resize($finalWidth, $finalHeight);
~~~~~

## Arguments

- `$finalWidth` `int`
- `$finalHeight` `int`

## Return value

- `bool`
