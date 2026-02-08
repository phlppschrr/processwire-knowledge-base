# PagesLoader::normalizeSelectorString()

Source: `wire/core/PagesLoader.php`

Normalize a selector string

This is to reduce the number of unique selectors that produce the same result.
It is helpful with caching results, so that we don't cache the same results multiple
times because they used slightly different selectors.

@param string $selector

@param bool $convertIDs Normalize to integer ID or array of integer IDs when possible (default=true)

@return array|int|string
