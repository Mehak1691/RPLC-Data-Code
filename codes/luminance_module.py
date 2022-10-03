import numpy as np
from PIL import Image, ImageDraw
import os
import time
import concurrent.futures
import pandas as pd


class luminance():
    
    finished = 0
    
    def __init__(self, path):
        
        self.filename_arr = [] 
        self.luminance_arr = [] 
        self.data_frame = {'File Name': self.filename_arr,
                            'Luminance': self.luminance_arr}
        self.directory = path
        # changing current working dir
        os.chdir(self.directory)
        
    
    def generate_csv_file(self):
        print('Generating .csv file')
        df = pd.DataFrame(self.data_frame)
        df.to_csv(os.path.join(os.getcwd(), 'luminance.csv'), index=False, header=True)
    
    def loop_over_files(self):
        print('Looping files....')
        # check if edited folder is present or not
        if os.path.isdir('edited') == False:
            os.mkdir('edited')
        
        ### Multi-Threading
        try:
            with concurrent.futures.ProcessPoolExecutor() as executor:
                # mapping                   ->func         ->list of file paths
                results = executor.map(self.process_file, os.listdir(os.getcwd()))
                
                for filename, luminance in results:
                    self.filename_arr.append(filename)
                    self.luminance_arr.append(luminance)
                    
        except Exception as error:
            print('Exception Handling: Something wrong with {}'.format(error))
        
    
    def process_file(self, filename):
           
        if filename != 'edited':
        
            print('Processing {}.'.format(filename))
            
            # initializing arrays
            Rarr = np.array([])
            Garr = np.array([])
            Barr = np.array([])
            # loading image
            im = Image.open(filename)
            # converting to RGB
            rgb_im = im.convert('RGB')

            # looping every pixel
            for w in range(1, rgb_im.width):
                for h in range(0, rgb_im.height):
                    # getting RGB
                    r, g, b = rgb_im.getpixel((w, h))
                    # appending RGB in respective arrays
                    Rarr = np.append(Rarr, r)
                    Garr = np.append(Garr, g)
                    Barr = np.append(Barr, b)
                    
            # applying formula and averaging it
            luminance = np.average(np.sqrt( 0.299*Rarr**2 + 0.587*Garr**2 + 0.114*Barr**2 ))
            # modifing the image
            draw = ImageDraw.Draw(rgb_im)
            # defining text and it's coordinates
            draw.text((rgb_im.width //2, rgb_im.height // 4), "Luminance: {}".format(luminance))
            # saving new image in edited folder in current working dir
            new_file_name, ext = filename.split('.')
            edited_dir = os.path.join(os.getcwd(), 'edited')
            rgb_im.save(os.path.join(edited_dir, new_file_name + '(edited)' + '.' + ext))
            
            print('Finished {}'.format(filename))
            # Returning
            return [filename, luminance]
            
if __name__ == "__main__":
    
    # timer start
    start = time.perf_counter()
    # initailizing obj
    lumi_obj = luminance('C:\\Users\\60199\\Desktop\\Semidark\\images\\demo')
    #('G:\\Mehak\\Luminance\\img\\test')
    # processing files
    lumi_obj.loop_over_files()
    # genrating csv
    lumi_obj.generate_csv_file()
    # timer start
    end = time.perf_counter()
    
    print('With Muti-Processing took {0} minute(s) to process {1} images'.format((end - start)/60, len(lumi_obj.data_frame['luminance'])))