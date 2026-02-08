# $comment->quiet($quiet = null): bool

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Get or set quiet mode

When quiet mode is active, comment additions/changes don't trigger notifications and such.

## Usage

~~~~~
// basic usage
$bool = $comment->quiet();

// usage with all arguments
$bool = $comment->quiet($quiet = null);
~~~~~

## Arguments

- `$quiet` (optional) `bool` Specify only if setting

## Return value

- `bool` The current quiet mode
