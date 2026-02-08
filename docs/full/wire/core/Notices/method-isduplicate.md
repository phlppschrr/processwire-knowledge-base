# $notices->isDuplicate(Notice $item): bool|Notice

Source: `wire/core/Notices.php`

Is the given Notice a duplicate of one already here?

## Usage

~~~~~
// basic usage
$bool = $notices->isDuplicate($item);

// usage with all arguments
$bool = $notices->isDuplicate(Notice $item);
~~~~~

## Arguments

- `$item` `Notice`

## Return value

- `bool|Notice` Returns Notice that it duplicate sor false if not a duplicate
