# $pageFinder->getIncludeSelector($selectors): string

Source: `wire/core/PageFinder.php`

Get the include|status|check_access portions from given Selectors and return selector string for them

If given $selectors lacks an include or check_access selector, then it will pull from the
equivalent PageFinder setting if present in the original initiating selector.

## Arguments

- Selectors|string $selectors

## Return value

string
