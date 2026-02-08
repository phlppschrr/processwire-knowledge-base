# $session->close()

Source: `wire/core/Session.php`

Manually close the session, before program execution is done

A user session is limited to rendering one page at a time, unless the session is closed
early. Use this when you have a request that may take awhile to render (like a request
rendering a sitemap, etc.) and you don't need to get/save session data. By closing the session
before starting a render, you can release the session to be available for the user to view
other pages while the slower page render continues.
