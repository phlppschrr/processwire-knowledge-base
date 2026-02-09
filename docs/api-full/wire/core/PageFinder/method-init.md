# $pageFinder->init(Selectors $selectors, array $options): array

Source: `wire/core/PageFinder.php`

Initialize new find operation and prepare options

## Usage

~~~~~
// basic usage
$array = $pageFinder->init($selectors, $options);

// usage with all arguments
$array = $pageFinder->init(Selectors $selectors, array $options);
~~~~~

## Arguments

- `$selectors` `Selectors`
- `$options` `array`

## Return value

- `array` Returns updated options with all present
