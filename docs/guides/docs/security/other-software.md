# Unknown

Source: https://processwire.com/docs/security/other-software/

ProcessWire will happily run alongside almost any other PHP application, including other CMSs. However, security on your site will only be as good as the weakest link.

The more applications running on the same account, the greater the potential security issues. This is particularly a concern when running ProcessWire alongside a highly targeted CMS like WordPress, which we will use only here as an example. If your WordPress blog gets hacked, there's a chance your ProcessWire installation will also be compromised since they exist on the same account and file system.

You can avoid this potential issue by jailing applications from one another via separate accounts and/or subdomains. Specifically, this means that one account/subdomain does not have write access to the others.

As an example, lets say your ProcessWire installation runs at domain.com and your WordPress blog runs at domain.com/blog/. It would be preferable for your blog to live at blog.domain.com, on an account jailed from the ProcessWire installation. That way, when your WordPress blog gets hacked, the damage is limited to the blog and not your entire site.

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

[Database-driven sessions](/docs/security/sessions/)[Third party modules](/docs/security/third-party-modules/)
