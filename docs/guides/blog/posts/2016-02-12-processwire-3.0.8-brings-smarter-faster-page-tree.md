# ProcessWire 3.0.8 brings smarter, faster page tree

Source: https://processwire.com/blog/posts/processwire-3.0.8-brings-smarter-faster-page-tree/

## Sections


## Smarter/faster page tree and an update on ProDrafts

12 February 2016 by Ryan Cramer [ 5 Comments](/blog/posts/processwire-3.0.8-brings-smarter-faster-page-tree/#comments)


### ProcessWire 3.0.8

This week we've got a really nice improvement to ProcessWire's page tree, something that I believe everyone that uses the ProcessWire admin will appreciate. Also a big focus this week was on ProDrafts and wrapping that up so that we can release it and make it available to you. More on both of these below!


## ProDrafts coming next week

ProDrafts is a module I've had in development for quite some time. It enables you to maintain separate live and draft versions of any page. The draft version can be manipulated, viewed and compared separately from the live version.

While ProcessWire itself can provide drafts of unpublished pages, ProDrafts can provide drafts of published pages, enabling you to make as many edits as you'd like before deciding to publish them to the live version of the page. This also enables greater workflow possibilities as it's now possible to have users propose edits to pages, while someone else can approve them.


### Ramping back up

Once things really got going with ProcessWire 3.0, I took my focus off of ProDrafts for a bit to dedicate as much focus as possible to PW3. Especially since some things in PW3 could affect our approach in ProDrafts. But now that I think PW3 is really getting pretty solid, I'm back on ProDrafts and spent the last week working to wrap things up. In fact, so much progress was made this week that I think we'll be ready for our first beta release next week, and I'm very excited about that.


### Versions coming soon too

In the interest of releasing it sooner rather than later, I decided to scale back the plans for version 1 and make it focus exclusively on drafts (per the original intention, rather than both drafts and versions). Versions will still be coming in the next version, and actually all the code to manage them is already present in ProDrafts. But they are disabled in version 1 since I feel the versions feature is more "alpha" state, while the drafts feature is more "beta" state. I'm comfortable releasing a Pro module initially in a beta state, but not in an alpha state. I didn't want the versions feature to hold things up, since most are more interested in the drafts feature. So the versions feature will be delayed for a bit while I do further testing and development to work out any possible kinks. Though it should be noted that even at present, the versions feature works quite well, so it's really not far off.


### Release model

Like we've done with the initial beta release of most Pro modules, the price of ProDrafts will be discounted with a coupon code until we are officially out of beta and/or have the versions feature ready. We will likely use a pricing model similar to ProFields since we think ProDrafts is one of those modules you'll likely want to use on many sites you work with, unlike modules like FormBuilder that you might only need for 1 site at a time. If your experience is the same as mine, once you start using ProDrafts, you'll find you want it in a lot of places.


## Page tree upgrades

This week's ProcessWire version is 3.0.8 and introduces a really useful addition to our page list / page tree. The concept is simple. Wherever you last left the page tree is where it will be when you return to it.


### Smarter page lists

What this means is that if you've drilled down to several pages in your page list (thus making them "open" in the tree), they will remain open until closed… regardless of where else you navigate to in the meantime. You will never lose your spot, nor do you have to wait for the tree to load. Simply click the "Pages" tab and you will immediately return to where you left.


### Faster page lists

You might be familiar with the concept of pre-opened pages already, as it's essentially the behavior you get if you click a breadcrumb item at the top of the page editor. But there's actually a big difference here too, in that there is no more waiting for the page tree to open each page. It now does it all in one shot... no more multiple-ajax calls to render an opened tree. Meaning, no more waiting to get to where you want to go. This is the case regardless of whether you click a breadcrumb in the page editor, or click the "Pages" tab in your admin.


### Works with paginated lists too

Some of you with lots of pages in your site are aware that when it comes to pagination in the page tree, there has never been an easy way to return to the spot where you left it. If you had edited a page on the 50th pagination of a page list, then you could get back relatively easily to the parent, but would still have to navigate through all the pagination to get back to where you were.

That's all changed in ProcessWire 3.0.8. The smarter page tree remembers your last pagination too:

I've been using this update locally for the last couple of days and think it's such a nice improvement that I'd never want to go without again. I'm interested to hear what you think too. That's all for this week. Hope you all have a great weekend and remember to read the [ProcessWire Weekly](http://weekly.pw).
