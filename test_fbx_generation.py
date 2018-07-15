#!/usr/bin/env python3
# Purpose: Unit tests Pandas to FBX
# Usage:
#    source env/bin/activate
#    python3 -m unittest discover .

import sys
import os
from pathlib import Path
import pandas as pd
import random
import hashlib
import unittest

import config

# Config
logger = config.get_logger()


# Tests
class TestAggregation(unittest.TestCase):

    def setUp(self):
        logger.debug("Set-up")

    def tearDown(self):
        logger.debug("Tear-down")

    def test_generate_simple_object(self):
        df = pd.DataFrame()
        # analysis_filepath = Path('./437a7e57797001a8a7eb3bebd6255461e4c8ea43-analysis.csv')
        # output_filepath = 'three_d_scatter'
        # figure_filter = '.png'
        # , names=columns
        # df = pd.read_csv(filepath_or_buffer=str(analysis_filepath))
        # mplutils.save_3dscatter(df,
        #                        z_column='bollinger_cash_and_asset_value',
        #                        x_column='no_of_std',
        #                        y_column='lookback_period',
        #                        output_filepath=output_filepath,
        #                        figure_filter=figure_filter)
        # Inline plot for 3d scatter
        # then split for mapplotlib and FBX
        assert df is not None


if __name__ == '__main__':
    unittest.main()
