import argparse
import os 
import shutil
import subprocess
import winreg
import pygame
import random
import json


pygame.init()
client_dir = os.getcwd()
cur_dir = os.path.abspath(os.path.dirname(__file__))
python = f"{cur_dir}\\Python\\python.exe"
def build_method(icon,dist,name):
    items_to_delete = os.listdir(os.path.join(cur_dir, "run"))
    for item in items_to_delete:
        if(item != "orochi"):
            item_path = os.path.join(cur_dir, "run", item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
    items_to_copy = os.listdir(client_dir)
    for item in items_to_copy:
        if("src" in item or "scripts" in item or item =="main.py"):
            source = os.path.join(client_dir, item)
            destination = os.path.join(cur_dir, "run", item)
            if os.path.isdir(source):
                shutil.copytree(source, destination)
            else:
                shutil.copy(source, destination)
        else:
            continue

    build = f'{python} -m PyInstaller {name} --noconfirm --onefile --windowed {icon} {cur_dir}/run/main.py {dist} --add-data {cur_dir}/orochi;orochi --add-data {cur_dir}/run/src;src --add-data {cur_dir}/run/scripts;scripts '
    print( build)
    subprocess.run(["cmd", "/c",build])
    print("Done!")
def main():
    global client_dir
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Command")
    parser.add_argument("--name", help="Name of project")
    parser.add_argument("--location", help="Location of project")
    parser.add_argument("--icon", help="Icon of build project in .ico")
    parser.add_argument("--dist", help="Dist of build project")
    parser.add_argument("--usejson", help="Use json to build?")
    parser.add_argument("--bat", help="Use bat to run?")
    args = parser.parse_args()
    command = args.command
    if(command == "create"):
        print("Creating a new project...")
        name = "orochi_game" if not args.name else args.name
        location = client_dir if not args.location else args.location
        shutil.copytree(f"{cur_dir}/project_sample",f"{location}/{name}")

        with open(f"{location}/{name}/commands/open.bat", 'w') as f:
            f.write(f'{location}/{name}/lapce.exe {location}/{name}/')
        with open(f"{location}/{name}/commands/build.bat", 'w') as f:
            f.write(f'orochi build --usejson true')
        with open(f"{location}/{name}/commands/run.bat", 'w') as f:
            f.write(f'orochi run --bat true')
    if(command == "open"):
        print("Openning project with Lapce...\nhttps://github.com/lapce/lapce")
        if(os.path.exists(f"{client_dir}/main.py")):
            run = f'{client_dir}/lapce.exe {client_dir}'
            subprocess.run(["cmd", "/c",run])
        else:
            print("A orochi project need a main.py file!")
    if(command == "run"):
        if(args.bat == "true"):
            client_dir += "/../"
        audio_files = ['/sounds/orochi.mp3', '/sounds/orochi1.wav', '/sounds/orochi2.wav', '/sounds/orochi3.wav', '/sounds/orochi4.wav', '/sounds/orochi5.wav']
        selected_audio_file = random.choice(audio_files)
        orochi_wakeup = pygame.mixer.Sound(cur_dir + selected_audio_file)
        notif = pygame.mixer.Sound(cur_dir + '/sounds/notif.mp3')
        notif.set_volume(0.2)
        notif.play()
        orochi_wakeup.set_volume(0.4)
        orochi_wakeup.play()
        print("Running project...")
        items_to_delete = os.listdir(os.path.join(cur_dir, "run"))
        for item in items_to_delete:
            if(item != "orochi"):
                item_path = os.path.join(cur_dir, "run", item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
        items_to_copy = os.listdir(client_dir)
        for item in items_to_copy:
            if("src" in item or "scripts" in item or item =="main.py"):
                source = os.path.join(client_dir, item)
                destination = os.path.join(cur_dir, "run", item)
                if os.path.isdir(source):
                    shutil.copytree(source, destination)
                else:
                    shutil.copy(source, destination)
            else:
                continue


        if(os.path.exists(f"{cur_dir}/run/main.py")):
            run = f'{python} {cur_dir}/run/main.py'
            subprocess.run(["cmd", "/c",run])
        else:
            print("A orochi project need a main.py file!")

    if(command == "build"):
        print("Building... Wait...")
        if(args.usejson == "true" or args.usejson == "True"):
            with open(f'{client_dir}/build_settings.json', 'r') as file:
                settings = json.load(file)
            client_dir += "/../"
            icon = f"--icon {settings['icon']}" if settings['icon'] != "" else f'--icon {cur_dir}/orochi/src/orochi_icon.ico'
            dist = f"--dist {settings['dist']}" if settings['dist'] != "" else f"--dist {client_dir}"
            name = f"--name {settings['name']}" if settings['name'] != "" else f"--name my_orochi_game"
            build_method(icon,dist,name)
        else:
            icon = f'--icon {args.icon}' if args.icon else f'--icon {cur_dir}/orochi/src/orochi_icon.ico'
            dist = f'--dist "{args.dist}"' if args.dist else f"--dist {client_dir}"
            name = f'--name {args.name}' if args.name else f"--name my_orochi_game"
    
            build_method(icon,dist,name)
    if(command == "package-install"):
        if(args.name):
            command = f"{python} -m pip install {args.name}"
            subprocess.run(["cmd", "/c",command])
        else:
            print("You need to give a name!")
    if(command == "package-uninstall"):
        if(args.name):
            command = f"{python} -m pip uninstall {args.name}"
            subprocess.run(["cmd", "/c",command])
        else:
            print("You need to give a name!")

if __name__ == "__main__":
    main()