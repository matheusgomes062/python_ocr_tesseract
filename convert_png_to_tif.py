from PIL import Image
im = Image.open("/home/matheus/Downloads/ocrd-train-master/letras e seus respectivos valores (c0000_14)/c0000_14_00000.png")
im.save(r'/home/matheus/Downloads/ocrd-train-master/letras e seus respectivos valores (c0000_14)/test.tif')  # or 'test.tif'
