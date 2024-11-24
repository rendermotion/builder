
from builder.pipeline import environment
import importlib
try:
    from mgear.shifter import io
    from mgear.shifter import guide_manager
except:
    guide_manager=None
    io = None
    print('mgear not found')
import pymel.core as pm
from pathlib import Path
import os
importlib.reload(environment)


def export_template():
    pm.select('guide')
    granny = environment.Environment()
    if not granny.data.exists():
        granny.data.mkdir(parents=True, exist_ok=True)
    io.export_guide_template('{}/guides.json'.format(granny.data))


def import_template():
    asset_env = environment.Environment()
    file_path = '{}/guides.json'.format(asset_env.data)

    if os.path.exists(file_path):
        io.import_guide_template('{}/guides.json'.format(asset_env.data))
    else:
        print('no guides template found at path {}'.format(file_path))


def build_from_data_guides():
    asset_env = environment.Environment()
    file_path = '{}/guides.json'.format(asset_env.data)
    if os.path.exists(file_path):
        io.import_guide_template(f'{asset_env.data}/guides.json')
    else:
        print(f'no guides template found at path {file_path}')


def build_template():
    if pm.ls('guide'):
        pm.select('guide')
        guide_manager.build_from_selection()
    else:
        print('no guide found on the scene')



if __name__ == '__main__':
    import_template()
    build_template()