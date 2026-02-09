# Config: URLs

Source: `wire/core/Config.php`

- [$urls: Paths](method-urls.md) Items from $config->urls reflect the http path one would use to load a given location in the web browser. URLs retrieved from $config->urls always end with a trailing slash. This is the same as the $urls API variable.

- $pageNameCharset: string Character set for page names, must be 'ascii' (default, lowercase) or 'UTF8' (uppercase).

- $pageNameWhitelist: string Whitelist of characters allowed in UTF8 page names.

- $pageNameUntitled: string Name to use for untitled pages (default="untitled").

- $pageNumUrlPrefix: string Prefix used for pagination URLs. Default is "page", resulting in "/page1", "/page2", etc.

- $pageNumUrlPrefixes: array Multiple prefixes that may be used for detecting pagination (internal use, for multi-language)

- $maxUrlSegments: int Maximum number of extra stacked URL segments allowed in a page's URL (including page numbers)

- $maxUrlSegmentLength: int Maximum length of any individual URL segment (default=128).

- $maxUrlDepth: int Maximum URL/path slashes (depth) for request URLs. (Min=10, Max=60)

- $longUrlResponse: int Response code when URL segments, depth or length exceeds max allowed. @since 3.0.243

- $maxPageNum: int Maximum number of recognized paginations
