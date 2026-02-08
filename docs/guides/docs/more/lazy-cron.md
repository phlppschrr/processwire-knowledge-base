# Lazy Cron

Source: https://processwire.com/docs/more/lazy-cron/

## Summary

This core module provides hooks that are automatically executed at various intervals.

## Key Points

- This core module provides hooks that are automatically executed at various intervals.
- It is called 'lazy' because it's triggered by a pageview, so the interval is guaranteed to be at least the time requested (and maybe more) rather than exactly the time requested. The more pageviews your site gets, the closer it is. This is fine for most cases, but if you need it to be fully accurate I'll describe how you can make it not-lazy a little further down.
- This is a core module included with ProcessWire 2.1+. Go to Admin > Modules and click "check for new modules". Then click the "install" button for the LazyCron module. LazyCron is now installed and ready to be used by other modules or via the API.

## Sections


### How to install

This is a core module included with ProcessWire 2.1+. Go to Admin > Modules and click "check for new modules". Then click the "install" button for the LazyCron module. LazyCron is now installed and ready to be used by other modules or via the API.


### Hookable time intervals

These are the function names you can hook from LazyCron. The function names describe the time intervals they provide. If you think I'm missing any important time intervals, please let us know and we can add more.


## How to use Lazy Cron

This module is mainly of use inside the API and to other modules. You hook one of the named intervals mentioned in the list above, and the function you provide will be executed at approximately that time interval. Here's how you do it, both from a class (module) and outside of one:


### Usage in a class/module


### Procedural usage (like in a template or elsewhere in the API):


### Arguments provided to the hooks

If desired, you can retrieve the number of seconds that have actually elapsed since your hooked function was last called:


## How Lazy Cron works

When installed, LazyCron hooks into ProcessWire's ProcessPageView::finished() method. This ensures that the scheduled tasks are executed after the pageview has already been delivered rather than before or during it. This hopefully avoids any perceived slowdown if the scheduled tasks take time.


### How to make it not-lazy

In most cases, the way that LazyCron works out of the box is just fine. But if your need requires assurance that the module will always execute at exactly the interval you need (rather than possibly later), you need to setup a real cron job to trigger a pageview in your site. So if you needed accuracy to 1 minute, you'd setup a cron job to execute every one minute, and pull a page from the site. There are any number of ways you could pull a page from your site, but here is one using wget:
