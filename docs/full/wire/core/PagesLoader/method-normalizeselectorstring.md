# $pagesLoader->normalizeSelectorString($selector, $convertIDs = true): array|int|string

Source: `wire/core/PagesLoader.php`

Normalize a selector string

This is to reduce the number of unique selectors that produce the same result.
It is helpful with caching results, so that we don't cache the same results multiple
times because they used slightly different selectors.

## Usage

~~~~~
// basic usage
$array = $pagesLoader->normalizeSelectorString($selector);

// usage with all arguments
$array = $pagesLoader->normalizeSelectorString($selector, $convertIDs = true);
~~~~~

## Arguments

- `$selector` `string`
- `$convertIDs` (optional) `bool` Normalize to integer ID or array of integer IDs when possible (default=true)

## Return value

- `array|int|string`
