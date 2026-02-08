# Securing your admin

Source: https://processwire.com/docs/security/admin/

## Summary

Information about the design and purpose of the admin environment and how to protect it. Overview of securing your admin, preventing attacks, SSL certificates, tracking logins, enabling 2FA, managing page edit access and other security best practices.

## Key Points

- Information about the design and purpose of the admin environment and how to protect it. Overview of securing your admin, preventing attacks, SSL certificates, tracking logins, enabling 2FA, managing page edit access and other security best practices.
- With some CMS products, the admin environment crosses over with the front-end themed environment, and in fact may even be the same thing. In environments like that, both front-end and admin users might use the same login form and edit their profile settings (email, password, etc.) in the same location, among other things. In such environments, there is a grey area between what is admin and what is not. ProcessWire’s admin is the exact opposite of this, and there is no grey area.
- ProcessWire completely isolates the front-end from the admin environment with no crossover between the two. It is an administrative tool, exclusively for trusted users. While the front-end is for everyone else. This enables us to lock-down the security of the front-end to a greater extent than might otherwise be possible, while opening up the capabilities and power of the admin environment more than if it were shared with the front-end.

## Sections


### About the admin environment

With some CMS products, the admin environment crosses over with the front-end themed environment, and in fact may even be the same thing. In environments like that, both front-end and admin users might use the same login form and edit their profile settings (email, password, etc.) in the same location, among other things. In such environments, there is a grey area between what is admin and what is not. ProcessWire’s admin is the exact opposite of this, and there is no grey area.


### Who the admin is for and who it is not

In ProcessWire's fully isolated admin environment, it's important to understand who the admin environment is for and who it is not. The intention behind the admin is to give the user as much power and control as possible for administering and editing the website/application content. Within the admin is the power to make or break the site; an environment for trusted users only.


### Hiding your admin URL

The default ProcessWire admin URL is domain.com/processwire/. If you want to hide the location of your admin URL, you can rename it. You have the option of doing this during the installation process. You can also do it from the ProcessWire admin. Here's how:


### Preventing dictionary attacks

You'll be glad to know that your ProcessWire admin login is secured automatically from dictionary attacks by the Session Login Throttle module, which is installed by default. This module throttles repeated login attempts, preventing the same username from being attempted for login more than once in 5 seconds. Every failed login attempt increases that waiting period exponentially, making rapid-fire dictionary attacks nearly impossible.


### Install an SSL certificate and require https for your admin

Web traffic is inherently insecure and everything sent to and from the server is unencrypted. This includes any login information you use to get into your admin, as well as cookies used to maintain your session. By installing an SSL certificate, you drastically reduce the potential for this information to be intercepted over the network by 3rd parties. As a result, installing an SSL certificate is one of the best security upgrades you can make for your site.


### Keep track of logins

A good security practice is to keep track of who is using the ProcessWire admin. It can be helpful to keep track of both successful and failed logins, and may serve as an early warning when someone is snooping around. You can access the built-in session log via Setup > Logs > session.


### Don't install the “forgot password” module unless you need it

ProcessWire comes with a module called Process Forgot Password, which can be installed in your admin under Modules > Core > Process > Forgot Password. This can be very handy for many installations. But if it's something that your installation doesn't need, then don't install it.


### Choose strong passwords

This goes without saying, but regardless of how well your admin URL is hidden, you should make sure you (and any other ProcessWire user accounts) have good passwords that aren't used elsewhere. You can enforce password strength settings from the "pass" field settings, editable in the admin from Fields > Show System Fields > Edit ("pass" field).
