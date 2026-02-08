# ProcessWire security: securing your admin control panel

Source: https://processwire.com/docs/security/admin/

## Summary

Information about the design and purpose of the admin environment and how to protect it. Overview of securing your admin, preventing attacks, SSL certificates, tracking logins, enabling 2FA, managing page edit access and other security best practices.

## Key Points

- Login to your ProcessWire admin. In the page tree, click and edit the *Admin* page.
- Click the *Settings* tab and change the *Name* field to something different. After changing it, save.
- You will get a 404 error–this is normal, because your admin no longer lives at the previous URL.
- In your browser address bar, enter your new admin URL and you are good to go.

## Sections


## Securing your admin

Information about the design and purpose of the admin environment and how to protect it. Overview of securing your admin, preventing attacks, SSL certificates, tracking logins, enabling 2FA, managing page edit access and other security best practices.


### About the admin environment

With some CMS products, the admin environment crosses over with the front-end themed environment, and in fact may even be the same thing. In environments like that, both front-end and admin users might use the same login form and edit their profile settings (email, password, etc.) in the same location, among other things. In such environments, there is a grey area between what is admin and what is not. ProcessWire’s admin is the exact opposite of this, and there is no grey area.

ProcessWire completely isolates the front-end from the admin environment with no crossover between the two. It is an administrative tool, exclusively for trusted users. While the front-end is for everyone else. This enables us to lock-down the security of the front-end to a greater extent than might otherwise be possible, while opening up the capabilities and power of the admin environment more than if it were shared with the front-end.

Using an isolated admin also promotes greater long term content portability for the site, as content administrators remain focused on long term semantics over short term style. This ensures that when the front-end is redesigned, the underlying content remains semantic enough to work within any design.

To reinforce ProcessWire as a trusted-user only environment, a user must have (at minimum) page-edit permission in one of their assigned roles (whether assigned to any templates or not). Otherwise the user will not be able to use the admin environment. The intention here is to prevent developers from utilizing the admin as a front-end environment, ensuring the integrity of the separation between isolated admin and front-end is maintained.


### Who the admin is for and who it is not

In ProcessWire's fully isolated admin environment, it's important to understand who the admin environment is for and who it is not. The intention behind the admin is to give the user as much power and control as possible for administering and editing the website/application content. Within the admin is the power to make or break the site; an environment for trusted users only.

Trusted users are individuals that you trust with the content and operation of your website/application; Users that you trust to use correct terminology and spelling in content; Users that you trust to maintain security best practices and strong, secure passwords that are kept confidential; Users you trust not to deface, compromise, insert/upload offensive or illegal content, or even experiment with doing any of these things. Such trusted users might include your web developers, administrators and highly trusted editors of the site and its content. You should have an understanding and trust that users you assign access to are not there to even experiment with harmful actions to the site. The ProcessWire admin is designed for these trusted users only, and not for any others.

Superusers and other users with the ability to edit and/or publish site content should be trusted in the same way you would trust someone to compose an email for you, and in the same way you would trust someone with ftp access to the site. While the access is certainly not the same (no they can't compose your email and they don't have ftp access), the level of trust should be the same. If it is not, then you should maintain a workflow and approval process between the source of the content and the trusted user that posts the content.

With an understanding of the power and scope of the admin environment, you'll want to protect it in several ways, which we'll discuss below.


### Hiding your admin URL

The default ProcessWire admin URL is domain.com/processwire/. If you want to hide the location of your admin URL, you can rename it. You have the option of doing this during the installation process. You can also do it from the ProcessWire admin. Here's how:

- Login to your ProcessWire admin. In the page tree, click and edit the *Admin* page.
- Click the *Settings* tab and change the *Name* field to something different. After changing it, save.
- You will get a 404 error–this is normal, because your admin no longer lives at the previous URL.
- In your browser address bar, enter your new admin URL and you are good to go.


### Preventing dictionary attacks

You'll be glad to know that your ProcessWire admin login is secured automatically from dictionary attacks by the *Session Login Throttle* module, which is installed by default. This module throttles repeated login attempts, preventing the same username from being attempted for login more than once in 5 seconds. Every failed login attempt increases that waiting period exponentially, making rapid-fire dictionary attacks nearly impossible.

You can further lock down the settings of this module by configuring it (in Modules > Core > Session > Login Throttle). If your admin doesn't have simultaneous users coming from the same shared IP address, we recommend checking the box to enable throttling by IP address. When checked, not only will attempts for the same username be throttled, but any attempts (regardless of username) will be throttled by IP address as well.

The only reason that we don't have this "throttle by IP" box checked by default is because some clients have multiple users coming from the same IP address. In that instance, one person forgetting their password could temporarily prevent other people from logging in.


### Install an SSL certificate and require https for your admin

Web traffic is inherently insecure and everything sent to and from the server is unencrypted. This includes any login information you use to get into your admin, as well as cookies used to maintain your session. By installing an SSL certificate, you drastically reduce the potential for this information to be intercepted over the network by 3rd parties. As a result, installing an SSL certificate is one of the best security upgrades you can make for your site.

Once you've got an SSL certificate installed on your server, you need to make sure that it is put to use. At minimum, we recommend locking down your "admin" template to only allow https traffic. However, make sure that your site is accessible via https://yourdomain.com before you do this, otherwise you could lock yourself out of the admin.

Once confirmed that your site is accessible via https, login to your admin (using the https URL), and do the following:

- Click "Setup" then "Templates" (click the Templates label rather than a specific template).
- Click the "Filters" box, then "Show system templates", and choose "Yes".
- When the page reloads, you'll have a "System" section where you will see an "admin" template. Click "admin".
- Click the "URLs" tab and scroll to the "Scheme/Protocol" section. Click "HTTPS only" and Save.


### Keep track of logins

A good security practice is to keep track of who is using the ProcessWire admin. It can be helpful to keep track of both successful and failed logins, and may serve as an early warning when someone is snooping around. You can access the built-in session log via Setup > Logs > session.

If you'd like more information or options than what the default session log includes, take a look at the [Login Notifier](http://modules.processwire.com/modules/login-notifier/) module by Ryan Cramer or the [Login History module](http://modules.processwire.com/modules/process-login-history/) by Teppo Koivula.


### Don't install the “forgot password” module unless you need it

ProcessWire comes with a module called *Process Forgot Password*, which can be installed in your admin under Modules > Core > Process > Forgot Password. This can be very handy for many installations. But if it's something that your installation doesn't need, then don't install it.

While we've gone to great efforts to ensure our forgot password module is secure (and in fact, more secure than any other we've seen), it still involves emailing the user a time-limited link to reset their password. As you may already know, email is not the safest way to transport confidential information, so limiting what can happen with email [when you can] is worthwhile.

It's worth noting that ProcessWire's forgot password function only works if the session that requested the reset is the same session that clicks the email link and performs the reset. That provides an additional layer of security over other password reset functions that we've seen. But if your email account is compromised, then all bets are off: your ProcessWire password then has the potential to be compromised as well. So if your site doesn't absolutely need a forgot password function, then don't install it.


### Choose strong passwords

This goes without saying, but regardless of how well your admin URL is hidden, you should make sure you (and any other ProcessWire user accounts) have good passwords that aren't used elsewhere. You can enforce password strength settings from the "pass" field settings, editable in the admin from Fields > Show System Fields > Edit ("pass" field).


### Install 2-factor (or multi-factor) authentication

ProcessWire supports 2-factor authentication (2FA/TFA/MFA) natively and can be used with applications like Authy, Google Authenticator, Microsoft Authenticator, LastPass and others supporting TOTP (time-based one-time protocol).

To start using it, you'll want to install the 1st party [TfaTotp](http://modules.processwire.com/modules/tfa-totp/) module. You may also want to install the [TfaEmail](https://modules.processwire.com/modules/tfa-email/) module as a 2nd option, which may not be as secure as TOTP, but can be an easier path for some users, and enables you to enforce 2-factor authentication automatically. Other Tfa module options may also be available in the modules directory [Tfa page](https://modules.processwire.com/categories/tfa/). Once one or more Tfa modules are installed, you can enable them to be used in admin by configuring the ProcessLogin module settings (Modules > Configure > ProcessLogin).

[See this page for more details on two-factor authentication in ProcessWire](/docs/security/two-factor-authentication/)


### Managing the security of page edit access in the admin

The primary purpose of ProcessWire’s admin is to manage the pages of the site or application, along with other resources that support them (templates, fields, modules, etc.).

You can control which trusted users can edit which pages, assignable per-role and by-template. When using access control settings to manage page-edit access, you should limit access to edit system pages (which include homepage, 404 page, and everything within the admin page structure) to superusers only; as well as search, sitemap or other types of single-purpose pages you might be using in your site (if you are using them). Superusers can already edit everything, so you can achieve this by simply not assigning any edit access to these system pages at all.

**Assign edit access to specific content types rather than general purpose ones** When possible, page edit access should be assigned to templates representing specific content types rather than general purpose ones. For example, if you have a user that you only want to edit your terms-and-conditions page, then make sure that terms-and-conditions page is using its own template (rather than a "basic-page") one, so that you can assign edit access to just that page. When your system is using a "basic-page" type template (whether named that or not) do not use it for assigning page-edit access control, since it may be used by many general purpose pages. When you need to assign edit access to pages using such template(s), clone the template to a new one, set the page to use it, and assign the necessary edit access to the new template.

**Do not assign edit permissions on the homepage template** The home (homepage) template is access controlled already, and other non-access controlled pages below it inherit access settings from it. This is very useful when it comes to view permission (which is required here), so it may be tempting to use it as a quick solution to assign site-wide edit access. But you should avoid this temptation, do not assign roles edit permission to the home template. Why not? First off, if we want to stick to best practices, superuser should be the only role with site-wide edit access. Secondly, edit access assigned at the homepage inherits down through the tree in a way that can be ambiguous. Instead, create roles with specific purposes that can edit specific content types (templates), and assign as many roles as you need to a particular user, consistent with their edit needs. Non-superusers should not be able to directly edit the root (home) page in the site. If you have a user that needs to edit homepage content, the homepage should pull content from other pages using templates that you assign access to separately.

**Field-level access control** After taking the standard template-level access control into account, consider that ProcessWire also supports field-level access control. This can be useful for controlling access to pages where you want the user to be able to edit some parts of it and not others.

**Balancing complexity** Be careful not to over-complicate your access control settings beyond your security needs. ProcessWire will let you create very powerful and complex access control scenarios in your admin, but that doesn't mean that you should. Increasing complexity can also reduce security, as the who/what/where of access control becomes more difficult to keep track of. For this reason, only introduce fine granular access control settings (such as field-level access control) into your installation in cases where you need it, and where it adds additional clarity or simplicity to the overall access control setup. Find the right balance that maximizes security while limiting complexity.
