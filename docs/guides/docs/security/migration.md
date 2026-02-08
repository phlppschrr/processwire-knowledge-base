# ProcessWire security: migrating to production

Source: https://processwire.com/docs/security/migration/

# Migrating to production 

Unless the production server is a completely dedicated environment, don't assume that what was safe on your development server will also be safe on the production server.

The server configuration and necessary permissions between your development server and production server may be completely different. Take the time to revisit all the pages in this security section (particularly [file permissions](/docs/security/file-permissions/)) with the context specific to your production server. In particular, pay attention to your writable file system permissions for /site/assets/, /site/modules/ and everything in them, as well as your /site/config.php file. You may need to make a [recursive change to all files in that directory](/docs/security/file-permissions/#how-to-change-permissions-of-existing-files) after migrating to production. For instance, if your production server has Apache running as your account, and your development server didn't, then you should lock down the permissions consistent with what the server supports.
- [Potential permissions for writable files and directories](/docs/security/file-permissions/#potential-permissions-for-writable-directories-and-files)
- [How to change permissions of existing directories and files](/docs/security/file-permissions/#how-to-change-permissions-of-existing-files)
- [Securing your /site/config.php file](/docs/security/file-permissions/#securing-your-site-config.php-file)
- [Determining who Apache runs as](/docs/security/file-permissions/#determining-what-user-apache-runs-as)

You might also find it worthwhile to install a test copy of ProcessWire on your production server before migrating your site to it. The installer can identify many potential issues ahead of time, saving you the hassle of figuring things out during migration. Remember to delete the test installation afterwards.
