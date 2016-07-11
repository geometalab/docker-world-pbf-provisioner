import os

latitude_degrees = 180
longitude_degrees = 360


def cut(pbf_world_path, halvening_steps=7):
    print(_preprocess_pbf(pbf_world_path))
    # for step in range(halvening_steps):
    #     latitude_degrees_step = latitude_degrees
    #     longitude_degrees_step = longitude_degrees
    #     if (step+1) % 2 == 0:
    #         latitude_degrees_step = latitude_degrees_step / 2
    #     else:
    #         longitude_degrees_step = longitude_degrees_step / 2
    #     lat = -90
    #     long = -180
    #     while lat < latitude_degrees:
    #         lat_from = lat
    #         lat = lat + latitude_degrees_step
    #         while long < longitude_degrees:
    #             long_from = long
    #             long = long + longitude_degrees_step
    #             print(step, long_from, lat_from, long, lat)
        # print(step, latitude_degrees_step, longitude_degrees_step)


def _preprocess_pbf(pbf_world_path):
    """
    splits the world pbf into more agreeable sizes.

    :param pbf_world_path:
    :return: the generated pbf files paths
    """
    tmp_file_name = 'tmp_from_{}_{}_to_{}_{}.pbf'
    file_list = []
    for long_ in _create_bounds(-180, 180, 180):
        lat_ = (-90, 90)
        minlon, minlat, maxlon, maxlat = long_[0], lat_[0], long_[1], lat_[1]
        tmp_pbf = _cut(
                in_pbf=pbf_world_path,
                minlon=minlon,
                minlat=minlat,
                maxlon=maxlon,
                maxlat=maxlat,
                out_pbf=tmp_file_name.format(minlon, minlat, maxlon, maxlat)
        )
        for lat_ in _create_bounds(-90, 90, 90):
            minlon, minlat, maxlon, maxlat = long_[0], lat_[0], long_[1], lat_[1]
            file_list.append(
                _cut(
                    in_pbf=tmp_pbf,
                    minlon=minlon,
                    minlat=minlat,
                    maxlon=maxlon,
                    maxlat=maxlat,
                    out_pbf=tmp_file_name.format(minlon, minlat, maxlon, maxlat)
                )
            )
    return file_list


def _cut(*, in_pbf, minlon, minlat, maxlon, maxlat, out_pbf, hash_memory=5000):
    cut_command = [
        'osmconvert',
        in_pbf,
        "-b={},{},{},{}".format(minlon, minlat, maxlon, maxlat),
        "--out-pbf",
        "-o={}".format(out_pbf),
        "--hash-memory={}".format(hash_memory)
    ]
    print(" ".join(cut_command))
    return out_pbf


def _create_bounds(start, end, step):
    bounds = []
    old_value = None
    for index, i in enumerate(range(start, end + 1, step)):
        if old_value is None:
            old_value = i
            continue
        bounds.append((old_value, i))
        old_value = i
    return bounds
