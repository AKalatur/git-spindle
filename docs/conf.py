import cloud_sptheme as csp
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
source_suffix = '.rst'
master_doc = 'index'
project = u'git-hub'
copyright = u'2012, Dennis Kaarsemaker'
version = '1.7'
release = '1.7'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'cloud'
html_static_path = ['_static']
html_theme_options = {
    'roottarget': 'index',
    'stickysidebar': False,
}
html_theme_path = [csp.get_theme_dir()]
html_show_sourcelink = False
html_show_sphinx = False
extensions = ['ansicolor']
