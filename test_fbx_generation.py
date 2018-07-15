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
import render

# Config
logger = config.get_logger()

# Constants
output_path = './target'


# Data builders
def load_dataframe():
    analysis_filepath = Path('./437a7e57797001a8a7eb3bebd6255461e4c8ea43-analysis.csv')
    df = pd.read_csv(filepath_or_buffer=str(analysis_filepath))
    return df


# Tests
class TestAggregation(unittest.TestCase):

    def setUp(self):
        logger.debug("Set-up")
        if not os.path.exists(output_path):
            os.makedirs(output_path)

    def tearDown(self):
        logger.debug("Tear-down")

    def test_to_logging(self):
        df = load_dataframe()
        assert len(df)
        render.to_logging(df,
                          z_column='bollinger_cash_and_asset_value',
                          x_column='no_of_std',
                          y_column='lookback_period')

    def test_to_3d_scatter(self):
        visualisation_type = 'three_d_scatter'
        file_type = '.png'
        output_filepath = Path(output_path, visualisation_type).with_suffix(file_type)

        df = load_dataframe()
        assert len(df) > 0
        render.to_3dscatter(df,
                              z_column='bollinger_cash_and_asset_value',
                              x_column='no_of_std',
                              y_column='lookback_period',
                              output_filepath=output_filepath,
                              figure_filter=file_type)
        assert len(df) > 0
        assert len(df) is not None

    def test_generate_simple_object(self):
        df = load_dataframe()
        assert len(df)
        # Inline plot for 3d scatter
        # then split for mapplotlib and FBX


if __name__ == '__main__':
    unittest.main()
