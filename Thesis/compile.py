#!/usr/bin/env python3
import subprocess
import sys
import os
import argparse

def run_command(command, description):
    """Spustí daný příkaz a při chybě vypíše chybovou hlášku."""
    print("Spouštím:", " ".join(command))
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"Chyba během {description}. Ukončuji skript.")
        sys.exit(1)

def compile_latex(main_file):
    """Kompiluje LaTeX dokument s využitím bibtexu."""
    # První běh pdflatex (vytvoří .aux soubory)
    run_command(["pdflatex", main_file], "prvního běhu pdflatex")
    
    # Spuštění bibtexu (zpracuje bibliografii)
    base_name = os.path.splitext(main_file)[0]
    run_command(["bibtex", base_name], "běhu bibtex")
    
    # Druhý běh pdflatex (pro aktualizaci odkazů)
    run_command(["pdflatex", main_file], "druhého běhu pdflatex")
    
    # Třetí běh pdflatex (pro definitivní sestavení)
    run_command(["pdflatex", main_file], "třetího běhu pdflatex")
    
    print("Kompilace proběhla úspěšně.")

def cleanup_aux_files():
    """Odstraní všechny pomocné soubory vytvořené během kompilace i z podsložek."""
    # Seznam přípon pomocných souborů, které se mají odstranit
    extensions = [
        ".aux", ".log", ".bbl", ".blg", ".toc",
        ".lof", ".lot", ".out", ".fls", ".fdb_latexmk",
        ".synctex.gz", ".idx", ".ilg", ".ind", ".xmpi"
    ]
    
    for root, dirs, files in os.walk("."):
        for filename in files:
            for ext in extensions:
                if filename.endswith(ext):
                    filepath = os.path.join(root, filename)
                    try:
                        os.remove(filepath)
                        print(f"Odstraněn soubor: {filepath}")
                    except Exception as e:
                        print(f"Chyba při odstraňování souboru {filepath}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Kompilace LaTeX dokumentu s využitím bibtexu. Pomocné soubory se smažou pouze pokud je zadán parametr --clear."
    )
    parser.add_argument("main_file", nargs="?", default="diploma-thesis.tex",
                        help="Hlavní LaTeX soubor (výchozí: diploma-thesis.tex)")
    parser.add_argument("--clear", action="store_true",
                        help="Pokud je zadán, smaže pomocné soubory po kompilaci.")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.main_file):
        print(f"Chyba: Soubor {args.main_file} nebyl nalezen.")
        sys.exit(1)
    
    compile_latex(args.main_file)
    
    if args.clear:
        cleanup_aux_files()
