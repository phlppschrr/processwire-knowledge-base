# PageComparison

Source: `wire/core/PageComparison.php`

ProcessWire Page Comparison

Provides implementation for Page comparison functions.

Methods:
- [`is(Page $page, int|string|array|Selectors|Page|Template $status): bool`](method-is.md)
- [`_if(Page $page, string|bool|int $key, string|callable|mixed $yes = '', string|callable|mixed $no = ''): mixed|string|bool`](method-_if.md)
- [`matches(Page $page, string|array|Selectors $s, array $options = array()): bool`](method-matches.md)
- [`selectorMatches(Page $page, Selector $selector): bool`](method-selectormatches.md)
- [`selectorMatchesProperty(Page $page, Selector $selector, string $property): bool`](method-selectormatchesproperty.md)
- [`getObjectValueArray(Wire|object $object, string $property = ''): array`](method-getobjectvaluearray.md)
- [`isEqual(Page $page, string $key, mixed $value1, mixed $value2): bool`](method-isequal.md)
