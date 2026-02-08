# $pages->___found(PageArray $pages, array $details)

Source: `wire/core/Pages.php`

Hook called at the end of a $pages->find(), includes extra info not seen in the resulting PageArray

## Arguments

- `$pages` `PageArray` The pages that were found
- `$details` `array` Extra information on how the pages were found, including: - `pageFinder` (PageFinder): The PageFinder instance that was used. - `pagesInfo` (array): The array returned by PageFinder. - `options` (array): Options that were passed to $pages->find().
