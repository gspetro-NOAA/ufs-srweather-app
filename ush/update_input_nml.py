#!/usr/bin/env python3

"""
Updates the model namelist for a variety of different settings.
"""

import argparse
import os
import sys
from textwrap import dedent

from uwtools.api.config import get_nml_config, realize

from python_utils import (
    print_input_args,
    print_info_msg,
    cfg_to_yaml_str,
)

VERBOSE = os.environ.get("VERBOSE", "true")

def update_input_nml(namelist, restart, aqm_na_13km):
    """
    Updates the FV3 ``input.nml`` file in the specified run directory

    Args:
        namelist    (str) : Path to the namelist
        restart     (bool): Whether the forecast should start from restart?
        aqm_na_13km (bool): Whether the 13km AQM configuration should be used?

    Returns:
        None: Updates ``input.nml`` with the settings provided
    """

    print_input_args(locals())
    settings = {}

    # For restart run
    if restart:
        settings["fv_core_nml"] = {
            "external_ic": False,
            "make_nh": False,
            "mountain": True,
            "na_init": 0,
            "nggps_ic": False,
            "warm_start": True,
        }

        settings["gfs_physics_nml"] = {
            "nstf_name": [2, 0, 0, 0, 0],
        }

    # For AQM_NA_13km domain for air quality modeling
    if aqm_na_13km:
        settings["fv_core_nml"] = {
            "k_split": 1,
            "n_split": 8,
        }


    print_info_msg(
        dedent(
            f"""
            Updating {namelist}

            The updated values are:

            {cfg_to_yaml_str(settings)}

            """
        ),
        verbose=VERBOSE,
    )

    # Update the experiment's FV3 INPUT.NML file
    realize(
        input_config=namelist,
        input_format="nml",
        output_file=namelist,
        output_format="nml",
        update_config=get_nml_config(settings),
        )

def _parse_args(argv):
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Update FV3 input.nml file for restart.")

    parser.add_argument(
        "-n", "--namelist",
        dest="namelist",
        required=True,
        help="Path to namelist to update.",
    )

    parser.add_argument(
        "--restart", 
        action='store_true',
        help='Update for restart',
    )

    parser.add_argument(
        "--aqm_na_13km", 
        action='store_true',
        help='Update for AQM_NA_13km in air quality modeling',
    )

    return parser.parse_args(argv)


if __name__ == "__main__":
    args = _parse_args(sys.argv[1:])
    update_input_nml(
        namelist=args.namelist,
        restart=args.restart,
        aqm_na_13km=args.aqm_na_13km,
    )
