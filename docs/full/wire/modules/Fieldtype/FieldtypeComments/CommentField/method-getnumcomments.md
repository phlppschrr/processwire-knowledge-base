# $commentField->getNumComments(Page $page, array $options = array()): int

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Get number of comments for Page, optionally limited by specific $options

Unlike the count() method this is focused on a specific Page and may be faster in
cases where it matches what you need to count.

## Arguments

- `$page` `Page`
- `$options` (optional) `array` - `status` (int): Specify Comment::status* constant to include only this status - `minStatus` (int): Specify Comment::status* constant to include only comments with at least this status - `maxStatus` (int): Specify Comment::status* constant or include only comments up to this status - `parent` (int|Comment): Specify parent comment ID, 0 for root-only, or omit for no parent limitation - `minCreated` (int): Minimum created unix timestamp - `maxCreated` (int): Maximum created unix timestamp - `stars` (int): Number of stars to match (1-5) - `minStars` (int): Minimum number of stars to match (1-5) - `maxStars` (int): Maximum number of stars to match (1-5)

## Return value

int

## Since

3.0.153
