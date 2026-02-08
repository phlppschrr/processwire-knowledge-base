# $pageimage->filenameDoesNotExist($filename): bool

Source: `wire/core/Pageimage.php`

Hook called by the size() method when a source/original filename does not exist

For the return value, override the default `false` return value and set
it to `true` in order to make it continue as if the filename did exist,
such as if your hook copied a file to $filename.

## Usage

~~~~~
// basic usage
$bool = $pageimage->filenameDoesNotExist($filename);
~~~~~

## Hookable

- Hookable method name: `filenameDoesNotExist`
- Implementation: `___filenameDoesNotExist`
- Hook with: `$pageimage->filenameDoesNotExist()`

## Arguments

- `$filename` `string`

## Return value

- `bool`

## Since

3.0.254
