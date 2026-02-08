# Session::hasLoginCookie()

Source: `wire/core/Session.php`

Is a session login cookie present?

This only indicates the user was likely logged in at some point, and may not indicate an active login.
This method is more self describing version of `$session->hasCookie(true);`


@return bool

@since 3.0.175
