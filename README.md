# open-data-test-bonus
open-data-test-bonus



# GDAL Driver issue
Before running this test, please make sure gdal is installed correctly with the JP2OpenJPEG driver,
You can use `gdalinfo --formats` to make sure the driver is inside
Otherwise, gdal will use jasper to handle jp2 format image, which will limit the handled size and crash if the image is too big


# Run the program directly in local
* go to the folder

* install the requirements first :
`pip3 install -r requirements.txt`

* run :
`python3 main.py`



# Run the program via Docker in local
* go to the folder and build the docker :
`docker build -t open-test-gis .`

* run the docker container cmd (replace [A FOLDER IN YOUR HOST MACHINE], where you will find the image cropping result file) :
`docker run -v [A FOLDER IN YOUR HOST MACHINE]:/usr/local/bin/test/output open-test-gis`
