# $pagesLoader->normalizeSelector($selector, $convertIDs = true): array|int|string

Source: `wire/core/PagesLoader.php`

Normalize a selector

This is to reduce the number of unique selectors that produce the same result.
It is helpful with caching results, so that we don't cache the same results multiple
times because they used slightly different selectors.

## Arguments

- string|int|array $selector
- bool $convertIDs Convert ID-only selectors to integers or arrays of integers?

## Return value

array|int|string
