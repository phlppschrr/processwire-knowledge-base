# Config: HTTP-and-input

Source: `wire/core/Config.php`

@property string $httpHost Current HTTP host name.

@property bool $protectCSRF Enables CSRF (cross site request forgery) protection on all PW forms, recommended for security.

@property string $wireInputOrder Order that variables with the $input API var are handled when you access $input->var.

@property bool $wireInputLazy Specify true for $input API var to load input data in a lazy fashion and potentially use less memory. Default is false.

@property int $wireInputArrayDepth Maximum multi-dimensional array depth for input variables accessed from $input or 1 to only allow single dimension arrays. @since 3.0.178

@property array $cookieOptions Options for setting cookies from $input->cookie

@property array $httpHosts HTTP hosts For added security, specify the host names ProcessWire should recognize.

@property bool|string|array $noHTTPS When boolean true, pages requiring HTTPS will not enforce it (useful for dev environments). May also specify hostname (string) or hostnames (array) to disable HTTPS for.
