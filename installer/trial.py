import os
import wget
import argparse


parser = argparse.ArgumentParser()  
parser.add_argument('-o', '--oprating_sys', help="Methion ur OS")   
args = parser.parse_args() 



if  args.oprating_sys == 'win' or args.oprating_sys == 'windows':
    apps={
    'node':'https://nodejs.org/dist/v14.17.0/node-v14.17.0-x86.msi',
    'python':'https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe',
    'golang':'https://golang.org/dl/go1.16.4.windows-amd64.msi',
    'java':'https://javadl.oracle.com/webapps/download/AutoDL?BundleId=244581_d7fc238d0cbf4b0dac67be84580cfb4b',
    'php':'https://windows.php.net/downloads/releases/php-devel-pack-8.0.6-nts-Win32-vs16-x64.zip',
    'postgres':'https://sbp.enterprisedb.com/getfile.jsp?fileid=1257678&_ga=2.166897018.536363423.1621183480-389848539.1621183480',
    'vscode':'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user',
    'android_studio':'https://redirector.gvt1.com/edgedl/android/studio/install/4.2.1.0/android-studio-ide-202.7351085-windows.exe',
    'notepadpp':'https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9.5/npp.7.9.5.Installer.exe',
    'postman':'https://dl.pstmn.io/download/latest/win64',
    'mingw':'https://sourceforge.net/projects/mingw/files/latest/download'
    }
    save_path = os.path.abspath('.')
    user_input=input("Enter dir name: ")#User_inpt = dir
    if user_input != os.path.exists:
        try:
            os.mkdir(user_input)
        except:
            print(f"The dir You Entred {user_input} already exists")
    completeName = os.path.join(save_path, user_input)#join the Both curent Dir and New Dir

    for x in apps:
        if x == 'node':
            filename=f"{x}.msi"
            wget.download(apps[x],f"{completeName}\{filename}")
            print('-' * 15,f"{x} Done",'-' * 15)
        elif x == 'python':
            filename=f"{x}.exe"
            wget.download(apps[x],f"{completeName}\{filename}")
            print('-' * 15,f"{x} Done",'-' * 15)
        elif x == 'golang':
            filename=f"{x}.msi"
            wget.download(apps[x],f"{completeName}\{filename}")
            print('-' * 15,f"{x} Done",'-' * 15)
        elif x == 'java':
            filename=f"{x}.exe"
            wget.download(apps[x],f"{completeName}\{filename}")
            print('-' * 15,f"{x} Done",'-' * 15)
        elif x == 'php':
            filename=f"{x}.zip"
            wget.download(apps[x],f"{completeName}\{filename}")
            print('-' * 15,f"{x} Done",'-' * 15)
        elif x == 'postgres':
            filename=f"{x}.exe"
            wget.download(apps[x],f"{completeName}\{filename}")
            print('-' * 15,f"{x} Done",'-' * 15)
        elif x == 'vscode':
            filename=f"{x}.exe"
            wget.download(apps[x],f"{completeName}\{filename}")
            print('-' * 15,f"{x} Done",'-' * 15)
        elif x == 'android_studio':
            filename=f"{x}.exe"
            wget.download(apps[x],f"{completeName}\{filename}")
            print('-' * 15,f"{x} Done",'-' * 15)
        elif x == 'notepaspp':
            filename=f"{x}.exe"
            wget.download(apps[x],f"{completeName}\{filename}")
            print('-' * 15,f"{x} Done",'-' * 15)
        elif x == 'postman':
            filename=f"{x}.exe"
            wget.download(apps[x],f"{completeName}\{filename}")
            print('-' * 15,f"{x} Done",'-' * 15)
        elif x == 'mingw':
            filename=f"{x}.exe"
            wget.download(apps[x],f"{completeName}\{filename}")
            print('-' * 15,f"{x} Done",'-' * 15)
    print('-' *20,"All installation Done", '-' * 20)



elif args.oprating_sys == 'unix' or args.oprating_sys == 'kali' or args.oprating_sys == 'ubuntu' or args.oprating_sys == 'linux':
    print(f"{args.oprating_sys}")