# Running ProcessWire alongside other software

Source: https://processwire.com/docs/security/other-software/

## Summary

ProcessWire will happily run alongside almost any other PHP application, including other CMSs. However, security on your site will only be as good as the weakest link.The more applications running on the same account, the greater the potential security issues. This is particularly a concern when running ProcessWire alongside a highly targeted CMS like WordPress, which we will use only here as an example. If your WordPress blog gets hacked, there's a chance your ProcessWire installation will also be compromised since they exist on the same account and file system.You can avoid this potential issue by jailing applications from one another via separate accounts and/or subdomains. Specifically, this means that one account/subdomain does not have write access to the others.As an example, lets say your ProcessWire installation runs at domain.com and your WordPress blog runs at domain.com/blog/. It would be preferable for your blog to live at blog.domain.com, on an account jailed from the ProcessWire installation. That way, when your WordPress blog gets hacked, the damage is limited to the blog and not your entire site.

## Key Points

- ProcessWire will happily run alongside almost any other PHP application, including other CMSs. However, security on your site will only be as good as the weakest link.The more applications running on the same account, the greater the potential security issues. This is particularly a concern when running ProcessWire alongside a highly targeted CMS like WordPress, which we will use only here as an example. If your WordPress blog gets hacked, there's a chance your ProcessWire installation will also be compromised since they exist on the same account and file system.You can avoid this potential issue by jailing applications from one another via separate accounts and/or subdomains. Specifically, this means that one account/subdomain does not have write access to the others.As an example, lets say your ProcessWire installation runs at domain.com and your WordPress blog runs at domain.com/blog/. It would be preferable for your blog to live at blog.domain.com, on an account jailed from the ProcessWire installation. That way, when your WordPress blog gets hacked, the damage is limited to the blog and not your entire site.

## Sections


## Running ProcessWire alongside other software

ProcessWire will happily run alongside almost any other PHP application, including other CMSs. However, security on your site will only be as good as the weakest link.The more applications running on the same account, the greater the potential security issues. This is particularly a concern when running ProcessWire alongside a highly targeted CMS like WordPress, which we will use only here as an example. If your WordPress blog gets hacked, there's a chance your ProcessWire installation will also be compromised since they exist on the same account and file system.You can avoid this potential issue by jailing applications from one another via separate accounts and/or subdomains. Specifically, this means that one account/subdomain does not have write access to the others.As an example, lets say your ProcessWire installation runs at domain.com and your WordPress blog runs at domain.com/blog/. It would be preferable for your blog to live at blog.domain.com, on an account jailed from the ProcessWire installation. That way, when your WordPress blog gets hacked, the damage is limited to the blog and not your entire site.
