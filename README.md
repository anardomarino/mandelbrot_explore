# Mandelbrot Explorer

## Usage

```bash
./mandelbrot.py [FILE_NAME]
```
Execute the above bash command in the root directory. If permission is denied, you may modify the permissions by running:
```bash
chmod 777 mandelbrot.py
```
This allows all users to access the mandelbrot file and its functions.
If Python is installed somewhere other than the /bin/ folder, you may also run the program by running:
```bash
[python] mandelbrot.py [FILE_NAME] 
```
Where FILE\_NAME is the name of the image to be generated (omit the .jpg, as that is added automatically).

## DEBUG
When set to `True`, crosshairs will appear on the developed image, allowing the user to fine tune the X\_SHIFT and Y\_SHIFT parameters to control where the next fractal zoom will be cenetered.

## ZOOM\_FACTOR
Set to 100 initially, with increasing values corresponding to an increasing zoom.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

