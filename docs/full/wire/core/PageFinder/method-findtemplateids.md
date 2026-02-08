# $pageFinder->findTemplateIDs($selectors, $options = array()): array

Source: `wire/core/PageFinder.php`

Find template ID for each page — returns array of template IDs indexed by page ID

## Usage

~~~~~
// basic usage
$array = $pageFinder->findTemplateIDs($selectors);

// usage with all arguments
$array = $pageFinder->findTemplateIDs($selectors, $options = array());
~~~~~

## Arguments

- `$selectors` `Selectors|string|array` Selectors object, selector string or selector array
- `$options` (optional) `array`

## Return value

- `array`

## Since

3.0.152
