# $notices->removeNotice($item): self

Source: `wire/core/Notices.php`

Remove a Notice

Like the remove() method but also removes persist notices.

## Usage

~~~~~
// basic usage
$result = $notices->removeNotice($item);
~~~~~

## Arguments

- `$item` `string|Notice` Accepts a Notice object or Notice ID string.

## Return value

- `self`

## Since

3.0.149
