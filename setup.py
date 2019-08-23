import cx_Freeze

executables =[cx_Freeze.Executable("SnakeRule.py")]

cx_Freeze.setup(
        name="SnakeRule",
        version="1.0.0",
        author="Ash",
        options = {"build_exe":{"packages":["pygame"],"include_files":["snakehead.png","snakerule_apple.png"]}},
        description = "this is my first pygame",
        executables=executables
)
