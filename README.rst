==================
plonetheme.trantor
==================

Trantor Theme (based Foundation Framework).


Introduction
============

Trantor Theme is an installable Plone Theme developed by 
`Tristan Le Toullec`_ using the **theming** and **packaging** 
features available in `plone.app.theming`_.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest versión (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/tristanlt/plonetheme.trantor/raw/master/plonetheme/trantor/static/preview.png


Features
========

- Included support the `Zurb Foundation`_ framework for the `3.2.5 version`_.
- Included dropdown menu support via `webcouturier.dropdownmenu`_ package.
- It's an installable Plone Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- Also it's a simple Diazo package (Zip file).


Installation
============


Zip file
--------

If you are an end user, you might enjoy installation via zip file import.

1. Download a `zip file <https://github.com/tristanlt/plonetheme.trantor/raw/master/plonetheme.trantor.zip>`_.
2. Import the theme from the Diazo theme control panel.

Enabling the theme
^^^^^^^^^^^^^^^^^^

Select and enable the theme from the Diazo control panel. That's it!


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``plonetheme.trantor`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.trantor


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.trantor',
    ],


Usage
=====

The **Zurb Foundation** resources for this *Plone Diazo theme* are included 
into the ``plonetheme/trantor/static/`` directory: ::

	./
	├── fonts
	│   ├── accessibility_foundicons.eot
	│   ├── accessibility_foundicons.svg
	│   ├── accessibility_foundicons.ttf
	│   ├── accessibility_foundicons.woff
	│   ├── general_enclosed_foundicons.eot
	│   ├── general_enclosed_foundicons.svg
	│   ├── general_enclosed_foundicons.ttf
	│   ├── general_enclosed_foundicons.woff
	│   ├── general_foundicons.eot
	│   ├── general_foundicons.svg
	│   ├── general_foundicons.ttf
	│   ├── general_foundicons.woff
	│   ├── social_foundicons.eot
	│   ├── social_foundicons.svg
	│   ├── social_foundicons.ttf
	│   └── social_foundicons.woff
	├── foundation
	│   ├── config.rb
	│   ├── humans.txt
	│   ├── images
	│   │   └── foundation
	│   │       └── orbit
	│   │           ├── bullets.jpg
	│   │           ├── left-arrow.png
	│   │           ├── left-arrow-small.png
	│   │           ├── loading.gif
	│   │           ├── mask-black.png
	│   │           ├── pause-black.png
	│   │           ├── right-arrow.png
	│   │           ├── right-arrow-small.png
	│   │           ├── rotator-black.png
	│   │           └── timer-black.png
	│   ├── index.html
	│   ├── javascripts
	│   │   └── foundation
	│   │       ├── app.js
	│   │       ├── jquery.cookie.js
	│   │       ├── jquery.event.move.js
	│   │       ├── jquery.event.swipe.js
	│   │       ├── jquery.foundation.accordion.js
	│   │       ├── jquery.foundation.alerts.js
	│   │       ├── jquery.foundation.buttons.js
	│   │       ├── jquery.foundation.clearing.js
	│   │       ├── jquery.foundation.forms.js
	│   │       ├── jquery.foundation.joyride.js
	│   │       ├── jquery.foundation.magellan.js
	│   │       ├── jquery.foundation.mediaQueryToggle.js
	│   │       ├── jquery.foundation.navigation.js
	│   │       ├── jquery.foundation.orbit.js
	│   │       ├── jquery.foundation.reveal.js
	│   │       ├── jquery.foundation.tabs.js
	│   │       ├── jquery.foundation.tooltips.js
	│   │       ├── jquery.foundation.topbar.js
	│   │       ├── jquery.js
	│   │       ├── jquery.offcanvas.js
	│   │       ├── jquery.placeholder.js
	│   │       └── modernizr.foundation.js
	│   ├── MIT-LICENSE.txt
	│   ├── robots.txt
	│   ├── sass
	│   │   ├── app.scss
	│   │   ├── _custom4plone.scss
	│   │   └── _settings.scss
	│   └── stylesheets
	│       └── app.css
	├── foundicon-general-search.png
	├── index-c.html
	├── index-cp.html
	├── index-pc.html
	├── index-pcp.html
	├── manifest.cfg
	├── prettify
	│   ├── lang-apollo.js
	│   ├── lang-basic.js
	│   ├── lang-clj.js
	│   ├── lang-css.js
	│   ├── lang-dart.js
	│   ├── lang-erlang.js
	│   ├── lang-go.js
	│   ├── lang-hs.js
	│   ├── lang-lisp.js
	│   ├── lang-llvm.js
	│   ├── lang-lua.js
	│   ├── lang-matlab.js
	│   ├── lang-ml.js
	│   ├── lang-mumps.js
	│   ├── lang-n.js
	│   ├── lang-pascal.js
	│   ├── lang-proto.js
	│   ├── lang-rd.js
	│   ├── lang-r.js
	│   ├── lang-scala.js
	│   ├── lang-sql.js
	│   ├── lang-tcl.js
	│   ├── lang-tex.js
	│   ├── lang-vb.js
	│   ├── lang-vhdl.js
	│   ├── lang-wiki.js
	│   ├── lang-xq.js
	│   ├── lang-yaml.js
	│   ├── prettify.css
	│   ├── prettify.js
	│   └── run_prettify.js
	├── preview.png
	├── rules.xml
	└── theme.css


Contribute
==========

- Issue Tracker: https://github.com/tristanlt/plonetheme.trantor/issues
- Source Code: https://github.com/tristanlt/plonetheme.trantor


License
=======

The project is licensed under the GPLv2.

Credits
-------

- Andre Nogueira (agnogueira at gmail dot com).

.. _`Tristan Le Toullec`: http://tristan.lt/blog
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`Zurb Foundation`: https://foundation.zurb.com/
.. _`3.2.5 version`: https://github.com/zurb/foundation-sites/releases/tag/v3.2.5
.. _`webcouturier.dropdownmenu`: https://github.com/collective/webcouturier.dropdownmenu/