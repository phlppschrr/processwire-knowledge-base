# New ProcessWire modules directory

Source: https://processwire.com/blog/posts/new-processwire-modules-directory/

## Sections


## New ProcessWire modules directory

20 November 2020 by Ryan Cramer [ 17 Comments](/blog/posts/new-processwire-modules-directory/#comments)

There’s a new modules directory on the ProcessWire site now up and running. In this post we’ll cover a few details about what’s changed and what’s new.

While the data behind the directory is largely the same, the new modules directory is a major upgrade in appearance, consistency and functionality, especially when it comes to tools for module authors.

The new modules directory is also using ProcessWire’s multi-instance support to boot a copy of modules.processwire.com and to pull and manipulate data from it. There's more about that (and a lot more) in [part 1 of this post](https://processwire.com/talk/topic/24591-weekly-update-%E2%80%93%C2%A06-november-2020/), which was in the forum. This post is part 2, which focuses more on the newly added module author tools. If you are interested, I recommend reading part 1 first.

First off, as you might expect, module authors can login to edit their modules anytime (by clicking the Login/Register link in the top right corner). But they can do a lot more too…

Module authors can [create their own accounts](https://processwire.com/modules/login/register). If you are a module author, please register with the email address that your existing modules were submitted with. That way it’ll migrate your modules automatically. Though let me know if any don’t come through into your account and I can update them.

Module authors can click a button on their module page to automatically refresh the README, version, and other module information, live from GitHub.

Once a module has been approved, module authors can un-publish and publish their own modules as they see fit. They also have the ability to delete their own modules.

Trusted module authors that have been around a long time have the ability to approve their own newly submitted modules.

Users can manage their own profile, including biography, photo, two-factor authentication settings, and more. Once you’ve added a bio and a photo, it’ll show these on your [author page](https://processwire.com/modules/author/ryan-cramer/).

Users can maintain their own “favorites” list of modules that includes any modules in the directory. The plan is to show these in the public profile, but currently it only shows it to the user that created the list.

For newly submitted modules, we now require that they have a GitHub repository. The overwhelming majority of modules already do, so it seemed like a safe bet to standardize on that.

Beyond the appearance of the directory, these accounts are the biggest difference from the old modules directory, as the old directory had nothing like this. Though it also means it’s the one part of the site that has had the least testing so far. I’ve been working on it the last couple of weeks and only pushed it live to the server today. If you are a module author and have a chance to create an account, login and test it out, I’d appreciate your feedback. Also, if all of your modules don’t automatically show up in your account, please let me know so I can migrate them manually.

In addition to ProcessWire, the tools used to create the modules directory, accounts and editing ability are [LoginRegisterPro](/store/login-register-pro/), [FormBuilder](/store/form-builder/) and [FieldtypeLikes](/store/likes/). The modules directory data still comes from its own separate ProcessWire installation at modules.processwire.com, but is booted by the main ProcessWire site using ProcessWire’s [multi-instance support](/blog/posts/multi-instance-pw3/). The majority of the code behind the modules directory is now in the main ProcessWire site installation, even if all the data is still in a separate install. I found this setup to be a good learning experience and have taken a lot of notes about working with multi-instance that I hope to formulate into a good blog/post in the next few weeks.

There's still more work to do here and likely some bugs to iron out. But after spending most of the week on it, I think most of the work is now out of the way and I'm hoping to get back to focusing on the core next week. Thanks for reading, enjoy the [ProcessWire Weekly](https://weekly.pw) and have a great weekend!
