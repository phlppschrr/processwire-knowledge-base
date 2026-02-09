# $wireInput->urlSegmentFirst($get = ''): string|int|bool

Source: `wire/core/WireInput.php`

Same as urlSegment() method but apply only to first URL segment. (since 3.0.155)

## Usage

~~~~~
// basic usage
$string = $wireInput->urlSegmentFirst();

// usage with all arguments
$string = $wireInput->urlSegmentFirst($get = '');
~~~~~
