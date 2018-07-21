#!/usr/bin/env python3
# Purpose: Unit tests Pandas to FBX
# Usage:
#    source env/bin/activate
#    python3 -m unittest discover .

import os
from pathlib import Path
import pandas as pd
import unittest

import config
import render

# Config
logger = config.get_logger()

# Constants
source_filepath = Path('./examples/plotly-gpl-data/3d-scatter.csv')
obj_filepath = Path('./examples/cube.obj')
output_path = './output'


# Data builders
def load_dataframe():
    df = pd.read_csv(filepath_or_buffer=str(source_filepath))
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
                          z_column='z1',
                          x_column='x1',
                          y_column='y1')

    def test_to_3d_scatter(self):
        visualisation_type = 'scatter_plot_3d'
        file_type = '.png'
        output_filepath = Path(output_path, visualisation_type).with_suffix(file_type)

        df = load_dataframe()
        assert len(df) > 0
        render.to_3dscatter(df,
                            z_column='z1',
                            x_column='x1',
                            y_column='y1',
                            output_filepath=output_filepath)
        assert output_filepath.exists()

    def test_generate_simple_object(self):
        visualisation_type = 'scatter_plot_3d_object'
        file_type = '.obj'
        output_filepath = Path(output_path, visualisation_type).with_suffix(file_type)
        df = load_dataframe()
        assert len(df) > 0
        render.to_3dscatter_3dobject(df,
                                     z_column='z1',
                                     x_column='x1',
                                     y_column='y1',
                                     output_filepath=output_filepath)
        assert output_filepath.exists()


if __name__ == '__main__':
    unittest.main()
