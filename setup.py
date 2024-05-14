from cx_Freeze import setup, Executable

setup(
    name = "main" ,
    version = "0.1" ,
    description = "A description of the script" ,
    executables = [Executable("main.py")],
)
