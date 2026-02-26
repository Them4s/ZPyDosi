# test if the spectro script are still working
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
# print(arg_csv)
# exit()
def test_my_script(tmp_path):
    dest_data = tmp_path / "test_data"
    shutil.copytree(TEST_DATA_DIR, dest_data)

    run_script(
        tmp_path,
        str(ROOT / "Scripts" / "Analysis" / "check10.py"),
        arg_csv, ard_dosi, arg_case, "print=True"
    )
    
    
    run_script(
        tmp_path,
        str(ROOT / "Scripts" / "Spectrometry" / "spectrum_counter11.py"),
        "csv={}/check_out/input_exemple_2020_10_15_07_55_19_Fu_p13_In-Pni-10-i.xlsx".format(tmp_path),
        "case=2020_10_15_07_55_19_Fu_p13_In-Pni-10-i", "plot=False", "serv=1"
    )
    run_script(
        tmp_path,
        str(ROOT / "Scripts" / "Spectrometry" / "spectrum_nrj2.py"),
        "tka=test_data/spectro_files/calib_spectra/2020_09_29_12_00_00_Fu_p13_Eu152-2020.TKA"
    )
