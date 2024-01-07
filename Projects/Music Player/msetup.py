from cx_Freeze import sys,setup, Executable
includefiles = [ 'music.ico', 'loupe.png','mute.png','pause.png','play.png','resume.png','stop.png','unmute.png','Vdown.png','Vup.png']
excludes = [ ]
packages = [ ]
base = None
if sys.platform =='win32':
    base = "Win32GUI"

shortcut_table=[
    ( "Desktopshortcut", #shortcut
      "DesktopFolder", #Directory
      "Shivam Music player", #name
      "TARGETDIR", #componant
      "[TARGETDIR]\musicplayer.exe", #Targate
      None, #Argument
      None, # Description
      None, #Hotkey
      None, #Icon
      None, # IconIndex
      None,# Showcmd
"TARGETDIR", #wkdir
      )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_option = {"data": msi_data}
setup(
    version = " 1.0" ,
    descripton = "Shivam Music playrer developed by Shivam ojha ",
    author = "Shivam Ojha",
    name = "Shivam Music Player",
    options = { 'build_exe' :{ 'include_files': includefiles}, "bdist_msi": bdist_msi_option, },
    executables = [
        Executable(
            script="musicplayer.py",
            base= base,
            icon="music.ico",
        )
    ]

)