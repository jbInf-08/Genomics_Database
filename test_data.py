import subprocess
import sys
from pathlib import Path

import pandas as pd

from genomics_system import AnalysisTool, CancerGenomicsDatabase


def test_cli_load_csv_smoke(tmp_path):
    csv_path = tmp_path / "mini.csv"
    csv_path.write_text("PATIENT_ID,TP53\nP-1,Mut\nP-2,WT\n", encoding="utf-8")

    proc = subprocess.run(
        [sys.executable, "genomics_system.py", "--load-csv", str(csv_path), "--database-path", str(tmp_path / "db.json")],
        input="7\n",
        text=True,
        capture_output=True,
        check=False,
    )
    assert proc.returncode == 0
    assert "Successfully loaded 2 patient records." in proc.stdout


def test_patient_id_preserved_from_csv(tmp_path):
    csv_path = tmp_path / "mini.csv"
    csv_path.write_text("PATIENT_ID,TP53\nP-1,Mut\nP-2,WT\n", encoding="utf-8")
    db = CancerGenomicsDatabase(csv_path=str(csv_path), database_path=str(tmp_path / "db.json"))
    assert "P-1" in db.patients
    assert "P-2" in db.patients


def test_mutation_report_generation(tmp_path):
    csv_path = tmp_path / "mini.csv"
    csv_path.write_text("PATIENT_ID,TP53\nP-1,Mut\n", encoding="utf-8")
    db = CancerGenomicsDatabase(csv_path=str(csv_path), database_path=str(tmp_path / "db.json"))
    report = AnalysisTool.generate_mutation_report(db)
    assert "Mutation Report" in report
    assert "Patients loaded: 1" in report