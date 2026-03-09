# test if the uncertainty propagation for ND dodi and core is working and then produce C/E
import subprocess
import sys
import shutil
from pathlib import Path

import matplotlib as mpl
mpl.rcParams["text.usetex"] = shutil.which("latex") is not None

ROOT = Path(__file__).resolve().parents[1]
TEST_DATA_DIR = Path(__file__).parent / "test_data"

def run_script(tmp_path, *args):
    proc = subprocess.run(
        [sys.executable, *args],
        cwd=tmp_path,  # <-- working directory is temp folder
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, (
        f"Command failed: {' '.join(args)}\n"
        f"stdout:\n{proc.stdout}\n"
        f"stderr:\n{proc.stderr}\n"
    )

arg_csv="csv_data="+str(ROOT / "tests" / "test_case.xlsx")
ard_dosi="csv_dosi="+str(ROOT / "tests" / "test_data" / "dosi.xlsx")
arg_case=str("lcase=expNi_in2")
gr="gr_order=4" # aggregate spectra by 2^gr_order to decrease ram usage, can affect precision if too small
# print(arg_csv)
# exit()
def test_my_script(tmp_path):
    dest_data = tmp_path / "test_data"
    shutil.copytree(TEST_DATA_DIR, dest_data)

    run_script(
        tmp_path,
        str(ROOT / "Scripts" / "Spectrometry" / "ratioeff5.py"),
        arg_csv, ard_dosi, arg_case, "plot=False"
    )
    run_script(
        tmp_path,
        str(ROOT / "Scripts" / "Uncertainties" / "nducup14_WIP.py"),
        arg_csv, ard_dosi, arg_case
    )
    run_script(
        tmp_path,
        str(ROOT / "Scripts" / "Uncertainties" / "nducup_nuis4.py"),
        arg_csv, ard_dosi, arg_case, gr
    )
    run_script(
        tmp_path,
        str(ROOT / "Scripts" / "Analysis" / "irrad2hpge_21_WIP.py"),
        arg_csv, ard_dosi, arg_case, "t_corr=True", "load_nuis=True", "load_pos=False",
        "which_norm=Custom", "Exp_only=False",  "CoC_mode=False", "No_cov=False"
    )