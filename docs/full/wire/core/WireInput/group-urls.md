# WireInput: URLs

Source: `wire/core/WireInput.php`

@property int $pageNum Current page number (where 1 is first)

@property string $url Current requested URL including page numbers and URL segments, excluding query string.

@property string $httpUrl Like $url but includes the scheme/protcol and hostname.

@property string $queryString Current query string

@property string $scheme Current scheme/protcol, i.e. http or https
