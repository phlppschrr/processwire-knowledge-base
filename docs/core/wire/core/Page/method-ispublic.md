# Page::isPublic()

Source: `wire/core/Page.php`

Is this page public and viewable by all?

This is a state that persists regardless of user, so has nothing to do with the current user.
To be public, the page must be published and have guest view access.


@return bool True if public, false if not
