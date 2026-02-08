# Config: system

Source: `wire/core/Config.php`

@property string $version Current ProcessWire version string (i.e. "2.2.3")

@property int $systemVersion System version, used by SystemUpdater to determine when updates must be applied.

@property string $adminEmail Email address to send fatal error notifications to.

@property array $adminTemplates Names of templates that ProcessWire should consider exclusive to the admin. @since 3.0.142

@property bool $advanced Special mode for ProcessWire system development. Not recommended for regular site development or production use.

@property bool $demo Special mode for demonstration use that causes POST requests to be disabled. Applies to core, but may not be safe with 3rd party modules.

@property bool|int|string $debug Special mode for use when debugging or developing a site. Recommended TRUE when site is in development and FALSE when not. Or set to `Config::debug*` constant.

@property string|callable|array $debugIf Enable debug mode if condition is met. One of IP address to match, regex to match IP, array of IPs to match, or callable function that returns true|false.

@property array $debugTools Tools, and their order, to show in debug mode (admin)

@property array $wireMail Default WireMail module settings. See /wire/config.php $config->wireMail for details.

@property string $fatalErrorHTML HTML used for fatal error messages in HTTP mode.

@property int $fatalErrorCode HTTP code to send on fatal error (typically 500 or 503).

@property array $preloadCacheNames Cache names to preload at beginning of request

@property bool $allowExceptions Allow Exceptions to propagate? (default=false, specify true only if you implement your own exception handler)

@property bool $usePoweredBy Use the x-powered-by header? Set to false to disable.

@property bool $useFunctionsAPI Allow most API variables to be accessed as functions? (see /wire/core/FunctionsAPI.php)

@property bool|int $useMarkupRegions Enable support for front-end markup regions? True to enable or int 2 to enable also with file regions.

@property bool|array $useLazyLoading Delay loading of fields (and templates/fieldgroups) till requested? Can improve performance on systems with lots of fields or templates. @since 3.0.193

@property bool $usePageClasses Use custom Page classes in `/site/classes/[TemplateName]Page.php`? @since 3.0.152

@property bool|int|string|null $useVersionUrls Default value for $useVersion argument of $config->versionUrls() method @since 3.0.227

@property int $lazyPageChunkSize Chunk size for for $pages->findMany() calls.

@property string $tableSalt Additional hash for other (non-authentication) purposes. @since 3.0.164

@property array $statusFiles File inclusions for ProcessWire’s runtime statuses/states. @since 3.0.142

@property string|null $phpMailAdditionalParameters Additional params to pass to PHP’s mail() function (when used), see $additional_params argument at https://www.php.net/manual/en/function.mail.php

@property int $installed Timestamp of when this PW was installed, set automatically by the installer for future compatibility detection.
