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
- [`url(string|Wire $for): string|null`](method-url.md)
- [`urls(string|Wire $for = ''): null|string|Paths`](method-urls.md)
- [`setLocation(string $for, string $dir, string|bool $url = ''): self`](method-setlocation.md)
- [`setPath(string $for, string $path): self`](method-setpath.md)
- [`setUrl(string $for, string $url): self`](method-seturl.md)
- [`path(string $for): null|string`](method-path.md)
- [`paths(string $for = ''): null|string|Paths`](method-paths.md)
- [`js(string|array $key = null, mixed $value = null): array|mixed|null|$this`](method-js.md)
- [`jsConfig(string $key = null, mixed|null $value = null): mixed|null|array|self`](method-jsconfig.md)
- [`phpVersion(string|null $minVersion): bool`](method-phpversion.md)
- [`version(string $minVersion = ''): bool|string`](method-version.md)
- [`installedAfter(int|string $date): bool`](method-installedafter.md)
- [`installedBefore(int|string $date): bool`](method-installedbefore.md)
- [`serverProtocol(): string`](method-serverprotocol.md)
- [`requestUrl(string|array $match = '', string $get = ''): string`](method-requesturl.md)
- [`requestPath(string|array $match = ''): string`](method-requestpath.md)
- [`requestMethod(string|array $match = ''): string`](method-requestmethod.md)
- [`versionUrls(array|FilenameArray|WireArray|\ArrayObject $urls, bool|null|string $useVersion = null): array`](method-versionurls.md)
- [`versionUrl(string $url, bool|null|string $useVersion = null): string`](method-versionurl.md)

Constants:
- [`debugVerbose`](const-debugverbose.md)
- [`debugDev`](const-debugdev.md)
