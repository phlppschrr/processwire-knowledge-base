# PageComparison

Source: `wire/core/PageComparison.php`

## Summary

ProcessWire Page Comparison

Common methods:
- [`is()`](method-is.md)
- [`_if()`](method-_if.md)
- [`matches()`](method-matches.md)
- [`selectorMatches()`](method-selectormatches.md)
- [`selectorMatchesProperty()`](method-selectormatchesproperty.md)

Provides implementation for Page comparison functions.

## Methods
- [`is(Page $page, int|string|array|Selectors|Page|Template $status): bool`](method-is.md) Is this page of the given type? (status, template, etc.)
- [`_if(Page $page, string|bool|int $key, string|callable|mixed $yes = '', string|callable|mixed $no = ''): mixed|string|bool`](method-_if.md) If value is available for $key return or call $yes condition (with optional $no condition)
- [`matches(Page $page, string|array|Selectors $s, array $options = array()): bool`](method-matches.md) Given a Selectors object or a selector string, return whether this Page matches it
- [`selectorMatches(Page $page, Selector $selector): bool`](method-selectormatches.md) Return whether individual Selector object matches Page
- [`selectorMatchesProperty(Page $page, Selector $selector, string $property): bool`](method-selectormatchesproperty.md) Return whether single property from individual Selector matches Page
- [`getObjectValueArray(Wire|object $object, string $property = ''): array`](method-getobjectvaluearray.md) Given an object, return the value(s) it represents (optionally from a property in the object)
- [`isEqual(Page $page, string $key, mixed $value1, mixed $value2): bool`](method-isequal.md) Is $value1 equal to $value2?
