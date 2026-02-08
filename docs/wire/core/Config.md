# Config

Source: `wire/core/Config.php`

ProcessWire Config

Handles ProcessWire configuration data

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

Holds ProcessWire configuration settings as defined in /wire/config.php and /site/config.php.
Javascript configuration
For more detailed descriptions of these $config properties, including default values, see the
[/wire/config.php](https://github.com/processwire/processwire/blob/master/wire/config.php) file.


@see /wire/config.php for more detailed descriptions of all config properties.

## admin

@property array $logs Additional core logs to keep

@property bool $logIP Include IP address in logs, when applicable?

@property string $defaultAdminTheme Default admin theme: AdminThemeUikit, AdminThemeDefault or AdminThemeReno.

@property array $AdminThemeUikit Settings specific to AdminThemeUikit module (see this setting in /wire/config.php). @since 3.0.179

@property array $modals Settings for modal windows

## database

@property string $dbHost Database host

@property string $dbName Database name

@property string $dbUser Database user

@property string $dbPass Database password

@property string $dbPort Database port (default=3306)

@property string $dbCharset Default is 'utf8' but 'utf8mb4' is also supported.

@property string $dbEngine Database engine (MyISAM or InnoDB)

@property string $dbSocket Optional DB socket config for sites that need it.

@property bool $dbCache Whether to allow MySQL query caching.

@property bool $dbLowercaseTables Force any created field_* tables to be lowercase.

@property string $dbPath MySQL database exec path (Path to mysqldump)

@property array $dbOptions Any additional driver options to pass as $options argument to "new PDO(...)".

@property array $dbSqlModes Set or adjust SQL mode per MySQL version, where array keys are MySQL version and values are SQL mode command(s).

@property int $dbQueryLogMax Maximum number of queries WireDatabasePDO will log in memory, when debug mode is enabled (default=1000).

@property string $dbInitCommand Database init command, for PDO::MYSQL_ATTR_INIT_COMMAND. Note placeholder {charset} gets replaced with $config->dbCharset.

@property bool $dbStripMB4 When dbEngine is not utf8mb4 and this is true, we will attempt to remove 4-byte characters (like emoji) from inserts when possible. Note that this adds some overhead.

@property array|null $dbReader Configuration values for read-only database connection (if available). @since 3.0.175

## date-time

@property string $dateFormat Default system date format, preferably in sortable string format. Default is 'Y-m-d H:i:s'

@property string $timezone Current timezone using PHP timeline options: http://php.net/manual/en/timezones.php

## files

@property bool $pagefileSecure When used, files in /site/assets/files/ will be protected with the same access as the page. Routes files through a passthrough script. Note if applying to existing site it may not affect existing pages and file/image fields until they are accessed or saved.

@property string $pagefileSecurePathPrefix One or more characters prefixed to the pathname of protected file dirs. This should be some prefix that the .htaccess file knows to block requests for.

@property array $fileContentTypes Array of extensions and the associated MIME type for each (for file output). See /wire/config.php for details and defaults.

@property array $fileCompilerOptions Array of options for FileCompiler class. See /wire/config.php for details and defaults.

@property string $chmodDir Octal string permissions assigned to directories created by ProcessWire

@property string $chmodFile Octal string permissions assigned to files created by ProcessWire

@property bool $chmodWarn Set to false to suppress warnings about 0666/0777 file permissions that are potentially too loose

@property string $uploadTmpDir Optionally override PHP's upload_tmp_dir with your own. Should include a trailing slash.

@property string $uploadBadExtensions Space separated list of file extensions that are always disallowed from uploads.

@property bool $pagefileExtendedPaths Use extended file mapping?

## HTTP-and-input

@property string $httpHost Current HTTP host name.

@property bool $protectCSRF Enables CSRF (cross site request forgery) protection on all PW forms, recommended for security.

@property string $wireInputOrder Order that variables with the $input API var are handled when you access $input->var.

@property bool $wireInputLazy Specify true for $input API var to load input data in a lazy fashion and potentially use less memory. Default is false.

@property int $wireInputArrayDepth Maximum multi-dimensional array depth for input variables accessed from $input or 1 to only allow single dimension arrays. @since 3.0.178

@property array $cookieOptions Options for setting cookies from $input->cookie

@property array $httpHosts HTTP hosts For added security, specify the host names ProcessWire should recognize.

@property bool|string|array $noHTTPS When boolean true, pages requiring HTTPS will not enforce it (useful for dev environments). May also specify hostname (string) or hostnames (array) to disable HTTPS for.

## images

@property array $imageSizes Predefined image sizes (and options) indexed by name. See /wire/config.php for example. @since 3.0.151

@property array $imageSizerOptions Options to set image sizing defaults. Please see the /wire/config.php file for all options and defaults.

@property array $webpOptions Options for webp images. Please see /wire/config.php for all options.

@property array $adminThumbOptions Admin thumbnail image options

## modules

@property array $pageList Settings specific to Page lists.

@property array $pageEdit Settings specific to Page editors.

@property array $pageAdd Settings specific to Page adding.

@property string $moduleServiceURL URL where the modules web service can be accessed

@property string $moduleServiceKey API key for modules web service

@property bool $moduleCompile Allow use of compiled modules?

@property array $moduleInstall Admin module install options you allow.

@property array $substituteModules Associative array with names of substitute modules for when requested module doesn't exist

@property array $markupQA Optional settings for MarkupQA class used by FieldtypeTextarea module.

## other

@method array|string wireMail($key = '', $value = null)

@method array imageSizes($key = '', $value = null)

@method array|bool|string|int|float imageSizerOptions($key = '', $value = null)

@method array|int|bool webpOptions($key = '', $value = null)

@method array|string contentTypes($key = '', $value = null)

@method array|string fileContentTypes($key = '', $value = null)

@method array|string|bool fileCompilerOptions($key = '', $value = null)

@method array|string|string[] dbOptions($key = '', $value = null)

@method array|string|string[] dbSqlModes($key = '', $value = null)

@method array|int|bool pageList($key = '', $value = null)

@method array|bool pageEdit($key = '', $value = null)

@method array|string pageAdd($key = '', $value = null)

@method array|string moduleInstall($key = '', $value = null)

@method array|string substituteModules($key = '', $value = null)

@method array|string|bool AdminThemeUikit($key = '', $value = null)

@method array|string modals($key = '', $value = null)

@method array|bool markupQA($key = '', $value = null)

@method array|string statusFiles($key = '', $value = null)

## paths

@property Paths $paths All of what can be accessed from $config->urls can also be accessed from $config->paths, with one important difference: the returned value is the full disk path on the server. There are also a few items in $config->paths that aren't in $config->urls. All entries in $config->paths always end with a trailing slash.

## runtime

@property bool $ajax If the current request is an ajax (asynchronous javascript) request, this is set to true.

@property bool|int $modal If the current request is in a modal window, this is set to a positive number. False if not.

@property bool|int $admin Is current request for logged-in user in admin? True, false, or 0 if not yet known. @since 3.0.142

@property bool $https If the current request is an HTTPS request, this is set to true.

@property FilenameArray $styles Array used by ProcessWire admin to keep track of what stylesheet files its template should load. It will be blank otherwise. Feel free to use it for the same purpose in your own sites.

@property FilenameArray $scripts Array used by ProcessWire admin to keep track of what javascript files its template should load. It will be blank otherwise. Feel free to use it for the same purpose in your own sites.

@property Paths $urls Items from $config->urls reflect the http path one would use to load a given location in the web browser. URLs retrieved from $config->urls always end with a trailing slash. This is the same as the $urls API variable.

@property bool $internal This is automatically set to FALSE when PW is externally bootstrapped.

@property bool $cli This is automatically set to TRUE when PW is booted as a command line (non HTTP) script.

@property string $serverProtocol Current server protocol, one of: HTTP/1.1, HTTP/1.0, HTTP/2, or HTTP/2.0. @since 3.0.166

@property string $versionName This is automatically populated with the current PW version name (i.e. 2.5.0 dev)

@property string|null $pagerHeadTags Populated at runtime to contain `<link rel=prev|next />` tags for document head, after pagination has been rendered by MarkupPagerNav module.

## session

@property string $sessionName Default session name to use (default='wire')

@property string $sessionNameSecure Session name when on HTTPS. Used when the sessionCookieSecure option is enabled (default). When blank (default), it will assume sessionName + 's'.

@property bool|int $sessionCookieSecure Use secure cookies when on HTTPS? When enabled, separate sessions will be maintained for HTTP vs. HTTPS. Good for security but tradeoff is login session may be lost when switching (default=1 or true).

@property null|string $sessionCookieDomain Domain to use for sessions, which enables a session to work across subdomains, or NULL to disable (default/recommended).

@property string $sessionCookieSameSite Cookie “SameSite” value for sessions - “Lax” (default) or “Strict”. @since 3.0.178

@property bool|callable $sessionAllow Are sessions allowed? Typically boolean true, unless provided a callable function that returns boolean. See /wire/config.php for an example.

@property int $sessionExpireSeconds How many seconds of inactivity before session expires?

@property bool $sessionChallenge Should login sessions have a challenge key? (for extra security, recommended)

@property int|bool $sessionFingerprint Should login sessions be tied to IP and user agent? 0 or false: Fingerprint off. 1 or true: Fingerprint on with default/recommended setting (currently 10). 2: Fingerprint only the remote IP. 4: Fingerprint only the forwarded/client IP (can be spoofed). 8: Fingerprint only the useragent. 10: Fingerprint the remote IP and useragent (default). 12: Fingerprint the forwarded/client IP and useragent. 14: Fingerprint the remote IP, forwarded/client IP and useragent (all).

@property int $sessionHistory Number of session entries to keep (default=0, which means off).

@property string $sessionForceIP Force the client IP address returned by $session->getIP() to be this rather than auto-detect (useful with load balancer). Use for setting value only.

@property array $loginDisabledRoles Array of role name(s) or ID(s) of roles where login is disallowed.

@property string $userAuthSalt Salt generated at install time to be used as a secondary/non-database salt for the password system.

@property string $userAuthHashType Default is 'sha1' - used only if Blowfish is not supported by the system.

@property bool $userOutputFormatting Enable output formatting for current $user API variable at boot? (default=false) @since 3.0.241

## system

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

## system-IDs

@property int $rootPageID Page ID of homepage (usually 1)

@property int $adminRootPageID Page ID of admin root page

@property int $trashPageID Page ID of the trash page.

@property int $loginPageID Page ID of the admin login page.

@property int $http404PageID Page ID of the 404 “page not found” page.

@property int $usersPageID Page ID of the page having users as children.

@property array $usersPageIDs Populated if multiple possible users page IDs (parent for users pages)

@property int $rolesPageID Page ID of the page having roles as children.

@property int $permissionsPageID Page ID of the page having permissions as children.

@property int $guestUserPageID Page ID of the guest (default/not-logged-in) user.

@property int $superUserPageID Page ID of the original superuser (created during installation).

@property int $guestUserRolePageID Page ID of the guest user role (inherited by all users, not just guest).

@property int $superUserRolePageID Page ID of the superuser role.

@property int $userTemplateID Template ID of the user template.

@property array $userTemplateIDs Array of template IDs when multiple allowed for users.

@property int $roleTemplateID Template ID of the role template.

@property int $permissionTemplateID Template ID of the permission template.

@property int $externalPageID Page ID of page assigned to $page API variable when externally bootstrapped

@property array $preloadPageIDs Page IDs of pages that will always be preloaded at beginning of request

## template-files

@property string $templateExtension Default is 'php'

@property array $contentTypes Array of extensions and the associated MIME type for each (for template file output).

@property string $prependTemplateFile PHP file in /site/templates/ that will be loaded before each page's template file (default=none)

@property string $appendTemplateFile PHP file in /site/templates/ that will be loaded after each page's template file (default=none)

@property bool $templateCompile Allow use of compiled templates?

@property string $ignoreTemplateFileRegex Regular expression to ignore template files

## URLs

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

## debugVerbose

Constant for verbose debug mode (uses more memory)

## debugDev

Constant for core development debug mode (makes it use newer JS libraries in some cases)

## url()

Get URL for requested resource or module

`$config->url('something')` is a shorter alternative for `$config->urls->get('something')`.

~~~~~
// Get the admin URL
$url = $config->url('admin');

// Same thing, using alternate syntax
$url = $config->urls->admin;
~~~~~


@param string|Wire $for Predefined ProcessWire URLs property or module name

@return string|null

## urls()

Get URL for requested resource or module or get all URLs if no argument


@param string|Wire $for Predefined ProcessWire URLs property or module name

@return null|string|Paths

@since 3.0.130

## setLocation()

Given a directory to a named location, updates $config->paths and $config->urls for it

- Paths relative to PW installation root should omit the leading slash, i.e. use `site/templates/` and NOT `/site/templates/`.

- If specifying just the `$dir` argument, it updates both `$config->paths` and `$config->urls` for it.

- If specifying both `$dir` and `$url` arguments, then `$dir` refers to `$config->paths` and `$url` refers to `$config->urls`.

- The `$for` argument can be: `cache`, `logs`, `files`, `tmp`, `templates`, or one of your own. Other named locations may
  also work, but since they can potentially be used before PW’s “ready” state, they may not be reliable.

- **Warning:** anything that changes a system URL may make the URL no longer have the protection of the root .htaccess file.
  As a result, if you modify system URLs for anything on a live server, you should also update your .htaccess file to
  reflect your changes (while leaving existing rules for original URL in place).

The following example would be in /site/init.php or /site/ready.php (or equivalent module method). In this example we
are changing the location (path and URL) of our /site/templates/ to use a new version of the files in /site/dev-templates/
so that we can test them out with user 'karen', while all other users on the site get our regular templates.
~~~~~
// change templates path and URL to /site/dev-templates/ when user name is 'karen'
if($user->name == 'karen') {
  $config->setLocation('templates', 'site/dev-templates/');
}
~~~~~


@param string $for Named location from `$config->paths` or `$config->urls`, one of: `cache`, `logs`, `files`, `tmp`, `templates`, or your own.

@param string $dir Directory or URL to the location. Should be either a path or URL relative to current installation root (recommended),
  or an absolute disk path that resolves somewhere in current installation root. If specifying an absolute path outside of the installation
  root, then you’ll also want to provide the $url argument since PW won’t know it. You may also specify a blank string for this argument
  if you only want to set the $url argument.

@param string|bool $url If the $dir argument represents both the path and URL relative to site root, you can omit this argument.
  If path and URL cannot be derived from one another, or you only want to modify the $url (leaving $dir blank), you
  can specify the URL in this argument. Specify boolean false if you only want to set the $dir (path) and not detect the $url from it.

@return self

@throws WireException If request cannot be accommodated

@since 3.0.141

## setPath()

Change or set just the server disk path for the named location (leaving URL as-is)

- If you want to update both disk path and URL at the same time, or if URL and path are going to be the same relative to
  installation root, use the `setLocation()` method instead.

- Paths relative to PW installation root should omit the leading slash, i.e. use `site/templates/` and NOT `/site/templates/`.

- The `$for` argument can be: `cache`, `logs`, `files`, `tmp`, `templates`, or one of your own. Other named locations may
  also work, but since they can potentially be used before PW’s “ready” state, they may not be reliable.


@param string $for Named location from `$config->paths`, one of: `cache`, `logs`, `files`, `tmp`, `templates`, or your own.

@param string $path Path relative to PW installation root (no leading slash), or absolute path if not.

@return self

@throws WireException

@since 3.0.141

## setUrl()

Change or set just the URL for the named location (leaving server disk path as-is)

- If you want to update both disk path and URL at the same time, or if URL and path are going to be the same relative to
  installation root, use the `setLocation()` method instead.

- Paths relative to PW installation root should omit the leading slash, i.e. use `site/templates/` and NOT `/site/templates/`.

- The `$for` argument can be: `cache`, `logs`, `files`, `tmp`, `templates`, or one of your own. Other named locations may
  also work, but since they can potentially be used before PW’s “ready” state, they may not be reliable.

- **Warning:** anything that changes a system URL may make the URL no longer have the protection of the root .htaccess file.
  As a result, if you modify system URLs for anything on a live server, you should also update your .htaccess file to
  reflect your changes (while leaving existing rules for original URL in place).

The following examples would go in /site/ready.php.

Let’s say we created a symbolic link in our web root `/tiedostot/` (Finnish for “files”) that points to /site/assets/files/.
We want all of our file URLs to appear as “/tiedostot/1234/img.jpg” rather than “/site/assets/files/1234/img.jpg”. We would
change the URL for ProcessWire’s `$config->urls->files` to point there like this example below. (Please also see warning above)
~~~~~
if($page->template != 'admin') {
  $config->setUrl('files', 'tiedostot/');
}
~~~~~
In this next example, we are changing all of our file URLs on the front-end to point a cookieless subdomain that maps all
requests to the root path of https://files.domain.com to /site/assets/files/. The example works for CDNs as well.
~~~~~
if($page->template != 'admin) {
  $config->setUrl('files', 'https://files.domain.com/');
}
~~~~~


@param string $for Named location from `$config->urls`, one of: `cache`, `logs`, `files`, `tmp`, `templates`, or your own.

@param string $url URL relative to PW installation root (no leading slash) or absolute URL if not (optionally including scheme and domain).

@return self

@throws WireException

@since 3.0.141

## path()

Get disk path for requested resource or module

`$config->path('something')` is a shorter alternative for `$config->paths->get('something')`.

~~~~~
// Get the PW installation root disk path
$path = $config->path('root');

// Same thing, using alternate syntax
$path = $config->paths->root;
~~~~~


@param string $for Predefined ProcessWire paths property or module class name

@return null|string

## paths()

Get disk path for requested resource or module or get all paths if no argument


@param string $for Predefined ProcessWire paths property or module name

@return null|string|Paths

@since 3.0.130

## js()

Set or retrieve a config value to be shared with javascript

Values are set to the Javascript variable `ProcessWire.config[key]`.

Note: In ProcessWire 3.0.173+ when setting new values, it is preferable to use
$config->jsConfig() instead, unless your intended use is to share an
existing $config property with JS.

1. Specify a $key and $value to set a JS config value.

2. Specify only a $key and omit the $value in order to retrieve an existing set value.
   The $key may also be an array of properties, which will return an array of values.

3. Specify boolean true for $value to share the $key with the JS side. If the $key
   specified does not exist then $key=true will be added to the JS config (which can later
   be overwritten with another value, which will still be shared with the JS config).
   The $key property may also be an array of properties to specify multiple.

4. Specify no params to retrieve in array of all existing set values.

~~~~~
// Set a property from PHP
$config->js('mySettings', [
  'foo' => 'bar',
  'bar' => 123,
]);

// Get a property (from PHP)
$mySettings = $config->js('mySettings');
~~~~~
~~~~~
// Get a property (from Javascript):
var mySettings = ProcessWire.config.mySettings;
console.log(mySettings.foo);
console.log(mySettings.bar);
~~~~~


@param string|array $key Property or array of properties

@param mixed $value

@return array|mixed|null|$this

## jsConfig()

Set or retrieve a config value exclusive to Javascript (ProcessWire.config)

Values are set to the Javascript variable `ProcessWire.config[key]`.

Unlike $config->js(), values get or set are exclusive to JS config only.

Values set with this method can be retrieved via $config->js() or $config->jsConfig(),
but they cannot be retrieved from $config->['key'] or $config->get('key').

If setting a new property for the JS config it is recommended that you use this
method rather than $config->js() in ProcessWire 3.0.173+. If backwards compatibility
is needed then you should still use $config->js().

1. Specify a $key and $value to set a JS config value.

2. Specify only a $key and omit the $value in order to retrieve an existing set value.

3. Specify no params to retrieve in array of all existing set values.

~~~~~
// Set a property from PHP
$config->jsConfig('mySettings', [
  'foo' => 'bar',
  'bar' => 123,
]);

// Get a property (from PHP)
$mySettings = $config->jsConfig('mySettings');
~~~~~
~~~~~
// Get a property (from Javascript):
var mySettings = ProcessWire.config.mySettings;
console.log(mySettings.foo);
console.log(mySettings.bar);
~~~~~


@param string $key Name of property to get or set or omit to return all data

@param mixed|null $value Specify value to set or omit (null) to get

@return mixed|null|array|self Returns null if $key not found, value when getting, self when setting, or array when getting all

@since 3.0.173

## phpVersion()

Return true if current PHP version is equal to or newer than the given version

~~~~~
if($config->phpVersion('7.0.0')) {
  // PHP version is 7.x
}
~~~~~


@param string|null $minVersion

@return bool

@since 3.0.101

## version()

Check if current ProcessWire version is equal to or newer than given version, or return current version

If no version argument is given, it simply returns the current ProcessWire version (3.0.130+)

~~~~~
if($config->version('3.0.100')) {
  // ProcessWire version is 3.0.100 or newer
}
~~~~~


@param string $minVersion Specify version string if you want to compare against current version

@return bool|string Returns current version if no argument given (3.0.130+), OR boolean if given a version argument:
 - If given version is older than current, returns false.
 - If given version is equal to or newer than current, returns true.

@since 3.0.106 with no-argument behavior added in 3.0.130

## installedAfter()

Was this ProcessWire installation installed after a particular date?


@param int|string $date Unix timestamp or strtotime() compatible date string

@return bool

@see Config::installedBefore(), Config::installed

@since 3.0.129

## installedBefore()

Was this ProcessWire installation installed before a particular date?


@param int|string $date Unix timestamp or strtotime() compatible date string

@return bool

@see Config::installedAfter(), Config::installed

@since 3.0.129

## serverProtocol()

Get current server protocol (for example: "HTTP/1.1")

This can be accessed by property `$config->serverProtocol`


@return string

@since 3.0.166

## requestUrl()

Current unsanitized request URL

- This is an alternative to `$input->url()` that’s available prior to API ready state.
- Useful if you need to know request URL from /site/config.php or other boot file.
- Returned value does not include query string, if present.
- Returned value includes installation subdirectory, if present.

~~~~~
if($config->requestUrl() === '/products/2021/') {
  // current request URL is exactly “/products/2021/”
}
if($config->requestUrl('/products/2021/')) {
  // current request matches “/products/2021/” somewhere in URL
}
if($config->requestUrl([ 'foo', 'bar', 'baz' ])) {
  // current request has one or more of 'foo', 'bar', 'baz' in the URL
}
~~~~~


@param string|array $match Optionally return URL only if some part matches given string(s) (default='')

@param string $get Specify 'path' to get and/or match path, 'query' to get and/or match query string, or omit for URL (default='')

@return string Returns URL string or blank string if $match argument used and doesn’t match.

@since 3.0.175

## requestPath()

Current unsanitized request path (URL sans ProcessWire installation subdirectory, if present)

This excludes any subdirectories leading to ProcessWire installation root, if present.
Useful if you need to know request path from /site/config.php or other boot file.

~~~~~
if(strpos($config->requestPath(), '/processwire/') === 0) {
  // current request path starts with “/processwire/”
}
if($config->requestPath('/processwire/')) {
  // the text “/processwire/” appears somewhere in current request path
}
if($config->requestPath([ 'foo', 'bar', 'baz' ])) {
  // current request has one or more of 'foo', 'bar', 'baz' in the path
}
~~~~~


@param string|array $match Optionally return path only if some part matches given string(s) (default='')

@return string Returns path string or blank string if $match argument used and doesn’t match.

@since 3.0.175

## requestMethod()

Current request method

This is an alternative to `$input->requestMethod()` that’s available prior to API ready state.
Useful if you need to match request method from /site/config.php or other boot file.

~~~~~
if($config->requestMethod('post')) {
  // request method is POST
}
if($config->requestMethod() === 'GET') {
  // request method is GET
}
$method = $config->requestMethod([ 'POST', 'get' ]);
if($method) {
  // method is either 'POST' or 'GET'
}
~~~~~


@param string|array $match Return found method if request method equals one given (blank if not), not case sensitive (default='')

@return string Returns one of GET, POST, HEAD, PUT, DELETE, OPTIONS, PATCH, OTHER or blank string if no match

@since 3.0.175

## versionUrls()

Given array of file asset URLs return them with cache-busting version strings

URLs that aready have query strings or URLs with scheme (i.e. https://) are ignored,
except for URLs that already have a core version query string, i.e. `?v=3.0.227`
may be converted to a different version string when appropriate.

URLs that do not resolve to a physical file on the file system, relative URLs, or
URLs that are outside of ProcessWire’s web root, are only eligible to receive a
common/shared version in the URL (like the core version).

To set a different default value for the `$useVersion` argument, you can populate
the `$config->useVersionUrls` setting in your /site/config.php with the default
value you want to substitute.

~~~~~
foreach($config->versionUrls($config->styles) as $url) {
  echo "<link rel='stylesheet' href='$url' />";
}
// there is also this shortcut for the above
foreach($config->styles->urls() as $url) {
  echo "<link rel='stylesheet' href='$url' />";
}
~~~~~


@param array|FilenameArray|WireArray|\ArrayObject $urls Array of URLs to file assets such as JS/CSS files.

@param bool|null|string $useVersion What to use for the version string (`null` is default):
 - `true` (bool): Get version from filemtime.
 - `false` (bool): Never get file version, just use $config->version.
 - `null` (null): Auto-detect: use file version in debug mode or dev branch only, $config->version otherwise.
 - `foobar` (string): Specify any string to be the version to use on all URLs needing it.
`- ?foo=bar` (string): Optionally specify your own query string variable=value.
 - The default value (null) can be overridden by the `$config->useVersionUrls` setting.

@return array Array of URLs updated with version strings where needed

@since 3.0.227

## versionUrl()

Given a file asset URLs return it with cache-busting version string

URLs that aready have query strings are left alone.


@param string $url URL to a file asset (such as JS/CSS file)

@param bool|null|string $useVersion See versionUrls() method for description of this argument.

@return string URL updated with version strings where necessary

@since 3.0.227

@see Config::versionUrls()
