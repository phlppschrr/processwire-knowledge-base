# Template: URLs

Source: `wire/core/Template.php`

- $allowPageNum: int Allow page numbers in URLs? (0=no, 1=yes)

- [$urlSegments: int|string](method-urlsegments.md) Allow URL segments on pages? (0=no, 1=yes (all), string=space separted list of segments to allow)

- $https: int Use https? (0 = http or https, 1 = https only, -1 = http only)

- $slashUrls: int Page URLs should have a trailing slash? 1 = yes, 0 = no

- $slashPageNum: string|int Should PageNum segments have a trailing slash? (0=either, 1=yes, -1=no) applies only if allowPageNum!=0.

- $slashUrlSegments: string|int Should last URL segment have a trailing slash? (0=either, 1=yes, -1=no) applies only if urlSegments!=0.
