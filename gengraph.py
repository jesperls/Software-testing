from staticfg import CFGBuilder
from os import listdir
from os.path import isfile, join


main_file = "main.py"
cfg = CFGBuilder().build_from_file(f"graphs/{main_file[:-3]}", main_file)
cfg.build_visual(f"graphs/{main_file[:-3]}", "pdf")

# import_export_file = "importexport.py"
# cfg = CFGBuilder().build_from_file(f"graphs/import_export_file", import_export_file)
# cfg.build_visual("graphs/{import_export_file[:-3]}", "pdf")

source_files = [f for f in listdir("source") if isfile(join("source", f))]
for f in source_files:
    cfg = CFGBuilder().build_from_file(f"graphs/{f[:-3]}", f"source/{f}")
    cfg.build_visual(f"graphs/{f[:-3]}", "png")
