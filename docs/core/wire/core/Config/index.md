# Config

Source: `wire/core/Config.php`

Inherits: `WireData`


Groups:
Group: [admin](group-admin.md)
Group: [database](group-database.md)
Group: [date-time](group-date-time.md)
Group: [files](group-files.md)
Group: [HTTP-and-input](group-http-and-input.md)
Group: [images](group-images.md)
Group: [modules](group-modules.md)
Group: [other](group-other.md)
Group: [paths](group-paths.md)
Group: [runtime](group-runtime.md)
Group: [session](group-session.md)
Group: [system](group-system.md)
Group: [system-IDs](group-system-ids.md)
Group: [template-files](group-template-files.md)
Group: [URLs](group-urls.md)

ProcessWire Config

Handles ProcessWire configuration data

This file is licensed under the MIT license
https://processwire.com/about/license/mit/


Holds ProcessWire configuration settings as defined in /wire/config.php and /site/config.php.
For more detailed descriptions of these $config properties, including default values, see the
[/wire/config.php](https://github.com/processwire/processwire/blob/master/wire/config.php) file.


@see /wire/config.php for more detailed descriptions of all config properties.

Methods:
- [`url(string|Wire $for): string|null`](method-url.md) Get URL for requested resource or module
- [`urls(string|Wire $for = ''): null|string|Paths`](method-urls.md) Get URL for requested resource or module or get all URLs if no argument
- [`setLocation(string $for, string $dir, string|bool $url = ''): self`](method-setlocation.md) Given a directory to a named location, updates $config->paths and $config->urls for it
- [`setPath(string $for, string $path): self`](method-setpath.md) Change or set just the server disk path for the named location (leaving URL as-is)
- [`setUrl(string $for, string $url): self`](method-seturl.md) Change or set just the URL for the named location (leaving server disk path as-is)
- [`path(string $for): null|string`](method-path.md) Get disk path for requested resource or module
- [`paths(string $for = ''): null|string|Paths`](method-paths.md) Get disk path for requested resource or module or get all paths if no argument
- [`js(string|array $key = null, mixed $value = null): array|mixed|null|$this`](method-js.md) Set or retrieve a config value to be shared with javascript
- [`jsConfig(string $key = null, mixed|null $value = null): mixed|null|array|self`](method-jsconfig.md) Set or retrieve a config value exclusive to Javascript (ProcessWire.config)
- [`phpVersion(string|null $minVersion): bool`](method-phpversion.md) Return true if current PHP version is equal to or newer than the given version
- [`version(string $minVersion = ''): bool|string`](method-version.md) Check if current ProcessWire version is equal to or newer than given version, or return current version
- [`installedAfter(int|string $date): bool`](method-installedafter.md) Was this ProcessWire installation installed after a particular date?
- [`installedBefore(int|string $date): bool`](method-installedbefore.md) Was this ProcessWire installation installed before a particular date?
- [`serverProtocol(): string`](method-serverprotocol.md) Get current server protocol (for example: "HTTP/1.1")
- [`requestUrl(string|array $match = '', string $get = ''): string`](method-requesturl.md) Current unsanitized request URL
- [`requestPath(string|array $match = ''): string`](method-requestpath.md) Current unsanitized request path (URL sans ProcessWire installation subdirectory, if present)
- [`requestMethod(string|array $match = ''): string`](method-requestmethod.md) Current request method
- [`versionUrls(array|FilenameArray|WireArray|\ArrayObject $urls, bool|null|string $useVersion = null): array`](method-versionurls.md) Given array of file asset URLs return them with cache-busting version strings
- [`versionUrl(string $url, bool|null|string $useVersion = null): string`](method-versionurl.md) Given a file asset URLs return it with cache-busting version string

Constants:
- [`debugVerbose`](const-debugverbose.md)
- [`debugDev`](const-debugdev.md)
