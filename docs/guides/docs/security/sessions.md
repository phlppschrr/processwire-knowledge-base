# Database-driven sessions

Source: https://processwire.com/docs/security/sessions/

## Summary

Database-driven sessions offer potentially better security since the session information is not stored on the file system.

## Key Points

- Database-driven sessions offer potentially better security since the session information is not stored on the file system.
- ProcessWire comes with the option to use database-driven sessions, but it is not turned on by default. However, in a shared environment, database-driven sessions offer potentially better security since the session information is not stored on the file system.
- To enable database-driven sessions, login to your admin and go to Modules > Core > Session > Session Handler Database. Click the Install button. Database-driven sessions will be enabled immediately, which means you are immediately logged out. Simply log back in, and your system is now using database-driven sessions.
