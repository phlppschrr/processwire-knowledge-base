# Demo of admin theme framework

Source: https://processwire.com/blog/posts/demo-of-admin-theme-framework/

## Sections


## Demo of admin theme framework

24 February 2017 by Ryan Cramer [ 17 Comments](/blog/posts/demo-of-admin-theme-framework/#comments)

Thanks for all of the enthusiasm from the last two weeks of blog posts. We've had lots of comments and feedback from you, which is always appreciated. This week we've got a demo setup of the admin theme framework that's been written about in the last two weeks of posts. It took me a little longer today to get it setup than planned, so I've got to keep this post really short. But that's okay, because it's always better to go and use something than it is to just read about it.

This is being developed as an admin theme framework that uses Uikit 3. While this is a fully functional admin theme, this is not intended as an admin theme design. Skilled designers like Tom Reno and others in our community will lead that effort.

[You can login to it here](http://demo.processwire.com/regular/processwire/). Login with username bloguser and password processwire3. The site is in demo mode, so it won't let you save anything, but will let you browse around and test things out. *Note: Apologies if you get an error trying to access this demo. We're having an intermittent server issue and hope to have it resolved shortly. If you get an error message when accessing the demo, please try again.*

[Last week](/blog/posts/continuing-work-on-new-admin-theme-framework/) we discussed the various presentation options available for page editor fields (Inputfields), and showed you a lot of screenshots. If you navigate to *Setup > Fields > [any-field] > Visibility > Theme settings*, you'll see how individual fields can be configured. You can also access this through field/template context, for when you want to configure the look for a field when it only appears in a specific template.

Because this is a demo and you can't actually save the field settings, I've added a "Demo" menu to the top navigation that lets you adjust some of these settings. Though note that it adjusts them for ALL fields in the page editor, which is probably not what you'd do in real life, but does get the point across for our demonstration purposes.

Note that these "demo" settings just affect the page editor fields. Also, some of the "Inputfield border" options can be combined if you'd like (such as Card + Offset).

By next week, I'm hoping to have this theme up in a GitHub repo that we can start collaborating from.


### ProcessWire 3.0.53 core

This week's dev core version is ProcessWire 3.0.53. While it contains a whole lot of code changes and additions, almost all of them are specific to supporting customizations by admin theme modules (like this one in development). As a result, if you are already running core 3.0.52, there's not much reason to download this core version just yet. But if we can get a beta version of this AdminThemeUikit module out by next week, and you want to work with it, then you'll want to upgrade your core at that time.

Thanks for reading and hope that you all have a great weekend. Enjoy reading the [ProcessWire Weekly](http://weekly.pw) tomorrow too.
