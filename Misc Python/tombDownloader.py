## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally

## Pirmary loop for downloading all the files
for i in range(1,204):
    image_url = f"https://online.anyflip.com/qloz/oeim/mobile/files/{i}.jpg"
    filename = image_url.split("/")[-1]


    print(f'attempting to download number {filename} from url {image_url}')
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')
