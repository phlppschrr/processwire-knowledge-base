# $pageimage->___filenameDoesNotExist($filename): bool

Source: `wire/core/Pageimage.php`

Hook called by the size() method when a source/original filename does not exist

For the return value, override the default `false` return value and set
it to `true` in order to make it continue as if the filename did exist,
such as if your hook copied a file to $filename.

## Arguments

- string $filename

## Return value

bool

## Meta

- @since 3.0.254
