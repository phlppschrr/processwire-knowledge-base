# $wireInput->urlSegmentMatch($get, $num = 0): string|int|bool

Source: `wire/core/WireInput.php`

Handles find/match logic for URL segment methods

## Usage

~~~~~
// basic usage
$string = $wireInput->urlSegmentMatch($get);

// usage with all arguments
$string = $wireInput->urlSegmentMatch($get, $num = 0);
~~~~~

## Arguments

- `$get` `string` URL segment match string
- `$num` (optional) `int` Limit only to this URL segment number (default=0 to indicate ignore)

## Return value

- `string|int|bool`

## Since

3.0.155
