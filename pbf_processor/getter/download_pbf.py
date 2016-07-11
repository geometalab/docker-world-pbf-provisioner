import os
import subprocess


def download_pbf(world_pbf_path=world_pbf_path, url=world_pbf_url, overwrite=False):
    if not overwrite and os.path.exists(world_pbf_path):
        return
    wget = ['wget', '-O', world_pbf_path, url]
    subprocess.check_call(wget)
    assert os.path.exists(world_pbf_path)
