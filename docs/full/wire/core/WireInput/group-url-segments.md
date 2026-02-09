# WireInput: URL-segments

Source: `wire/core/WireInput.php`

- [$urlSegments: array|string[]](method-urlsegments.md) Retrieve all URL segments (array). This requires url segments are enabled on the template of the requested page. You can turn it on or off under the url tab when editing a template.

- [$urlSegmentStr: string](method-urlsegmentstr.md) Alias of urlSegmentsStr

- $urlSegment1: string First URL segment

- $urlSegment2: string Second URL segment

- $urlSegment3: string Third URL segment, and so on...

- $urlSegmentLast: string Last URL segment (since 3.0.155)

- $urlSegmentFirst: string Alias of $urlSegment1 (since 3.0.155)

- urlSegment1($get = ''): string|int|bool Same as urlSegment() method but apply only to 1st URL segment. (since 3.0.155)

- urlSegment2($get = ''): string|int|bool Same as urlSegment() method but apply only to 2nd URL segment. (since 3.0.155)

- urlSegment3($get = ''): string|int|bool Same as urlSegment() method but apply only to 3rd URL segment. (since 3.0.155)

- urlSegmentLast($get = ''): string|int|bool Same as urlSegment() method but apply only to last URL segment. (since 3.0.155)

- urlSegmentFirst($get = ''): string|int|bool Same as urlSegment() method but apply only to first URL segment. (since 3.0.155)
