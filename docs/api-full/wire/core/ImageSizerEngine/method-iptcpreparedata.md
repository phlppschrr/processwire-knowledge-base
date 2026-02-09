# $imageSizerEngine->iptcPrepareData($includeCustomTags = false): string

Source: `wire/core/ImageSizerEngine.php`

Prepare IPTC data (@horst)

## Usage

~~~~~
// basic usage
$string = $imageSizerEngine->iptcPrepareData();

// usage with all arguments
$string = $imageSizerEngine->iptcPrepareData($includeCustomTags = false);
~~~~~

## Arguments

- `$includeCustomTags` (optional) `bool` (default=false)

## Return value

- `string` $iptcNew
