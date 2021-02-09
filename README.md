# markdown-lightbox

An extension for python markdown.

Wraps all images in a [lightbox](http://lokeshdhakar.com/projects/lightbox2/)
link. [lightbox](http://lokeshdhakar.com/projects/lightbox2/) was created by
Lokesh Dhakar and provided under the MIT License (see LICENSE in lightbox
directory). **Lightbox CSS and JS must be included in the final HTML -- this
extension will not add those!** Copies of the lightbox CSS and JS files are
included in this repository in the lightbox folder; alternatively, these files
can be accessed at the [lightbox github
repo](https://github.com/lokesh/lightbox2)

The extension can either group all images into the same lightbox if config
option group = True (the default), or make each image have a separate lightbox
if config option group = False.

Grouping of images into lightboxes can also be done manually by specifying
@{lightbox-name} right after the opening "[" bracket of the image, e.g.,
`![@{my-lightbox-name}Here is my description](image.jpg)` (or after "[!" if
hiding the image... see below)

Hidden images (that appear in the lightbox gallery but not on the main page) can
be added by adding a "!" right after the opening "[" bracket of the image. If
adding a lightbox name using "@{name}" then the "!" goes before the "@".

To install, clone the git repo and use `pip install /path/to/repo`

Then the extension can be used by doing:

```python
import markdown
from mdlightbox import LightboxImagesExtension

md = markdown.Markdown(extensions=[LightboxImagesExtension(group = True)])

#image with default lightbox name
md.convert('![my description](image.jpg)')

#hidden image
md.convert('![!my description](image.jpg)')

#specified lightbox name
md.convert('![@{mylightbox}my description](image.jpg)')

#hidden image with specified lightbox name
md.convert('![!@{mylightbox}my description](image.jpg)')
```

For use with Flask-Flatpages:

```python
FLATPAGES_MARKDOWN_EXTENSIONS = ['mdlightbox:LightboxImagesExtension']
```

I don't think it is currently possible with Flask-flatpages to add in
configuration options. You can always change the default for 'group' in the
source code if you prefer group = False.

For use with
[MkDocs](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):

```yaml
markdown_extensions:
    - mdlightbox
```

Add to configuration file in the project directory named mkdocs.yml.
