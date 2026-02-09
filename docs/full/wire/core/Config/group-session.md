# Config: session

Source: `wire/core/Config.php`

- `$sessionName: string` Default session name to use (default='wire')
- `$sessionNameSecure: string` Session name when on HTTPS. Used when the sessionCookieSecure option is enabled (default). When blank (default), it will assume sessionName + 's'.
- `$sessionCookieSecure: bool|int` Use secure cookies when on HTTPS? When enabled, separate sessions will be maintained for HTTP vs. HTTPS. Good for security but tradeoff is login session may be lost when switching (default=1 or true).
- `$sessionCookieDomain: null|string` Domain to use for sessions, which enables a session to work across subdomains, or NULL to disable (default/recommended).
- `$sessionCookieSameSite: string` Cookie “SameSite” value for sessions - “Lax” (default) or “Strict”. @since 3.0.178
- `$sessionAllow: bool|callable` Are sessions allowed? Typically boolean true, unless provided a callable function that returns boolean. See /wire/config.php for an example.
- `$sessionExpireSeconds: int` How many seconds of inactivity before session expires?
- `$sessionChallenge: bool` Should login sessions have a challenge key? (for extra security, recommended)
- `$sessionFingerprint: int|bool` Should login sessions be tied to IP and user agent? 0 or false: Fingerprint off. 1 or true: Fingerprint on with default/recommended setting (currently 10). 2: Fingerprint only the remote IP. 4: Fingerprint only the forwarded/client IP (can be spoofed). 8: Fingerprint only the useragent. 10: Fingerprint the remote IP and useragent (default). 12: Fingerprint the forwarded/client IP and useragent. 14: Fingerprint the remote IP, forwarded/client IP and useragent (all).
- `$sessionHistory: int` Number of session entries to keep (default=0, which means off).
- `$sessionForceIP: string` Force the client IP address returned by $session->getIP() to be this rather than auto-detect (useful with load balancer). Use for setting value only.
- `$loginDisabledRoles: array` Array of role name(s) or ID(s) of roles where login is disallowed.
- `$userAuthSalt: string` Salt generated at install time to be used as a secondary/non-database salt for the password system.
- `$userAuthHashType: string` Default is 'sha1' - used only if Blowfish is not supported by the system.
- `$userOutputFormatting: bool` Enable output formatting for current $user API variable at boot? (default=false) @since 3.0.241
