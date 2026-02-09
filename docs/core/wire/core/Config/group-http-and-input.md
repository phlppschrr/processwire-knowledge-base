# Config: HTTP-and-input

Source: `wire/core/Config.php`

- $httpHost: string Current HTTP host name.
- $protectCSRF: bool Enables CSRF (cross site request forgery) protection on all PW forms, recommended for security.
- $wireInputOrder: string Order that variables with the $input API var are handled when you access $input->var.
- $wireInputLazy: bool Specify true for $input API var to load input data in a lazy fashion and potentially use less memory. Default is false.
- $wireInputArrayDepth: int Maximum multi-dimensional array depth for input variables accessed from $input or 1 to only allow single dimension arrays. @since 3.0.178
- $cookieOptions: array Options for setting cookies from $input->cookie
- $httpHosts: array HTTP hosts For added security, specify the host names ProcessWire should recognize.
- $noHTTPS: bool|string|array When boolean true, pages requiring HTTPS will not enforce it (useful for dev environments). May also specify hostname (string) or hostnames (array) to disable HTTPS for.
