# PageComparison::matches()

Source: `wire/core/PageComparison.php`

Given a Selectors object or a selector string, return whether this Page matches it

@param Page $page

@param string|array|Selectors $s

@param array $options Options to modify behavior (3.0.225+ only):
 - `useDatabase` (bool|null): Use database for matching rather than in-memory? (default=false)

@return bool
