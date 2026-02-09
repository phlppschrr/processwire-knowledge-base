# $comment->numChildren(array $options = array()): int

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Return number of children (replies) for this comment

## Example

~~~~~
$qty = $comment->numChildren([ 'minStatus' => Comment::statusApproved ]);
~~~~~

## Usage

~~~~~
// basic usage
$int = $comment->numChildren();

// usage with all arguments
$int = $comment->numChildren(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array` Limit return value by specific properties (below): - `status` (int): Specify Comment::status* constant to include only this status - `minStatus` (int): Specify Comment::status* constant to include only comments with at least this status - `maxStatus` (int): Specify Comment::status* constant or include only comments up to this status - `minCreated` (int): Minimum created unix timestamp - `maxCreated` (int): Maximum created unix timestamp - `stars` (int): Number of stars to match (1-5) - `minStars` (int): Minimum number of stars to match (1-5) - `maxStars` (int): Maximum number of stars to match (1-5)

## Return value

- `int`

## Since

3.0.153
