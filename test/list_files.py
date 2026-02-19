from pathlib import Path

curr_dir = Path.cwd()
curr_file = Path(__file__).name


for filepath in curr_dir.rglob("*.txt"):
    if ".venv" in filepath.parts:
        continue
    if filepath.name == curr_file:
        continue
    
    print(f"current file {filepath}")
    if filepath.is_file():
        contents = filepath.read_text(encoding='utf-8')
        print(f" Contents: \n {contents}")
