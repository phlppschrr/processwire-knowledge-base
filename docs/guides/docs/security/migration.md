# Migrating to production

Source: https://processwire.com/docs/security/migration/

## Summary

Unless the production server is a completely dedicated environment, don't assume that what was safe on your development server will also be safe on the production server.

## Key Points

- Unless the production server is a completely dedicated environment, don't assume that what was safe on your development server will also be safe on the production server.
- The server configuration and necessary permissions between your development server and production server may be completely different. Take the time to revisit all the pages in this security section (particularly file permissions) with the context specific to your production server. In particular, pay attention to your writable file system permissions for /site/assets/, /site/modules/ and everything in them, as well as your /site/config.php file. You may need to make a recursive change to all files in that directory after migrating to production. For instance, if your production server has Apache running as your account, and your development server didn't, then you should lock down the permissions consistent with what the server supports.
