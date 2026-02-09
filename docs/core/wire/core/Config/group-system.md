# Config: system

Source: `wire/core/Config.php`

- [`$version: string`](method-version.md) Current ProcessWire version string (i.e. "2.2.3")
- `$systemVersion: int` System version, used by SystemUpdater to determine when updates must be applied.
- `$adminEmail: string` Email address to send fatal error notifications to.
- `$adminTemplates: array` Names of templates that ProcessWire should consider exclusive to the admin. @since 3.0.142
- `$advanced: bool` Special mode for ProcessWire system development. Not recommended for regular site development or production use.
- `$demo: bool` Special mode for demonstration use that causes POST requests to be disabled. Applies to core, but may not be safe with 3rd party modules.
- `$debug: bool|int|string` Special mode for use when debugging or developing a site. Recommended TRUE when site is in development and FALSE when not. Or set to `Config::debug*` constant.
- `$debugIf: string|callable|array` Enable debug mode if condition is met. One of IP address to match, regex to match IP, array of IPs to match, or callable function that returns true|false.
- `$debugTools: array` Tools, and their order, to show in debug mode (admin)
- [`$wireMail: array`](method-wiremail.md) Default WireMail module settings. See /wire/config.php $config->wireMail for details.
- `$fatalErrorHTML: string` HTML used for fatal error messages in HTTP mode.
- `$fatalErrorCode: int` HTTP code to send on fatal error (typically 500 or 503).
- `$preloadCacheNames: array` Cache names to preload at beginning of request
- `$allowExceptions: bool` Allow Exceptions to propagate? (default=false, specify true only if you implement your own exception handler)
- `$usePoweredBy: bool` Use the x-powered-by header? Set to false to disable.
- `$useFunctionsAPI: bool` Allow most API variables to be accessed as functions? (see /wire/core/FunctionsAPI.php)
- `$useMarkupRegions: bool|int` Enable support for front-end markup regions? True to enable or int 2 to enable also with file regions.
- `$useLazyLoading: bool|array` Delay loading of fields (and templates/fieldgroups) till requested? Can improve performance on systems with lots of fields or templates. @since 3.0.193
- `$usePageClasses: bool` Use custom Page classes in `/site/classes/[TemplateName]Page.php`? @since 3.0.152
- `$useVersionUrls: bool|int|string|null` Default value for $useVersion argument of $config->versionUrls() method @since 3.0.227
- `$lazyPageChunkSize: int` Chunk size for for $pages->findMany() calls.
- `$tableSalt: string` Additional hash for other (non-authentication) purposes. @since 3.0.164
- [`$statusFiles: array`](method-statusfiles.md) File inclusions for ProcessWire’s runtime statuses/states. @since 3.0.142
- `$phpMailAdditionalParameters: string|null` Additional params to pass to PHP’s mail() function (when used), see $additional_params argument at https://www.php.net/manual/en/function.mail.php
- `$installed: int` Timestamp of when this PW was installed, set automatically by the installer for future compatibility detection.
