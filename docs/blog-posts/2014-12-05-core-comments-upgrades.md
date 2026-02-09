# ProcessWire Core Comments Upgrades

Source: https://processwire.com/blog/posts/core-comments-upgrades/

## Sections


## ProcessWire Core Comments Upgrades

5 December 2014 by Ryan Cramer [ 24 Comments](/blog/posts/core-comments-upgrades/#comments)

In the coming weeks, several upgrades are on the way for comments in ProcessWire thanks to the sponsorship support of [update AG](http://update.ch). This week we implemented the first one:


### Threaded Comments

Previously our comments system supported only a flat/chronological layout. It still supports that, but now you can have the option of enabling threaded comments in your comment field settings. If you are using the current ProcessWire dev branch, you'll see it as the "Reply Depth" option in the comments field configuration.

I made a couple demo threads in the comments section on this page for you to preview. Feel free to reply there if you'd like to test it out. (If we get some real comment threads going, I'll delete the demo ones). If you decide to use this on your own site, please consider the feature in alpha test state and let us know how it works for you. Note that if you've custom styled your existing comments, you may need to tweak a few things after enabling threaded comments… with these new capabilities comes a little bit more markup to account for. The *FieldtypeComments* core module now includes read-to-go stylesheets and JS files to use directly or as starting points.


### What's coming next for the comments Fieldtype?

- Promoted comments and/or likes.
- Support for approval of comments directly from admin notification emails.
- Notification emails for users participating in a comments thread.
- Custom defined text-formatters for comments (using PW Textformatter modules).
- Upgrades to *ProcessLatestComments* module for comment management.
- More customization options and documentation updates/additions.

[Read the next part of this post: More new comments upgrades](/blog/posts/more-new-comments-upgrades/)
