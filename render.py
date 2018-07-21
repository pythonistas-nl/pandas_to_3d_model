# Purpose: Utility wrappers for visualisation
# This is needed for the projections:
# from mpl_toolkits.mplot3d import Axes3D
# Recommended list: python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
# >>> import matplotlib.pyplot as plt
# >>> plt.gcf().canvas.get_supported_filetypes()
# {
#     'ps': 'Postscript',
#     'eps': 'Encapsulated Postscript',
#     'pdf': 'Portable Document Format',
#     'pgf': 'PGF code for LaTeX',
#     'png': 'Portable Network Graphics',
#     'raw': 'Raw RGBA bitmap',
#     'rgba': 'Raw RGBA bitmap',
#     'svg': 'Scalable Vector Graphics',
#     'svgz': 'Scalable Vector Graphics'
# }

import sys
import matplotlib
import datetime
from pathlib import Path

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import config
import shapes

# https://matplotlib.org/users/installing.html#macos
# xcode-select --install
# (for subprocess32)
# python3 -m pip install matplotlib
# Docs say...
# python -mpip install -U pip
# python -mpip install -U matplotlib

# x = [1,2,3]
# y = [1,2,3]
# da = {
#   z_column: [1,2,3,2,3,2,1,0,1],
#   x_column: [1,2,3,1,2,3,1,2,3],
#   y_column: [1,1,1,2,2,2,3,3,3]
# }

logger = config.get_logger()


def to_logging(df, z_column, x_column, y_column):
    da = to_dictarray(df, {z_column: [], x_column: [], y_column: []})
    dump_dictarray_head(da)
    dump_dictarray_tail(da)


def to_3dscatter(df, z_column, x_column, y_column, output_filepath):
    logger.info('Saving 3D Scatter [{}]'.format(output_filepath))
    if Axes3D is None:
        logger.warning('Axes3D is None')
    da = to_dictarray(df, {z_column: [], x_column: [], y_column: []})
    dump_dictarray_head(da)
    dump_dictarray_tail(da)
    z = da[z_column]
    x = da[x_column]
    y = da[y_column]
    fig = plt.figure()
    ax = plt.subplot(111, projection='3d')
    ax.scatter(x, y, zs=z)
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    fig.savefig(str(output_filepath))
    plt.close(fig)
    return output_filepath


def to_3dscatter_3dobject(df, z_column, x_column, y_column, output_filepath):
    logger.info('Saving 3D Scatter Object[{}]'.format(output_filepath))
    entry_point = Path(sys.argv[0])
    objects = list()
    objects.append(shapes.build_unit_cube())
    shapes.save_as_obj(objects, output_filepath, generated_by=entry_point.name, group=output_filepath.stem)


def to_dictarray(df, da):
    for df_row in df.itertuples():
        dfdict_row = df_row._asdict()
        dr = {}
        for column in da.keys():
            try:
                da[column].append(float(dfdict_row[column]))
            except Exception as e:
                da[column].append(dfdict_row[column])
    return da


def dump_dictarray_head(da, columns=None):
    if columns == None:
        columns = da.keys()
    logger.debug('head:')
    dump_dictarray_sub(da, columns, 0, 5)


def dump_dictarray_tail(da, columns=None):
    if columns == None:
        columns = da.keys()
    maxlen = dictarray_maxlen(da)
    logger.debug('tail:')
    dump_dictarray_sub(da, columns, max(0, maxlen - 5), maxlen)


def dump_dictarray_sub(da, columns, start, end):
    if columns == None:
        columns = da.keys()
    for i in range(start, end):
        row_str = '('
        for column in columns:
            if i < len(da[column]):
                row_str = '{} {}'.format(row_str, da[column][i])
            else:
                row_str = '{} --'.format(row_str)
        logger.debug('[{}]: {} )'.format(i, row_str))


def dictarray_maxlen(da):
    columns = da.keys()
    maxlen = 0
    for column in columns:
        maxlen = max(maxlen, len(da[column]))
    return maxlen
