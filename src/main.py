from os import path
import os
import lib.utils as utils
import json

def main ():

    dir_name = path.dirname(path.dirname(__file__))

    # Test 1
    print('\n-- Running test 1 ...')
    with open(path.join(dir_name, 'data', 'test1-1.json'), 'r') as f:
        data = json.loads(f.read())
        output = utils.transform_geometry(data, 'epsg:4326', 'epsg:2154')
        print('-- Test 1.1 result: ', output)

    with open(path.join(dir_name, 'data', 'test1-2.json'), 'r') as f:
        data = json.loads(f.read())
        output = utils.transform_geometry(data, 'epsg:2154', 'epsg:4326')
        print('-- Test 1.2 result: ', output)

    # Test 2
    print('\n-- Running test 2 ...')
    with open(path.join(dir_name, 'data', 'test2.json'), 'r') as f:
        data = json.loads(f.read())
        box = utils.get_bounding_box(data)
        print('-- Test2 result (bounds) :', box)
        output = utils.box_to_geometry(box)
        print('-- Test 2 result (geojson) : ', output)


    # Test 3
    print('\n-- Running test 3 ...')
    with open(path.join(dir_name, 'data', 'test3.json'), 'r') as f:
        data = json.loads(f.read())
        box = utils.get_bounding_box(data)

        image_path = path.join(dir_name, 'data', '2A-2016-1225-6085-LA93-0M20-E080.jp2')

        output_dir = path.join(dir_name, 'output')
        if (not path.isdir(output_dir)):
            os.makedirs(output_dir)

        output = utils.crop_image_by_box(image_path, output_dir, box, 'epsg:4326')
        print('-- Test 3 Ok, check file :', output)



main()
