import configparser
import os
import shutil

config = configparser.ConfigParser()
filename = "config.ini"
config.read(filename)

def moveFiles(array, files, target):
    for x in array:
        print(f"moving {x} from {files} to {target}")
        result = shutil.move(f"{files}/{x}", f"{target}/{x}")
        if(result):
            print(f"sucessfully moved {x} from {files} to {target}")
        else: print(f"could not move {x} from {files} to {target}")

def generic_move(files, target, loc, extension):
    file_array = []
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension == extension:
            file_array.append(file)
            
    moveFiles(file_array, loc, target)

def create_target(target):
    if not os.path.exists(target):
        print(f"{target} does not exist, making the folder")
        try:
            os.mkdir(target)
            print("Directory created successfully")
            return target
        except Exception as e:
            print(f"Failed to create : {target}", e)
    else: 
        print(f"{target} already exists") 
        return target

def create_targets():
    raw_target = config['targets']['raws']
    jpg_target = config['targets']['jpgs']
    vid_target = config['targets']['film']
    raw_path = create_target(raw_target)
    jpg_path = create_target(jpg_target)
    vid_path = create_target(vid_target)
    return raw_path, jpg_path, vid_path

def main():
    files = os.listdir(config['files']['address'])
    loc = os.path.join(config['files']['address'])

    raw_target, jpg_target, vid_target =  create_targets()

    if not raw_target or not jpg_target or not vid_target:
        print("Not all files have been crated, fix")
        return

    generic_move(files, raw_target, loc, '.RAF')
    generic_move(files, jpg_target, loc, '.JPG')
    generic_move(files, vid_target, loc, '.MP4')

if __name__ == "__main__":
    main()