# $pagefileExtra->noCacheURL($http = false): string

Source: `wire/core/PagefileExtra.php`

Get cache busted URL

## Usage

~~~~~
// basic usage
$string = $pagefileExtra->noCacheURL();

// usage with all arguments
$string = $pagefileExtra->noCacheURL($http = false);
~~~~~

## Hookable

- Hookable method name: `noCacheURL`
- Implementation: `___noCacheURL`
- Hook with: `$pagefileExtra->noCacheURL()`

## Arguments

- `$http` (optional) `bool`

## Return value

- `string`

## Since

3.0.194
