# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Gammapy documentation Sphinx configuration file.

sphinx_counter = 0
def script_sorter(fname):
    global sphinx_counter
    sphinx_counter += 1
    return fname, chr(ord('`') + sphinx_counter)
    # return (not fname.startswith("plot_")), chr(ord('`') + sphinx_counter)
    # return '<%s: %s>' % (not fname.startswith("plot_"), chr(ord('`') + sphinx_counter))
    # return chr(ord('`') + sphinx_counter)
    # return (not fname.startswith("plot_")), str(sphinx_counter)
    # return '<%s: %s>' % (not fname.startswith("plot_"), str(sphinx_counter))
    # return '<%s: %s>' % (not fname.startswith("plot_"), fname)


