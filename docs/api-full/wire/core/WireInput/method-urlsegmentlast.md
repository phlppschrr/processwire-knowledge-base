# $wireInput->urlSegmentLast($get = ''): string|int|bool

Source: `wire/core/WireInput.php`

Same as urlSegment() method but apply only to last URL segment. (since 3.0.155)

## Usage

~~~~~
// basic usage
$string = $wireInput->urlSegmentLast();

// usage with all arguments
$string = $wireInput->urlSegmentLast($get = '');
~~~~~
