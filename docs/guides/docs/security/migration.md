# Unknown

Source: https://processwire.com/docs/security/migration/

Unless the production server is a completely dedicated environment, don't assume that what was safe on your development server will also be safe on the production server.

The server configuration and necessary permissions between your development server and production server may be completely different. Take the time to revisit all the pages in this security section (particularly [file permissions](/docs/security/file-permissions/)) with the context specific to your production server. In particular, pay attention to your writable file system permissions for /site/assets/, /site/modules/ and everything in them, as well as your /site/config.php file. You may need to make a [recursive change to all files in that directory](/docs/security/file-permissions/#how-to-change-permissions-of-existing-files) after migrating to production. For instance, if your production server has Apache running as your account, and your development server didn't, then you should lock down the permissions consistent with what the server supports.

- [Potential permissions for writable files and directories](/docs/security/file-permissions/#potential-permissions-for-writable-directories-and-files)
- [How to change permissions of existing directories and files](/docs/security/file-permissions/#how-to-change-permissions-of-existing-files)
- [Securing your /site/config.php file](/docs/security/file-permissions/#securing-your-site-config.php-file)
- [Determining who Apache runs as](/docs/security/file-permissions/#determining-what-user-apache-runs-as)

You might also find it worthwhile to install a test copy of ProcessWire on your production server before migrating your site to it. The installer can identify many potential issues ahead of time, saving you the hassle of figuring things out during migration. Remember to delete the test installation afterwards.

- [Security](/docs/security/)
- [Securing file permissions](/docs/security/file-permissions/)
- [Securing your admin](/docs/security/admin/)
- [Web hosting security](/docs/security/web-hosting/)
- [Migrating to production](/docs/security/migration/)
- [Remove unnecessary files](/docs/security/remove-unnecessary-files/)
- [Database-driven sessions](/docs/security/sessions/)
- [Running ProcessWire alongside other software](/docs/security/other-software/)
- [Third party modules](/docs/security/third-party-modules/)
- [Template files](/docs/security/template-files/)
- [2-factor authentication](/docs/security/two-factor-authentication/)

- [Docs](/docs/)
- [API reference](/api/ref/)
- [Getting started](/docs/start/)
- [Front-end](/docs/front-end/)
- [Tutorials](/docs/tutorials/)
- [Selectors](/docs/selectors/)
- [Modules & hooks](/docs/modules/)
- [Fields, types, input](/docs/fields/)
- [Access control](/docs/user-access/)
- [Security](/docs/security/)
- [Multi-language](/docs/multi-language-support/)
- [More topics](/docs/more/)

[Web hosting security](/docs/security/web-hosting/)[Remove unnecessary files](/docs/security/remove-unnecessary-files/)
