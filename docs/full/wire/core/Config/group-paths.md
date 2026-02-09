# Config: paths

Source: `wire/core/Config.php`

- [$paths: Paths](method-paths.md) All of what can be accessed from $config->urls can also be accessed from $config->paths, with one important difference: the returned value is the full disk path on the server. There are also a few items in $config->paths that aren't in $config->urls. All entries in $config->paths always end with a trailing slash.
