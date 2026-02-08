# WireInput: URL-segments

Source: `wire/core/WireInput.php`

@property array|string[] $urlSegments Retrieve all URL segments (array). This requires url segments are enabled on the template of the requested page. You can turn it on or off under the url tab when editing a template.

@property string $urlSegmentStr Alias of urlSegmentsStr

@property string $urlSegment1 First URL segment

@property string $urlSegment2 Second URL segment

@property string $urlSegment3 Third URL segment, and so on...

@property string $urlSegmentLast Last URL segment (since 3.0.155)

@property string $urlSegmentFirst Alias of $urlSegment1 (since 3.0.155)

@method string|int|bool urlSegment1($get = '') Same as urlSegment() method but apply only to 1st URL segment. (since 3.0.155)

@method string|int|bool urlSegment2($get = '') Same as urlSegment() method but apply only to 2nd URL segment. (since 3.0.155)

@method string|int|bool urlSegment3($get = '') Same as urlSegment() method but apply only to 3rd URL segment. (since 3.0.155)

@method string|int|bool urlSegmentLast($get = '') Same as urlSegment() method but apply only to last URL segment. (since 3.0.155)

@method string|int|bool urlSegmentFirst($get = '') Same as urlSegment() method but apply only to first URL segment. (since 3.0.155)
