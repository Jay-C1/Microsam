import os, z5py, zarr, napari, numpy as np

ROOT = r"E:/USYD/Course/25S1/5703/Micro_plugin/Test"   # ← 你的目录

# ---------- 读 committed_objects ----------
try:
    f = z5py.ZarrFile(ROOT, "r")
except Exception:
    f = zarr.open(ROOT, mode="r")

committed = f["committed_objects"][:]
print("shape:", committed.shape, "max:", committed.max())

# ---------- 打开 / 获取 napari viewer ----------
viewer = napari.current_viewer()
if viewer is None:                       # 没有就自己建一个
    viewer = napari.Viewer()

# ---------- 添加标签层 ----------
lab = viewer.add_labels(committed, name="loaded_committed_objects")

# 可见性设置
if hasattr(lab, "show_selected"):
    lab.show_selected = False
if hasattr(lab, "show_selected_label"):
    lab.show_selected_label = False

viewer.layers.move(viewer.layers.index(lab), len(viewer.layers) - 1)  # 放到最顶

napari.run()            # 仅当脚本独立运行时需要；在现有 napari Console 里执行可省略
