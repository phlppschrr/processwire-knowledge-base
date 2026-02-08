# Config: URLs

Source: `wire/core/Config.php`

@property Paths $urls Items from $config->urls reflect the http path one would use to load a given location in the web browser. URLs retrieved from $config->urls always end with a trailing slash. This is the same as the $urls API variable.

@property string $pageNameCharset Character set for page names, must be 'ascii' (default, lowercase) or 'UTF8' (uppercase).

@property string $pageNameWhitelist Whitelist of characters allowed in UTF8 page names.

@property string $pageNameUntitled Name to use for untitled pages (default="untitled").

@property string $pageNumUrlPrefix Prefix used for pagination URLs. Default is "page", resulting in "/page1", "/page2", etc.

@property array $pageNumUrlPrefixes Multiple prefixes that may be used for detecting pagination (internal use, for multi-language)

@property int $maxUrlSegments Maximum number of extra stacked URL segments allowed in a page's URL (including page numbers)

@property int $maxUrlSegmentLength Maximum length of any individual URL segment (default=128).

@property int $maxUrlDepth Maximum URL/path slashes (depth) for request URLs. (Min=10, Max=60)

@property int $longUrlResponse Response code when URL segments, depth or length exceeds max allowed. @since 3.0.243

@property int $maxPageNum Maximum number of recognized paginations
