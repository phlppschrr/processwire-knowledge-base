# Template: URLs

Source: `wire/core/Template.php`

@property int $allowPageNum Allow page numbers in URLs? (0=no, 1=yes)

@property int|string $urlSegments Allow URL segments on pages? (0=no, 1=yes (all), string=space separted list of segments to allow)

@property int $https Use https? (0 = http or https, 1 = https only, -1 = http only)

@property int $slashUrls Page URLs should have a trailing slash? 1 = yes, 0 = no

@property string|int $slashPageNum Should PageNum segments have a trailing slash? (0=either, 1=yes, -1=no) applies only if allowPageNum!=0.

@property string|int $slashUrlSegments Should last URL segment have a trailing slash? (0=either, 1=yes, -1=no) applies only if urlSegments!=0.
