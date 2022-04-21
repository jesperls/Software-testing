from staticfg import CFGBuilder

cfg = CFGBuilder().build_from_file("name", "source/warehouse.py")
cfg.build_visual("name", "png")