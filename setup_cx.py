from cx_Freeze import setup, Executable

setup(
    name="PasswordAnalyzer",
    version="1.0.0",
    description="أداة تحليل كلمة المرور",
    author="grob 7rb",
    executables=[Executable("محلل_كلمة_المرور.py", base=None)],
    options={
        'build_exe': {
            'packages': ['os', 'sys', 're', 'string', 'random', 'datetime'],
            'include_files': []
        }
    }
)