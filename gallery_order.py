# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Configuration for the order of gallery sections and examples.
# Paths are relative to the conf.py file.
#
# File strongly inspired by the matplotlib project
#


from sphinx_gallery.sorting import ExplicitOrder

# Gallery sections shall be displayed in the following order.
# Non-matching sections are inserted at the unsorted position

UNSORTED = "unsorted"

examples_order = [
    # '../galleries/examples/lines_bars_and_markers',
    # '../galleries/examples/images_contours_and_fields',
    # '../galleries/examples/subplots_axes_and_figures',
    # '../galleries/examples/statistics',
    # '../galleries/examples/pie_and_polar_charts',
    # '../galleries/examples/text_labels_and_annotations',
    # '../galleries/examples/color',
    # '../galleries/examples/shapes_and_collections',
    # '../galleries/examples/style_sheets',
    # '../galleries/examples/pyplots',
    # '../galleries/examples/axes_grid1',
    # '../galleries/examples/axisartist',
    # '../galleries/examples/showcase',
    # UNSORTED,
    # '../galleries/examples/userdemo',
    "../examples/models/spatial",
    "../examples/models/spectral",
    "../examples/models/temporal",
    "../examples/tutorials/starting",
    "../examples/tutorials/data",
    "../examples/tutorials/analysis-1d",
    "../examples/tutorials/analysis-2d",
    "../examples/tutorials/analysis-3d",
    "../examples/tutorials/analysis-time",
    "../examples/tutorials/api",
    "../examples/tutorials/scripts",
    UNSORTED
]

gallery_order = [
    "user-guide/model-gallery",
    "tutorials",
    UNSORTED
]

# tutorials_order = [
#     '../galleries/tutorials/introductory',
#     '../galleries/tutorials/intermediate',
#     '../galleries/tutorials/advanced',
#     UNSORTED,
#     '../galleries/tutorials/provisional'
# ]

folder_lists = [examples_order, gallery_order]

explicit_order_folders = [fd for folders in folder_lists
                          for fd in folders[:folders.index(UNSORTED)]]
explicit_order_folders.append(UNSORTED)
explicit_order_folders.extend([fd for folders in folder_lists
                               for fd in folders[folders.index(UNSORTED):]])


class MplExplicitOrder(ExplicitOrder):
    """For use within the 'subsection_order' key."""
    def __call__(self, item):
        """Return a string determining the sort order."""
        if item in self.ordered_list:
            return f"{self.ordered_list.index(item):04d}"
        else:
            return f"{self.ordered_list.index(UNSORTED):04d}{item}"

# Subsection order:
# Subsections are ordered by filename, unless they appear in the following
# lists in which case the list order determines the order within the section.
# Examples/tutorials that do not appear in a list will be appended.

list_all = [
    #  **Tutorials**
    #  introductory
    "overview", "analysis_1", "analysis_1",
    #  data exploration
    "hess", "cta", "fermi_lat", "hawc",
    #  data analysis
    #  1d
    "cta_sensitivity", "spectral_analysis", "spectral_analysis_hli", "spectral_analysis_rad_max",
    "extended_source_spectral_analysis", "ebl", "sed_fitting", "spectrum_simulation",
    #  2d 
    "detect", "ring_background", "modeling_2D",
    # 3d
    "cta_data_analysis", "analysis_3d", "flux_profiles", "energy_dependent_estimation", "analysis_mwl",
    "simulate_3d", "event_sampling", "event_sampling_nrg_depend_models",
    # time
    "light_curve", "light_curve_flare", "variability_estimation", "time_resolved_spectroscopy",
    "pulsar_analysis", "light_curve_simulation",
    # api
    "irfs", "models", "priors", "astro_dark_matter", "maps", "mask_maps", "datasets",
    "makers", "catalog", "observation_clustering", "model_management", "fitting", "estimators",
    # scripts
    "survey_map",
    ]
explicit_subsection_order = [item + ".py" for item in list_all]


class MplExplicitSubOrder(ExplicitOrder):
    """For use within the 'within_subsection_order' key."""
    def __init__(self, src_dir):
        self.src_dir = src_dir  # src_dir is unused here
        self.ordered_list = explicit_subsection_order

    def __call__(self, item):
        """Return a string determining the sort order."""
        if item in self.ordered_list:
            return f"{self.ordered_list.index(item):04d}"
        else:
            # ensure not explicitly listed items come last.
            return "zzz" + item


# Provide the above classes for use in conf.py
# sectionorder = MplExplicitOrder(explicit_order_folders)
# subsectionorder = MplExplicitSubOrder

sectionorder = MplExplicitOrder(explicit_order_folders)
subsectionorder = MplExplicitSubOrder

# def sectionorder():
#     return MplExplicitOrder(explicit_order_folders)
#
# def subsectionorder():
#     return MplExplicitSubOrder(explicit_subsection_order)