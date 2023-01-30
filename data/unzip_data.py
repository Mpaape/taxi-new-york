import zipfile
import os 


def main():
    #extracting from zip
    dataset_path = './new-york-city-taxi-fare-prediction.zip'
    zip_file = zipfile.ZipFile(file=dataset_path,mode='r')
    zip_file.extractall('.')
    zip_file.close()
    #showing files 
    print("all files in data/:")
    print("="*60)
    print(os.listdir('.'))
    print("="*60)

if __name__ == "__main__":
    main()