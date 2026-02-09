# $wireInput->urlSegment1($get = ''): string|int|bool

Source: `wire/core/WireInput.php`

Same as urlSegment() method but apply only to 1st URL segment. (since 3.0.155)

## Usage

~~~~~
// basic usage
$string = $wireInput->urlSegment1();

// usage with all arguments
$string = $wireInput->urlSegment1($get = '');
~~~~~
