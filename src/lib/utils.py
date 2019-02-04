from os import path
from shapely.geometry import shape, mapping, box
from shapely.ops import transform
from functools import partial

import pyproj
import gdal



def transform_geometry(geojson_geom, from_srs, to_srs):
    """Function to transform a geojson geometry

    Parameters
    ----------
    geojson_geom : object
        The geometry object in format geojson
    from_srs : object | str
        The project definition from which we want to transform, ex: epsg:4326
    to_srs : object | str
        The project definition to which we want to transform, ex: epsg:4326

    Returns
    -------
    object
        The tranformed geometry object in format geojson

    """
    geometry = shape(geojson_geom)
    project = partial(
        pyproj.transform,
        pyproj.Proj(init=from_srs),
        pyproj.Proj(init=to_srs)
    )

    res_geometry = transform(project, geometry)

    return mapping(res_geometry)



def get_bounding_box(geojson_geom):
    """Function to get a bounding box from a geojson geometry.

    Parameters
    ----------
    geojson_geom : object
        The geometry object in format geojson

    Returns
    -------
    list
        The bounding box coordinates list, [minX, minY, maxX, maxY]

    """
    geometry = shape(geojson_geom)
    return geometry.bounds



def box_to_geometry(bbox):
    """Function to get the geojson geometry from a bouding box coordinates list

    Parameters
    ----------
    bbox : list
        The bounding box coordinates list, [minX, minY, maxX, maxY]

    Returns
    -------
    object
        The geojson geometry of the bounding box

    """
    geometry = box(bbox[0], bbox[1], bbox[2], bbox[3])
    return mapping(geometry)



def crop_image_by_box(image_path, output_dir, box, box_srs=None):
    """Short summary.

    Parameters
    ----------
    image_path : str
        The input image file path
    output_dir : str
        The output directory
    box : list
        The bounding box coordinates list
    box_srs : object | str
        The project definition of the bounding box coordinates, ex: epsg:4326

    Returns
    -------
    None

    """
    if len(box) != 4:
        raise 'The box size is not correct'

    # The tranlsate bounding box params are [ulX, ulY, lrX, lrY] which should be [minX, maxY, maxX, minY]
    # So we should flip the Y axis
    flip_box = [box[0], box[3], box[2], box[1]]



    ds = gdal.Open(image_path)
    (image_name, image_ext) = path.splitext(path.basename(image_path))
    output_path = path.join(output_dir, '{}_cropped{}'.format(image_name, image_ext))
    ds = gdal.Translate(output_path, ds, projWin=flip_box, projWinSRS=box_srs)
    ds = None
    return output_path
