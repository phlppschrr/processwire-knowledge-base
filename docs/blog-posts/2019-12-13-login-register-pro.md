# Login Register Pro

Source: https://processwire.com/blog/posts/login-register-pro/

## Sections


## Login Register Pro module

13 December 2019 by Ryan Cramer [ 10 Comments](/blog/posts/login-register-pro/#comments)

This week we’ll take a look at LoginRegisterPro — a new module that provides an all-in-one, self contained module for providing new user registration, secure logins, profile editing, and more. It does this all in a manner that is reliable, efficient, comprehensive and secure.

As we continue preparing the ProcessWire core dev branch to become our new master, I've been trying to stay hands-off on new feature additions there as much as possible (till the new master is out), and instead focusing on finishing up modules I've had in development. Last time I told you about the [UserActivity](/blog/posts/user-activity-module/) module, and this time we’ll look at LoginRegisterPro, which is another module dealing with users; though significantly larger in scale/scope.

LoginRegisterPro is a module I've been working on for more than a year, and finally this month have it ready to share. While I don't have it available for download today I do expect to have a beta release as soon as early next week. If you'd like, [send me a message](https://processwire.com/blog/posts/login-register-pro/#more-info) and I'll send you an email once it's ready (there's a form at the bottom of this page).


### Introduction

LoginRegisterPro takes care of giving you a well qualified/authenticated user, and you decide what to do with that user. Whether that is using ProcessWire’s access control system to control what they can see, or using the API to control what they can access or achieve, LoginRegisterPro is built to be a very solid foundation for sites and applications working with front-end users.


### Background

LoginRegisterPro is a re-imagining of a module called [LoginRegister](/blog/posts/pw-3.0.76-plus-login-register/) that I built a few years ago for a client with very specific needs. At the client’s suggestion, it was released open source as a starting point or proof-of-concept for those looking to implement login, registration and front-end user profile editing capabilities. Despite being fairly limited in scope and purpose, there was a lot of interest in that module. Since that time, I've received numerous requests to build a Pro version of the module with more enterprise-level features and security, and with commercial support. LoginRegisterPro is the result.

While this module does still share some ideas in common with the original LoginRegister module, it is actually a full rewrite that attempts to cover most of the features that were requested, and with a much stronger foundation. In addition, because this module opens a lot of new possibilities, and everyone has slightly different needs, I wanted to be able to provide the proper level of long-term support that is available with the other Pro modules.

Even without this module, ProcessWire provides a great foundation for building your own front-end user system. I've built several for client projects over the years (as others have too). But they are always expensive and time consuming to build, and there's never been the budget or time to build an enterprise-level set of features. LoginRegisterPro handles all of that, saving you (and your clients) a lot of time and expense, while delivering a level of features, quality, consistency, ease-of-use and security that is consistent with the ProcessWire core, and doesn't leave you wanting more. With LoginRegisterPro, you no longer have to worry about how to safely register, confirm and authenticate front-end users for your sites or applications.


### Features

**General features**

- Front-end secure login form that uses email address as login name.
- Front-end secure new registration form with fully configurable fields.
- Front-end secure profile edit form with fully configurable fields.
- Email confirmation of new user registrations with randomly generated codes.
- Users can register on one computer and confirm it on another.
- Support for optional front-end “forgot password” reset capability.
- Optional ability for users to delete their own accounts.
- Optional ability to login user automatically after account confirmation.

**Security features**

- Support for logins with two-factor authentication (TFA).
- Support for Google reCAPTCHA on registration form.
- Support for blocking emails or IPs in [stopforumspam.com](https://stopforumspam.com) database.
- Support for throttling of logins to block dictionary attacks.
- Login and registration forms are protected by intelligent honeypots.
- User must confirm pass to change email, pass, TFA or account deletion.
- Ability to set which fields should also require password confirmation.
- Support for email whitelist, useful for company intranets and more.
- Support for keyword matching blacklists on emails to block registration.
- Registrations stored in DB, converted to users after email confirmation.
- All forms use CSRF protection (when not disabled in ProcessWire).
- Session fingerprinting also remains active when not disabled in ProcessWire.
- Configurable expiration of non-confirmed registrations.
- Optionally require new user to re-confirm password before account creation.
- Many other security improvements relative to original LoginRegister module.

**Customization features**

- Ability to assign custom role(s) to new accounts.
- Ability to control what roles can login on the front-end.
- Strong, well documented API that keeps you in control of action + output.
- Ability to customize markup output by the module.
- Ability to specify WireMail module to use for confirmation emails.
- Full control over the markup + content of the confirmation emails.
- Full control over the randomly generated code type and length.
- 30+ hookable methods to maximize customizability when you need it.


### Configuration

There's already a lot of words in this post and not many visuals, so lets just look at a screenshot of the module config screen. This might look like a lot, but this is with all of the options open (they are usually collapsed except when being edited). But as you can see, this module is very configurable and gives you a lot of control over what it does.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2686/pwlrp-config.png)


### Compared to LoginRegister

If you are familiar with the original LoginRegister module, here’s a few of the differences that you will find in LoginRegisterPro. The module is re-imagining of the LoginRegister module, written from the ground up with improvements in nearly every aspect. Below we’ll refer to LoginRegister as LR and LoginRegisterPro as LRPro:


### How it works

LoginRegisterPro operates off of a single Page in your website to render and process forms for Login, Registration and Profile editing. You only have to tell the module where to place its output, and it does the rest.

Guests may register to create a new account. User accounts are not actually created until validated by an email sent to the user. They receive a link containing a confirmation code. When clicked on (or pasted in manually after registration) the user account is then created. (Additional confirmation steps can also be optionally enabled). At this point, the user is now confirmed and can login (or be logged-in automatically).

Once users are logged-in, they are allowed to edit their Profile, which is where they can do things like change their password or email address, enable two-factor authentication, or modify any fields you’ve configured. Outside of that, LoginRegisterPro exists to support your front-end user account needs and it’s up to your configuration of ProcessWire’s access control—or your own logic—to determine what the users can access and do in your site/application.

Users that have accounts created through LoginRegisterPro automatically receive a role named “login-register” or other(s) that you configure. This enables you to assign this role (or roles) for “view” permission on one or more templates, so that certain pages in your website are only visible to users in that role.

Alternatively (or in addition) you might use your own logic in template files. For instance, if you wanted to only display a field named “member_notes” to users that are logged-in, you could do so like this:

```
if($user->isLoggedIn()) echo $page->member_notes;
```

LoginRegisterPro takes care of all of the difficult parts of validating, creating and authenticating users on your website, and making sure those users can manage their own account. But it doesn't place any limitations upon what you can do with those logged-in users your own. Whether that is building a website with a subscribers or members section, maintaining users in an online store, managing users for submitting or modifying content in your own forms, or anything else you can imagine — my hope is that LoginRegisterPro provides the foundation you need to accomplish your front-end user needs.


### Screenshots

Below are a couple of screenshots that demonstrate how the login and register forms look on this website. Of course, how they actually look will depend entirely on how you style and customize them and what fields you add to your registration form.

Next week I'll be finishing up the documentation for this module and then releasing it, and working on ProcessWire core 3.0.148 RC2. Thanks for reading, have a great weekend, and be sure to check in at [ProcessWire Weekly](https://weekly.pw) this weekend.
