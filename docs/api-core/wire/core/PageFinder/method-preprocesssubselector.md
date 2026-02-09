# $pageFinder->preProcessSubSelector(Selector $selector, Selectors $parentSelectors)

Source: `wire/core/PageFinder.php`

Pre-process a Selector that has a [quoted selector] embedded within its value

## Usage

~~~~~
// basic usage
$result = $pageFinder->preProcessSubSelector($selector, $parentSelectors);

// usage with all arguments
$result = $pageFinder->preProcessSubSelector(Selector $selector, Selectors $parentSelectors);
~~~~~

## Arguments

- `$selector` `Selector`
- `$parentSelectors` `Selectors`
