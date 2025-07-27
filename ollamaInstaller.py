
# https://stackoverflow.com/questions/5469301/run-a-bat-file-in-windows-using-python-code
def install():
    try:
        import ollama
    except ModuleNotFoundError:
        from subprocess import Popen
        p = Popen(["cmd", "/c", "start", "installOllama.bat"], cwd=r".\.")






