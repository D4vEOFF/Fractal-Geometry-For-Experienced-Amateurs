import subprocess
import sys
import os

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
    # Odebere příponu .tex pro bibtex
    base_name = os.path.splitext(main_file)[0]
    run_command(["bibtex", base_name], "běhu bibtex")
    
    # Druhý běh pdflatex (pro aktualizaci odkazů)
    run_command(["pdflatex", main_file], "druhého běhu pdflatex")
    
    # Třetí běh pdflatex (pro definitivní sestavení)
    run_command(["pdflatex", main_file], "třetího běhu pdflatex")
    
    print("Kompilace proběhla úspěšně.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main_file = sys.argv[1]
    else:
        main_file = "diploma-thesis.tex"
    
    if not os.path.exists(main_file):
        print(f"Chyba: Soubor {main_file} nebyl nalezen.")
        sys.exit(1)
    
    compile_latex(main_file)
