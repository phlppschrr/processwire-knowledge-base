# ProcessWire

Source: `wire/core/ProcessWire.php`

ProcessWire API Bootstrap

Represents an instance of ProcessWire connected with a set of API variables.
Methods for managing ProcessWire instances. Note that most of these methods are static.
This class boots a ProcessWire instance. The current ProcessWire instance is represented by the `$wire` API variable.
~~~~~
// To create a new ProcessWire instance
$wire = new ProcessWire('/server/path/', 'https://hostname/url/');
~~~~~

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

Default API vars (A-Z)
======================

@property AdminTheme|AdminThemeFramework|null $adminTheme

@property WireCache $cache

@property WireClassLoader $classLoader

@property Config $config

@property WireDatabasePDO $database

@property WireDateTime $datetime

@property Fieldgroups $fieldgroups

@property Fields $fields

@property Fieldtypes $fieldtypes

@property WireFileTools $files

@property Fuel $fuel

@property WireHooks $hooks

@property WireInput $input

@property Languages $languages (present only if LanguageSupport installed)

@property WireLog $log

@property WireMailTools $mail

@property Modules $modules

@property Notices $notices

@property Page $page

@property Pages $pages

@property Permissions $permissions

@property Process|ProcessPageView $process

@property WireProfilerInterface $profiler

@property Roles $roles

@property Sanitizer $sanitizer

@property Session $session

@property Templates $templates

@property Paths $urls

@property User $user

@property Users $users

@property ProcessWire $wire

@property WireShutdown $shutdown

@property PagesVersions|null $pagesVersions

@method init()

@method ready()

@method finished(array $data)

## versionMajor

Major version number

## versionMinor

Minor version number

## versionRevision

Reversion revision number

## versionSuffix

Version suffix string (when applicable)

## indexVersion

Minimum required index.php version, represented by the PROCESSWIRE define

## htaccessVersion

Minimum required .htaccess file version

## statusNone

Status prior to boot (no API variables available)

## statusBoot

Status when system is booting

API variables available: $wire, $hooks, $config, $classLoader

## statusInit

Status when system and modules are initializing

All API variables available except for $page

## statusReady

Status when system, $page and all API variables are ready

All API variables available

## statusRender

Status when the current $page’s template file is being rendered, set right before render

All API variables available

## statusDownload

Status when current request will send a file download to client and exit (rather than rendering a page template file)

All API variables available

## statusFinished

Status when the request has been fully delivered (but before a redirect)

All API variables available

## statusExited

Status when the request has finished abnormally (like a manual exit)

@since 3.0.180

## statusFailed

Status when the request failed due to an Exception or 404

API variables should be checked for availability before using.

## __construct()

Create a new ProcessWire instance

~~~~~
// A. Current directory assumed to be root of installation
$wire = new ProcessWire();

// B: Specify a Config object as returned by ProcessWire::buildConfig()
$wire = new ProcessWire($config);

// C: Specify where installation root is
$wire = new ProcessWire('/server/path/');

// D: Specify installation root path and URL
$wire = new ProcessWire('/server/path/', '/url/');

// E: Specify installation root path, scheme, hostname, URL
$wire = new ProcessWire('/server/path/', 'https://hostname/url/');
~~~~~

@param Config|string|null $config May be any of the following:
 - A Config object as returned from ProcessWire::buildConfig().
 - A string path to PW installation.
 - You may optionally omit this argument if current dir is root of PW installation.

@param string $rootURL URL or scheme+host to installation.
 - This is only used if $config is omitted or a path string.
 - May also include scheme & hostname, i.e. "http://hostname.com/url" to force use of scheme+host.
 - If omitted, it is determined automatically.

@throws WireException if given invalid arguments

## __destruct()

Destruct

## setConfig()

Populate ProcessWire's configuration with runtime and optional variables

@param Config $config

## setConfigDebug()

Determine whether debug mode should be enabled

@param Config $config

@return bool|int Returns determined debug mode value

@since 3.0.212

## getHttpHost()

Safely determine the HTTP host

@param Config $config

@return string

## initVar()

Initialize the given API var

@param string $name

@param Fieldtypes|Fields|Fieldgroups|Templates|Pages|Session $value

## setStatus()

Set the system status to one of the ProcessWire::status* constants

This also triggers init/ready functions for modules, when applicable.

@param int $status

@param array $data Associative array of any extra data to pass along to include files as locally scoped vars (3.0.142+)

## ___init()

Hookable init for anyone that wants to hook immediately before any autoload modules initialized or after all modules initialized

## ___ready()

Hookable ready for anyone that wants to hook immediately before any autoload modules ready or after all modules ready

## ___finished()

Hookable ready for anyone that wants to hook when the request is finished

@param array $data Additional data for hooks (3.0.147+ only):
 - `maintenance` (bool): Allow maintenance to run? (default=true)
 - `prevStatus` (int): Previous status before finished status (render, download or failed).
 - `exited` (bool): True if request was exited before finished (ProcessWire instance destructed before expected). 3.0.180+
 - `redirectUrl` (string): Contains redirect URL only if request ending with redirect (not present otherwise).
 - `redirectType` (int): Contains redirect type 301 or 302, only if requestUrl property is also present.

## set()

Set a new API variable

Alias of $this->wire(), but for setting only, for syntactic convenience.
i.e. $this->wire()->set($key, $value);

@param string $key API variable name to set

@param Wire|mixed $value Value of API variable

@param bool $lock Whether to lock the value from being overwritten

@return $this

## __get()

Get API var directly

@param string $name

@return mixed

## includeFile()

Include a PHP file, giving it all PW API varibles in scope

File is executed in the directory where it exists.

@param string $file Full path and filename

@param array $data Associative array of any extra data to pass along to include file as locally scoped vars

@return bool True if file existed and was included, false if not.

## __call()

Call method

@param string $method

@param array $arguments

@return mixed

@throws WireException

## getProcessWireInstanceID()

Instance ID of this ProcessWire instance


@return int

## addInstance()

Add a ProcessWire instance and return the instance ID


@param ProcessWire $wire

@return int

## getInstances()

Get all ProcessWire instances


@return array

## getNumInstances()

Return number of instances


@return int

## getInstance()

Get a ProcessWire instance by ID


@param int|null $instanceID Omit this argument to return the current instance

@return null|ProcessWire

## getCurrentInstance()

Get the current ProcessWire instance


@return ProcessWire|null

## setCurrentInstance()

Set the current ProcessWire instance


@param ProcessWire $wire

## removeInstance()

Remove a ProcessWire instance


@param ProcessWire $wire

## getRootPath()

Get root path, check it, and optionally auto-detect it if not provided

@param bool|string $rootPath Root path if already known, in which case we’ll just modify as needed
  …or specify boolean true to get absolute root path, which disregards any symbolic links to core.

@return string

## buildConfig()

Static method to build a Config object for booting ProcessWire

@param string $rootPath Path to root of installation where ProcessWire's index.php file is located.

@param string $rootURL Should be specified only for secondary ProcessWire instances.
  May also include scheme & hostname, i.e. "http://hostname.com/url" to force use of scheme+host.

@param array $options Options to modify default behaviors (experimental):
 - `siteDir` (string): Name of "site" directory in $rootPath that contains site's config.php, no slashes (default="site").

@return Config
