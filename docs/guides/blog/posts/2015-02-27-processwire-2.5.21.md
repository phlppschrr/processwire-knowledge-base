# Building ProcessWire with the best editing tools (2.5.21)

Source: https://processwire.com/blog/posts/processwire-2.5.21/

## Sections


## Building ProcessWire with the best editing tools (2.5.21)

27 February 2015 by Ryan Cramer [ 9 Comments](/blog/posts/processwire-2.5.21/#comments)

Before a few weeks ago, ProcessWire had the bare minimum when it comes to tools for inserting images and links into your content [from a rich text editor]. In fact, those tools were pretty much identical to how they'd been in the original release of ProcessWire 2.0 (more than 4 years ago now… has it been that long?). Most of you reading this are able to look past things like that and see that it doesn't matter too much because ProcessWire is so much more than this. Yet we can't lose sight of just how important these tools are in the bigger picture of the CMS world.


### ProcessWire and the rich text editor (as an example)

If there's one field that our clients likely interact with more than any other, it's the rich text editor (CKEditor, TinyMCE etc.). And if there is one editing tool prospective users are likely to test out, it's also likely the rich text editor. Never mind the fact that the rich text editor (RTE) is not particularly important to ProcessWire in the technical sense… it's just one Inputfield plugin module of many. You and I know that, but what makes ProcessWire special is still unknown to most.

Some have suggested that ProcessWire shouldn't even come with an RTE. But look at WordPress (a CMS built around an RTE): it owns more than 60% of the CMS market share, and powers nearly 25% of all websites in the world. This audience is very much RTE-focused, and it's one of the reasons why I think our RTE tools need to be the best they can be–to help attract people that have outgrown or are moving on from WordPress… with a tool that is truly better in every respect. WordPress is so lacking relative to ProcessWire in almost every other way, yet that doesn't matter to most of the potential users of CMS products.

Disclaimer: ProcessWire is not WordPress and does not aim to be. ProcessWire does not aim to be Laravel either.


### Our path for growth

It's always interesting to see what's happening in the framework scene, what's popular in the PHP world, or even what MODx, EE or Craft are doing. In fact, I'd love to sit back and focus on being a PHP aficionado, telling you a lot about PSR standards or PHP 7. I derive a lot of enjoyment from that for sure. But that's not how we scale ProcessWire to something truly big. We have to keep focused on what really matters now, and what will impact the experience of our users (and future users) the most. When we take a hard look at those current and future users, what really matters when it comes to growth? The current CMS landscape says a lot. We need to focus on the users of our product more than what's trending now or what our own coding passions are.

Our foundation is already strong (and we're always [improving that too](/blog/posts/processwires-roadmap-in-2015/#processwire-roadmap-for-3.0)). Our primary focus is on making consistent and incremental improvements to ProcessWire each day, and in every way–better and better. ProcessWire will always be the professional web developers CMS of choice with the most rock solid foundation behind it. But it's also got to be a lot more than that. My view is that ProcessWire's growth comes not from people outgrowing their PHP framework (a relatively small group), but from people outgrowing less powerful CMS products (a massive group).

For these reasons, I've been trying to give a lot of attention to making sure our interactive editing tools are the best they can be to compete on every level. In this post, the RTE is used as an example, since it's received focus in the last couple off weeks. But you'll see plenty of other examples in [almost every blog post here](/blog/posts/). This week our RTE link tool got a major upgrade, which I think you and your clients will like.


### New RTE link tool highlights

- Support for attributes: class, rel, title and target. Best of all, you can define what you want the options to be in the ProcessPageEditLink module configuration.
- Link to pages by typing a few characters of the page name or title (for autocomplete linking).
- Support for anchor links. If your editing area contains anchors, ProcessWire will find them and make them selectable in the link dialog.
- Auto detection of external links, with auto-assignment of attributes to external links. If you want your external links to automatically add `rel=nofollow` and `target=_blank` for example, no problem! You can also configure this from the ProcessPageEditLink module configuration.
- A live updated HTML preview of the link (for those like me that always go and click 'view source' after adding anything to an RTE). :)
- Autodetection of email addresses for mailto links.

New RTE link tool screenshots

This is the module configuration screen where you can define what attributes you want to make available for selection:

Grab ProcessWire 2.5.21 dev and please let us know how the new link tools work for you! We will continue to keep working to make sure that ProcessWire has the best editing tools available both for you and your clients.
