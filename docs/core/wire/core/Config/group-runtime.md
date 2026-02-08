# Config: runtime

Source: `wire/core/Config.php`

@property bool $ajax If the current request is an ajax (asynchronous javascript) request, this is set to true.

@property bool|int $modal If the current request is in a modal window, this is set to a positive number. False if not.

@property bool|int $admin Is current request for logged-in user in admin? True, false, or 0 if not yet known. @since 3.0.142

@property bool $https If the current request is an HTTPS request, this is set to true.

@property string $version Current ProcessWire version string (i.e. "2.2.3")

@property int $systemVersion System version, used by SystemUpdater to determine when updates must be applied.

@property FilenameArray $styles Array used by ProcessWire admin to keep track of what stylesheet files its template should load. It will be blank otherwise. Feel free to use it for the same purpose in your own sites.

@property FilenameArray $scripts Array used by ProcessWire admin to keep track of what javascript files its template should load. It will be blank otherwise. Feel free to use it for the same purpose in your own sites.

@property Paths $urls Items from $config->urls reflect the http path one would use to load a given location in the web browser. URLs retrieved from $config->urls always end with a trailing slash. This is the same as the $urls API variable.

@property Paths $paths All of what can be accessed from $config->urls can also be accessed from $config->paths, with one important difference: the returned value is the full disk path on the server. There are also a few items in $config->paths that aren't in $config->urls. All entries in $config->paths always end with a trailing slash.

@property bool $internal This is automatically set to FALSE when PW is externally bootstrapped.

@property bool $cli This is automatically set to TRUE when PW is booted as a command line (non HTTP) script.

@property string $serverProtocol Current server protocol, one of: HTTP/1.1, HTTP/1.0, HTTP/2, or HTTP/2.0. @since 3.0.166

@property string $versionName This is automatically populated with the current PW version name (i.e. 2.5.0 dev)

@property string|null $pagerHeadTags Populated at runtime to contain `<link rel=prev|next />` tags for document head, after pagination has been rendered by MarkupPagerNav module.
